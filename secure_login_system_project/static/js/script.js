document.addEventListener('DOMContentLoaded', () => {
    const password1 = document.getElementById('password1');
    const password2 = document.getElementById('password2');

    if (password1 && password2) {
        const feedback = document.createElement('div');
        feedback.className = 'small mt-2';
        password2.parentNode.appendChild(feedback);

        const validatePasswords = () => {
            if (!password2.value) {
                feedback.textContent = '';
                return;
            }

            if (password1.value === password2.value) {
                feedback.textContent = 'Passwords match.';
                feedback.className = 'small mt-2 text-success';
            } else {
                feedback.textContent = 'Passwords do not match.';
                feedback.className = 'small mt-2 text-danger';
            }
        };

        password1.addEventListener('input', validatePasswords);
        password2.addEventListener('input', validatePasswords);
    }
});
