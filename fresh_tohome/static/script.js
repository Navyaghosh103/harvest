const bar = document.getElementById('bar');
const close = document.getElementById('close');
const nav = document.getElementById('navbar');

if (bar) {
  bar.addEventListener('click', () => {
    nav.classList.add('active');
  })
}
if (close) {
  close.addEventListener('click', () => {
    nav.classList.remove('active');
  })
}

document.addEventListener("DOMContentLoaded", function() {
    // Get the sign-in button
var signinBtn = document.getElementById("signin-btn");

    // Add click event listener to the sign-in button
signinBtn.addEventListener("click", function() {
        // Redirect to the sign-in page when the button is clicked
window.location.href = "sign_in.html";
    });
});

