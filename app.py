from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import Vector, Query

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Azure Cognitive Services - Computer Vision setup
cog_key = "<your-computer-vision-api-key>"
cog_endpoint = "<your-computer-vision-api-endpoint>"
cog_credentials = CognitiveServicesCredentials(cog_key)
computervision_client = ComputerVisionClient(cog_endpoint, cog_credentials)

# Azure Cognitive Search setup
search_service_endpoint = "https://<your-search-service-name>.search.windows.net"
search_service_key = "<your-search-service-key>"
index_name = "product-index"
search_client = SearchClient(endpoint=search_service_endpoint, index_name=index_name, credential=AzureKeyCredential(search_service_key))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Check if a file was submitted
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        # If no file is selected
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # If file is selected and allowed
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Analyze image with Azure Computer Vision API
            with open(file_path, "rb") as image_stream:
                features = ['Description', 'Tags']
                result = computervision_client.analyze_image_in_stream(image_stream, visual_features=features)

            # Extract description and tags from Computer Vision API result
            description = result.description.captions[0].text if result.description.captions else "No description available"
            tags = result.tags

            # Perform search using Azure Cognitive Search
            vector_query = Vector(field="imageVector.vector", vector=tags, k=5)  # Using tags as vector query
            query = Query(vector_queries=[vector_query])
            results = search_client.search(query)

            search_results = [{"id": result["id"], "score": result["@search.score"]} for result in results]

            return render_template('results.html', description=description, tags=tags, results=search_results)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
