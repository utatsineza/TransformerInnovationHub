document.addEventListener("DOMContentLoaded", function () {
    const cartItems = document.querySelectorAll(".cart-item");

    cartItems.forEach((item) => {
        const decreaseBtn = item.querySelector(".decrease");
        const increaseBtn = item.querySelector(".increase");
        const quantityInput = item.querySelector(".quantity-input");
        const itemPrice = parseFloat(item.querySelector(".item-price").innerText);
        const totalPriceElement = item.querySelector(".total-price");
        const removeBtn = item.querySelector(".remove-item");

        function updateTotal() {
            let quantity = parseInt(quantityInput.value);
            if (isNaN(quantity) || quantity < 1) quantity = 1;
            quantityInput.value = quantity;
            totalPriceElement.innerText = `$${(itemPrice * quantity).toFixed(2)}`;
            calculateCartTotal();
        }

        decreaseBtn.addEventListener("click", () => {
            quantityInput.value = Math.max(1, parseInt(quantityInput.value) - 1);
            updateTotal();
        });

        increaseBtn.addEventListener("click", () => {
            quantityInput.value = parseInt(quantityInput.value) + 1;
            updateTotal();
        });

        removeBtn.addEventListener("click", () => {
            item.remove();
            calculateCartTotal();
        });

        quantityInput.addEventListener("input", updateTotal);
    });

    function calculateCartTotal() {
        let subtotal = 0;
        document.querySelectorAll(".total-price").forEach((priceElement) => {
            subtotal += parseFloat(priceElement.innerText.replace("$", ""));
        });
        const tax = subtotal * 0.05;
        const total = subtotal + tax;

        document.getElementById("subtotal").innerText = subtotal.toFixed(2);
        document.getElementById("tax").innerText = tax.toFixed(2);
        document.getElementById("total").innerText = total.toFixed(2);
    }

    calculateCartTotal();
});