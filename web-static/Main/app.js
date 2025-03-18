// Simulate storing user data in localStorage for simplicity
const users = JSON.parse(localStorage.getItem("users")) || [];

document
  .getElementById("sign-up-form")
  ?.addEventListener("submit", function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const newUser = { username, email, password };
    users.push(newUser);
    localStorage.setItem("users", JSON.stringify(users));

    alert("Account created successfully!");
    window.location.href = "login.html"; // Redirect to login page
  });

document.getElementById("login-form")?.addEventListener("submit", function (e) {
  e.preventDefault();

  const email = document.getElementById("login-email").value;
  const password = document.getElementById("login-password").value;

  const user = users.find((u) => u.email === email && u.password === password);

  if (user) {
    localStorage.setItem("currentUser", JSON.stringify(user)); // Store the logged-in user
    window.location.href = "index.html"; // Redirect to main page (or dashboard)
  } else {
    alert("Invalid credentials");
  }
});
