// JavaScript for client-side interactions

// Example of adding event listener for form submission
document.addEventListener('DOMContentLoaded', function() {
    let form = document.querySelector('#upload-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            let fileInput = document.querySelector('input[type="file"]');
            if (!fileInput.value) {
                event.preventDefault();
                alert('Please select a file.');
            }
        });
    }
});
