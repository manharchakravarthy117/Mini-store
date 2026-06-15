# app.py
# MiniStore - Demo E-Commerce Website using Streamlit

import streamlit as st

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS STYLING
# ---------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }

    .hero {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        padding: 40px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 1.1rem;
    }

    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        min-height: 260px;
    }

    .product-name {
        font-size: 1.2rem;
        font-weight: bold;
        color: #111827;
    }

    .product-category {
        color: #6b7280;
        font-size: 0.9rem;
    }

    .product-price {
        color: #16a34a;
        font-size: 1.3rem;
        font-weight: bold;
        margin-top: 10px;
    }

    .section-title {
        font-size: 2rem;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 20px;
        color: #1f2937;
    }

    .footer {
        text-align: center;
        color: gray;
        padding: 20px;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SAMPLE PRODUCT DATA
# ---------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 79.99,
        "category": "Electronics",
        "description": "Premium noise-cancelling wireless headphones with 30-hour battery life."
    },
    {
        "name": "Smart Watch",
        "price": 149.99,
        "category": "Electronics",
        "description": "Track fitness, heart rate, sleep, and notifications in style."
    },
    {
        "name": "Running Shoes",
        "price": 89.99,
        "category": "Fashion",
        "description": "Lightweight running shoes designed for comfort and performance."
    },
    {
        "name": "Leather Backpack",
        "price": 59.99,
        "category": "Fashion",
        "description": "Elegant and durable backpack suitable for work and travel."
    },
    {
        "name": "Coffee Maker",
        "price": 99.99,
        "category": "Home",
        "description": "Automatic coffee maker with programmable brewing settings."
    },
    {
        "name": "Desk Lamp",
        "price": 29.99,
        "category": "Home",
        "description": "Modern LED desk lamp with adjustable brightness levels."
    }
]

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

# Product Categories
categories = ["All"] + sorted(list(set(p["category"] for p in products)))

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

# Shopping Cart Summary
st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Shopping Cart")

cart_items = 3
cart_total = 239.97

st.sidebar.write(f"Items: **{cart_items}**")
st.sidebar.write(f"Total: **${cart_total:.2f}**")

st.sidebar.button("Checkout")

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>MiniStore</h1>
    <p>Your one-stop destination for quality products at amazing prices.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# WELCOME SECTION
# ---------------------------------------------------
st.markdown("""
### Welcome to MiniStore

Discover premium products across electronics, fashion, and home essentials.
Shop smarter with our carefully curated collection of top-rated items.
""")

# ---------------------------------------------------
# FILTER PRODUCTS
# ---------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product for product in products
        if product["category"] == selected_category
    ]

# ---------------------------------------------------
# FEATURED PRODUCTS SECTION
# ---------------------------------------------------
st.markdown(
    '<div class="section-title">Featured Products</div>',
    unsafe_allow_html=True
)

# Display products in a responsive grid
cols_per_row = 3

for i in range(0, len(filtered_products), cols_per_row):
    cols = st.columns(cols_per_row)

    for col, product in zip(cols, filtered_products[i:i+cols_per_row]):

        with col:
            st.markdown(f"""
            <div class="product-card">
                <div class="product-category">
                    {product['category']}
                </div>

                <div class="product-name">
                    {product['name']}
                </div>

                <p>{product['description']}</p>

                <div class="product-price">
                    ${product['price']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.button(
                f"Add to Cart",
                key=product["name"]
            )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("""
<div class="footer">
    © 2025 MiniStore | Demo E-Commerce Website built with Streamlit
</div>
""", unsafe_allow_html=True)