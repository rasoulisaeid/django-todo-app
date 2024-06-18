document.addEventListener('DOMContentLoaded', function() {
    const getCookie = (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    const csrftoken = getCookie('csrftoken');

    const checkboxes = document.querySelectorAll('.task-checkbox');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const taskId = this.getAttribute('data-task-id');
            const isChecked = this.checked;

            fetch(`/todo/tasks/${taskId}/update/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ status: isChecked })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('Task status updated successfully:', data);
                // Optionally handle the JSON response data here

                // Redirect to success_url after updating status (assuming the task was updated successfully)
                window.location.href = '/todo/tasks/'; // Replace with your actual success_url
            })
            .catch(error => {
                console.error('Error updating task status:', error);
            });
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const getCookie = (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    const csrftoken = getCookie('csrftoken');

    // Add event listener for contenteditable fields
    const editableFields = document.querySelectorAll('.editable');
    editableFields.forEach(field => {
        field.addEventListener('blur', function() {
            const taskId = this.getAttribute('data-task-id');
            const newTitle = this.textContent.trim(); // Get edited text

            fetch(`/todo/tasks/${taskId}/update/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ title: newTitle })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('Task title updated successfully:', data);
                // Optionally handle the JSON response data here
            })
            .catch(error => {
                console.error('Error updating task title:', error);
            });
        });
    });
});
