const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;
    const user = ""

    if (username === "user" && password === "123456") {
        alert("You have successfully logged in.");
        location.href = "http://127.0.0.1:5500/index.html";
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})