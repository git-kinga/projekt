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
//phone number only
var phoneInput = document.getElementById('phone');
phoneInput.addEventListener('keydown', function(event) {
  if (isNaN(Number(event.key))) {
    event.preventDefault();
  }
});

// password requierments for register
const passwordInput = document.getElementById('password-input');
const passwordError = document.querySelector('.password-error');
const passwordErrorMessage = document.querySelector('.password-error .error-message');
const passwordErrorTooltip = document.querySelector('.password-error .tooltip');
const passwordErrorLength = document.querySelector('.password-error .length');
const passwordErrorUppercase = document.querySelector('.password-error .uppercase');
const passwordErrorLowercase = document.querySelector('.password-error .lowercase');
const passwordErrorNumber = document.querySelector('.password-error .number');

passwordInput.addEventListener('input', function() {
  const password = passwordInput.value;
  const isValidLength = password.length >= 8;
  const hasUppercase = /[A-Z]/.test(password);
  const hasLowercase = /[a-z]/.test(password);
  const hasNumber = /\d/.test(password);

  if (!isValidLength || !hasUppercase || !hasLowercase || !hasNumber) {
    passwordError.classList.add('active');

    passwordErrorLength.classList.toggle('done', isValidLength);
    passwordErrorUppercase.classList.toggle('done', hasUppercase);
    passwordErrorLowercase.classList.toggle('done', hasLowercase);
    passwordErrorNumber.classList.toggle('done', hasNumber);

    passwordErrorTooltip.style.display = 'inline';
  } else {
    passwordError.classList.remove('active');
    passwordErrorTooltip.style.display = 'none';
  }
});

