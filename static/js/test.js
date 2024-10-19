// First, include Froala Editor CSS and JS in your Django admin template
// You can do this in your admin.py file or in a custom admin template

// Add this to your JavaScript file or in a <script> tag
document.addEventListener('DOMContentLoaded', function() {
    // Check if the content textarea exists
    var contentTextarea = document.getElementById('id_content');
    if (contentTextarea) {
        // Load Froala Editor CSS
        var link = document.createElement('link');
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = 'https://cdn.jsdelivr.net/npm/froala-editor@latest/css/froala_editor.pkgd.min.css';
        document.head.appendChild(link);

        // Load Froala Editor JS
        var script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = 'https://cdn.jsdelivr.net/npm/froala-editor@latest/js/froala_editor.pkgd.min.js';
        script.onload = function() {
            // Initialize Froala Editor
            new FroalaEditor('#id_content', {
                toolbarButtons: [
                    'bold', 'italic', 'underline', 'strikeThrough', '|',
                    'paragraphFormat', 'align', 'formatOL', 'formatUL', '|',
                    'insertLink', 'insertImage', 'insertTable', '|',
                    'html'
                ],
                heightMin: 300,
                heightMax: 600,
                // Ensure inserted images are treated as relative URLs
                imageUploadURL: '/your_image_upload_url/',
                imageUploadParams: {
                    csrfmiddlewaretoken: getCookie('csrftoken')
                }
            });
        };
        document.head.appendChild(script);
    }
});

// Helper function to get CSRF token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}