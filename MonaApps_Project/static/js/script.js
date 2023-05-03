let btnLogin = document.getElementById("login");
let btnSignUp = document.getElementById("signup");
let btnForgot = document.getElementById("forgot");

let signIn = document.querySelector(".signin");
let signUp = document.querySelector(".signup");
let forgot = document.querySelector(".forget");

btnLogin.onclick = function(){
    signIn.classList.add("active");
    signUp.classList.add("inActive");
}

btnSignUp.onclick = function(){
   signIn.classList.remove("active");
   signUp.classList.remove("inActive");
}

btnForgot.onclick = function(){
    signIn.classList.remove("active");
    forgot.classList.add("active");
}

let btnBack = document.getElementById("back");

btnBack.onclick = function(){
    signIn.classList.add("active");
    forgot.classList.remove("active");
}

//confirm password
const passwordField = document.querySelector('input[type="password"]');
const confirmPasswordField = document.querySelector('input[placeholder="Confirm Password"]');

function validatePassword() {
  if (passwordField.value !== confirmPasswordField.value) {
    confirmPasswordField.setCustomValidity("Passwords do not match");
  } else {
    confirmPasswordField.setCustomValidity("");
  }
}

passwordField.addEventListener("change", validatePassword);
confirmPasswordField.addEventListener("keyup", validatePassword);

//password strength checker
const passwordInput = document.querySelector('input[type="password"]');
passwordInput.addEventListener('input', checkPasswordStrength);

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
  passwordInput.style.borderColor = strengthColor[strengthValue];
}


// Get the form element
const form = document.querySelector('form-group');

// Attach an event listener to the form's submit event
form.addEventListener('submit', (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the values of the email and password fields
  const email = document.querySelector('input[type="email"]').value;
  const password = document.querySelector('input[type="password"]').value;
  const checkbox = document.querySelector('input[type="checkbox"]').value;
	
  // Create a new FormData object and add the email and password values to it
  const formData = new FormData();
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
// Get the form element
const form = document.querySelector('form-group');

// Attach an event listener to the form's submit event
form.addEventListener('submit', (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the values of the email and password fields
  const name = document.querySelector('input[type="name"]').value;
  const email = document.querySelector('input[type="email"]').value;
  const password = document.querySelector('input[type="password"]').value;
  const password2 = document.querySelector('input[type="password"]').value;
  const checkbox = document.querySelector('input[type="checkbox"]').value;name
	
  // Create a new FormData object and add the email and password values to it
  const formData = new FormData();
  formData.append('name', name);
  formData.append('email', email);
  formData.append('password', password);
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
