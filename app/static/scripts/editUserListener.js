function showField(field) {
    var emailField = document.getElementById('email-field');
    var passwordField = document.getElementById('password-field');
    var accessField = document.getElementById('access-field');

    // Hide all fields
    emailField.style.display = 'none';
    passwordField.style.display = 'none';
    accessField.style.display = 'none';

    // Show the selected field
    if (field === 'email') {
        console.log("works")
        emailField.style.display = 'block';
    } else if (field === 'password') {
        console.log("works")
        passwordField.style.display = 'block';
    } else if (field === 'access') {
        console.log("works")
        accessField.style.display = 'block';
    }
}