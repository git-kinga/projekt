const logregBox = document.querySelector('.logreg-box');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');

// To toggle between login and register
registerLink.addEventListener('click', () => {
    logregBox.classList.add('active');
});

loginLink.addEventListener('click', () => {
    logregBox.classList.remove('active');
});

document.getElementById("signin-btn").addEventListener("click", signIn);

function signIn() {
  // Get the values of the email and password fields
  var email = document.getElementById("floatingInput").value;
  var password = document.getElementById("floatingPassword").value;

  // Create an object with the email and password
  var credentials = {
    email: email,
    password: password
  };

  // Send a POST request with the credentials in JSON format
  fetch('/api/signin', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })
  .then(response => {
    // Handle the response from the server
    // For example, you can redirect the user to another page
    window.location.href = '/dashboard';
  })
  .catch(error => {
    // Handle the error
    console.error('Error:', error);
  });
}