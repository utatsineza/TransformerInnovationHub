// Store products in an array
const products = [
  { id: 1, name: "Light Glass", price: 50, image: "../Main/Images/glass.jpg" },
  { id: 2, name: "Product 2", price: 100, image: "../Main/Images/item1.jpg" },
  { id: 3, name: "Product 3", price: 30, image: "../Main/Images/item2.jpg" },
  { id: 4, name: "Product 4", price: 80, image: "../Main/Images/item3.jpg" },
  { id: 5, name: "Product 5", price: 120, image: "../Main/Images/item4.jpg" },
  { id: 6, name: "Product 6", price: 60, image: "../Main/Images/item5.jpg" },
  { id: 5, name: "Product 5", price: 120, image: "../Main/Images/item4.jpg" },
  { id: 6, name: "Product 6", price: 60, image: "../Main/Images/item5.jpg" },
  // Add more products as needed
];

// DOM elements
const cartIcon = document.getElementById("cart-btn");
const productContainer = document.getElementById("product-container");
const itemCountSelect = document.getElementById("item-count");
const sortBySelect = document.getElementById("sort-by");
const paginationContainer = document.querySelector(".pagination");

let currentPage = 1;
const productsPerPage = 4;

// Function to render products to the page
function renderProducts(productsToRender) {
  productContainer.innerHTML = ""; // Clear previous products

  productsToRender.forEach((product) => {
    const productElement = document.createElement("div");
    productElement.classList.add("product");
    productElement.setAttribute("data-product-id", product.id); // Add product ID

    productElement.innerHTML = `
          <img src="${product.image}" alt="${product.name}">
          <h3>${product.name}</h3>
          <p>$${product.price}</p>
          <div class="product-actions">
            <i class="fas fa-cart-plus" title="Add to Cart"></i>
          </div>
        `;

    // Add event listener for adding to cart
    productElement
      .querySelector(".fa-cart-plus")
      .addEventListener("click", () => {
        addToCart(product.id);
        window.location.href = `productpage.html?id=${product.id}`; // Redirect to productpage.html with product ID in the URL
      });

    productContainer.appendChild(productElement);
  });
}

// Function to generate pagination buttons
function generatePaginationButtons(totalProducts) {
  paginationContainer.innerHTML = "";
  const totalPages = Math.ceil(totalProducts / productsPerPage);

  for (let i = 1; i <= totalPages; i++) {
    const button = document.createElement("button");
    button.textContent = i;
    button.addEventListener("click", () => goToPage(i));
    paginationContainer.appendChild(button);
  }
}

// Function to handle sorting
function sortProducts(products, criteria) {
  if (criteria === "price-low") {
    return products.sort((a, b) => a.price - b.price);
  } else if (criteria === "price-high") {
    return products.sort((a, b) => b.price - a.price);
  }
  return products;
}

// Function to handle page change
function goToPage(pageNumber) {
  currentPage = pageNumber;
  const startIndex = (currentPage - 1) * productsPerPage;
  const endIndex = currentPage * productsPerPage;
  const productsToRender = products.slice(startIndex, endIndex);
  renderProducts(productsToRender);
}

// Function to handle adding a product to the cart
function addToCart(productId) {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const product = products.find((p) => p.id === productId);
  const existingProductIndex = cart.findIndex((item) => item.id === productId);

  if (existingProductIndex > -1) {
    cart[existingProductIndex].quantity += 1; // Increment quantity if already in cart
  } else {
    cart.push({ ...product, quantity: 1 }); // Add new product to the cart
  }

  localStorage.setItem("cart", JSON.stringify(cart));
}

// Event listeners for sort and filter changes
sortBySelect.addEventListener("change", () => {
  const sortedProducts = sortProducts(products, sortBySelect.value);
  renderProducts(sortedProducts);
  generatePaginationButtons(sortedProducts.length);
});

// Event listener for items per page selection
itemCountSelect.addEventListener("change", () => {
  const itemsPerPage = parseInt(itemCountSelect.value);
  const productsToRender = products.slice(0, itemsPerPage);
  renderProducts(productsToRender);
});

// Initial render
renderProducts(products.slice(0, productsPerPage));
generatePaginationButtons(products.length);

// Event listener for the cart icon
cartIcon.addEventListener("click", () => {
  window.location.href = "productpage.html"; // Redirect to productpage.html when the cart icon is clicked
});
