
document.getElementById("signin-btn").addEventListener("click", signIn);

function signIn() {
  // Get the values of the username and password fields
  var username = document.getElementById("floatingInput").value;
  var password = document.getElementById("floatingPassword").value;

  // Create an object with the username and password
  var credentials = {
    username: username,
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