function scrollToSection(id) {
  document.getElementById(id).scrollIntoView({
    behavior: 'smooth'
  });
}

async function sendContactData(event) {

  const product_data = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    message: document.getElementById("message").value,
  };

  const response = await fetch("/contact", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(product_data)
  });

  // const result = await response.json();
  // console.log(result);

}