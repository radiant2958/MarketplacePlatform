document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('registerForm'); // Убедитесь, что у формы есть этот ID
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch(form.action, { // Убедитесь, что у формы указан правильный action
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Функция getCookie должна извлекать CSRF-токен
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'ok') {
                window.location.href = data.redirect_url; // Перенаправление на другую страницу
            } else {
                const errorsContainer = document.getElementById('formErrors');
                errorsContainer.innerHTML = ''; // Очистка предыдущих ошибок
                data.errors.forEach(error => {
                    const errorElement = document.createElement('div');
                    errorElement.textContent = error.message;
                    errorsContainer.appendChild(errorElement);
                });
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

