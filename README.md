# ImageSearchApp

## Overview
This is an advanced web application built using Flask that incorporates Azure Cognitive Services for image analysis and Azure Cognitive Search for search functionalities. It allows users to upload images, perform image analysis using Azure Computer Vision API, and search for images based on tags using Azure Cognitive Search.

## Technology Stack
- **Flask**: Web framework for Python.
- **HTML/CSS/JavaScript**: Frontend for user interface and interactions.
- **Azure Cognitive Services - Computer Vision API**: For image analysis and recognition.
- **Azure Cognitive Search**: For indexing and searching images.


## Steps to Build the Application

### 1. Set Up Virtual Environment and Install Dependencies
Create and activate a virtual environment, then install required packages:
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Azure Setup
Azure Cognitive Services:

Create a Cognitive Services resource in Azure Portal.
Obtain the endpoint and subscription key for the Computer Vision API.
Azure Cognitive Search:

Create a search service in Azure Portal.
Set up an index for your products/images.
3. Flask Routes
/ (Index): Renders the home page (index.html) with a link to upload images.
/upload: Handles the image upload functionality. Checks for valid file types, saves the file, analyzes it using Azure Cognitive Services, and performs a search using Azure Cognitive Search.
4. Error Handling
Uses flash messages to handle errors and notify users if no file is selected or if there's an issue with the upload.

5. Templates
base.html: Base template with common elements (head, navigation).
index.html: Home page template with upload link.
upload.html: Upload page template with file input form.
results.html: Results page template to display image analysis results and search results.
Running the Application
Set Environment Variables
Replace <your-computer-vision-api-key>, <your-computer-vision-api-endpoint>, <your-search-service-name>, and <your-search-service-key> with your actual Azure credentials and endpoints.

Run the Application
Start the Flask application:
```bash
python app.py
```
Access the Application
Open your web browser and go to http://127.0.0.1:5000/ to access the application.

Notes
Ensure your virtual environment (venv) is activated before running the application.
Customize CSS (static/style.css) and JavaScript (static/script.js) files for styling and frontend interactions as needed.
Author
Your Name
Contact Information
License
This project is licensed under the MIT License.


### Tips for Usage:
- **Customization**: Modify HTML templates, CSS styles, and JavaScript scripts (`static/`) to fit specific design and functionality requirements.
- **Security**: Ensure Azure credentials and API keys (`<your-computer-vision-api-key>`, etc.) are kept secure and not hard-coded into public repositories.
- **Documentation**: Update the README with any additional features, troubleshooting steps, or deployment instructions as needed.

This structured `README.md` provides a comprehensive guide for developers to set up, configure, and use the ImageSearchApp Flask application with Azure services effectively. Adjust the details according to your specific project requirements and environment setup.
