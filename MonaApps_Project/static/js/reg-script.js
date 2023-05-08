// Get the form element
const form = document.querySelector('form');

// Attach an event listener to the form's submit event
form.addEventListener('submit', (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the values of the email and password fields
  const name = document.querySelector('input[type="name"]').value;
  const email = document.querySelector('input[type="email"]').value;
  const password = document.querySelector('input[type="password"]').value;
  const password2 = document.querySelector('input[type="password2"]').value;
  const checkbox = document.querySelector('input[type="checkbox"]').value;name
	
  // Create a new FormData object and add the email and password values to it
  const formData = new FormData();
  formData.append('name', name);
  formData.append('email', email);
  formData.append('password', password);
  formData.append('password2', password2);
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