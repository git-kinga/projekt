document.addEventListener('DOMContentLoaded', function () {
  const loginDiv = document.getElementById('login');
  const forgetDiv = document.getElementById('forget');
  const forgotLink = document.getElementById('forgot');
  const backLink = document.getElementById('back');

  forgotLink.addEventListener('click', function (event) {
    event.preventDefault();
    loginDiv.style.display = 'none';
    forgetDiv.style.display = 'block';
  });

  backLink.addEventListener('click', function (event) {
    event.preventDefault();
    loginDiv.style.display = 'block';
    forgetDiv.style.display = 'none';
  });
});

//confirm password
const passwordField = document.querySelector('input[type="password"]');
const confirmPasswordField = document.querySelector('input[placeholder="Confirm Password"]');

if (passwordField && confirmPasswordField) {
  function validatePassword() {
    if (passwordField.value !== confirmPasswordField.value) {
      confirmPasswordField.setCustomValidity("Passwords do not match");
    } else {
      confirmPasswordField.setCustomValidity("");
    }
  }

  passwordField.addEventListener("change", validatePassword);
  confirmPasswordField.addEventListener("keyup", validatePassword);
}

//password strength checker
const passwordInput = document.querySelector('input[type="password"]');
if (passwordInput) {
  passwordInput.addEventListener('input', checkPasswordStrength);
}

function checkPasswordStrength() {
  const password = passwordInput.value;
  const strengthBadge = document.querySelector('.password-strength');
  const strengthColor = {
    weak: '#dc3545',
    medium: '#ffc107',
    strong: '#28a745'
  }
  const strengthText = {
    weak: 'Weak',
    medium: 'Medium',
    strong: 'Strong'
  }

  if (strengthBadge) {
    // Check password strength
    let strengthValue = 'weak';
    if (password.length >= 8 && /[a-z]/.test(password) && /[A-Z]/.test(password) && /\d/.test(password) && /\W/.test(password)) {
      strengthValue = 'strong';
    } else if (password.length >= 8) {
      strengthValue = 'medium';
    }

    // Update strength badge
    strengthBadge.textContent = strengthText[strengthValue];
    strengthBadge.style.backgroundColor = strengthColor[strengthValue];
    if (passwordInput.style) {
      passwordInput.style.borderColor = strengthColor[strengthValue];
    }
  }
}

///toggle password
let eyeicon = document.getElementById("eyeicon");
let sineyeicon = document.getElementById("sineyeicon");
let coneyeicon = document.getElementById("coneyeicon");
let password = document.getElementById("password");
let conpassword = document.getElementById("conpassword");
let signinpassword = document.getElementById("signinpassword");

if (eyeicon && password) {
  eyeicon.onclick = function() {
    if (password.type === "password") {
      password.type = "text";
      eyeicon.src = "../static/images/eye-open.png";
    } else {
      password.type = "password";
      eyeicon.src = "../static/images/eye-close.png";
    }
  };
}

if (coneyeicon && conpassword) {
  coneyeicon.onclick = function() {
    if (conpassword.type === "password") {
      conpassword.type = "text";
      coneyeicon.src = "../static/images/eye-open.png";
    } else {
    conpassword.type = "password";
    coneyeicon.src = "../static/images/eye-close.png";
    }
    };
    }
if (sineyeicon && signinpassword) {
    sineyeicon.onclick = function() {
    if (signinpassword.type === "password") {
    signinpassword.type = "text";
    sineyeicon.src = "../static/images/eye-open.png";
    } else {
    signinpassword.type = "password";
    sineyeicon.src = "../static/images/eye-close.png";
    }
    };
    }
    
    // Get the form element
    const form = document.querySelector('form');
    
    // Attach an event listener to the form's submit event
    if (form) {
    form.addEventListener('submit', (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();
// Get the values of the email and password fields
const name = document.querySelector('input[type="text"]').value;
const email = document.querySelector('input[type="email"]').value;
const password = document.querySelector('input[type="password"]').value;
const checkbox = document.querySelector('input[type="checkbox"]').checked;

// Create a new FormData object and add the email and password values to it
const formData = new FormData();
formData.append('text', name);
formData.append('email', email);
formData.append('password', password);
formData.append('checkbox', checkbox);

// Send a POST request to the server with the form data
fetch('/login', {
  method: 'POST',
  body: formData
})
.then(response => {
  // Handle the response from the server
  console.log(response);
})
.catch(error => {
  // Handle any errors that occur during the fetch request
  console.error(error);
});
});
}