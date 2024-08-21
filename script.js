// Mock products data (could be fetched from an API in a real-world application)
const products = [
    {
        id: 1,
        name: 'Uppada Jamdani',
        description: 'Intricately weaved Jamdani Motifs',
        price: 6000,
        image: "D:/vscode/e-commerce/jamdani.jpg"
    },
    {
        id: 2,
        name: 'Kalamkari Silk Saree',
        description: 'Premium silk fabric, perfect for luxury garments.',
        price: 8000,
        image: "D:/vscode/e-commerce/kalamkari silk.jpg"
    },
    {
        id: 3,
        name: 'Ramdani Silk',
        description: 'Combination of traditional artistry with elegance',
        price: 5500,
        image: "D:/vscode/e-commerce/jamdani2.jpg"
    },
    {
        id: 4,
        name: 'Ikkat Design',
        description: 'Pure Uppada Cotton Saree',
        price: 4300,
        image: "D:/vscode/e-commerce/ikat cotton saree.jpg"
    }
];

// Shopping cart array
let cart = [];

// Load products and display them
function loadProducts() {
    const productList = document.getElementById('product-list');
    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.className = 'product';
        productElement.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h2>${product.name}</h2>
            <p>${product.description}</p>
            <p><strong>₹${product.price}</strong></p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productList.appendChild(productElement);
    });
}

// Add product to cart
function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    const cartItem = cart.find(item => item.id === productId);

    if (cartItem) {
        cartItem.quantity += 1;
    } else {
        cart.push({ ...product, quantity: 1 });
    }

    updateCartCount();
    alert(`${product.name} added to cart`);
}

// Update cart count in the navigation
function updateCartCount() {
    const cartCount = document.getElementById('cart-count');
    cartCount.innerText = cart.reduce((total, item) => total + item.quantity, 0);
}

// Initialize
loadProducts();
