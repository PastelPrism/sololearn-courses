document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("orderForm");

  form.addEventListener("submit", event => {
    event.preventDefault();

    const name  = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const color = document.getElementById("color").value;

    if (!name || !email || !color) {
      alert("Please fill in all fields before submitting.");
      return;
    }

    alert(`Thank you, ${name}! Your pastel ${color} prism is on its way! Hurray!`);
    form.reset();
  });
});