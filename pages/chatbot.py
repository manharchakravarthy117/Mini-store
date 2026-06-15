```python
import streamlit as st
from openai import OpenAI

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬",
    layout="wide"
)

st.title("💬 MiniStore Support Assistant")
st.caption("Ask questions about products, orders, delivery, returns, refunds, and payments.")

# --------------------------------------------------
# OPENAI CLIENT
# --------------------------------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# --------------------------------------------------
# PRODUCT CATALOG
# --------------------------------------------------
PRODUCT_CATALOG = """
MiniStore Product Catalog

1. Wireless Headphones
   Price: $79.99
   Category: Electronics
   Description:
   Premium noise-cancelling wireless headphones with 30-hour battery life.

2. Smart Watch
   Price: $149.99
   Category: Electronics
   Description:
   Track fitness, heart rate, sleep, and notifications.

3. Running Shoes
   Price: $89.99
   Category: Fashion
   Description:
   Lightweight running shoes designed for comfort and performance.

4. Leather Backpack
   Price: $59.99
   Category: Fashion
   Description:
   Durable and stylish backpack for work and travel.

5. Coffee Maker
   Price: $99.99
   Category: Home
   Description:
   Automatic coffee maker with programmable brewing.

6. Desk Lamp
   Price: $29.99
   Category: Home
   Description:
   Modern LED lamp with adjustable brightness.
"""

# --------------------------------------------------
# SYSTEM PROMPT
# --------------------------------------------------
SYSTEM_PROMPT = f"""
You are the official customer support assistant for MiniStore.

Your job is to help customers with:

- Products
- Product recommendations
- Orders
- Delivery and shipping
- Refunds
- Returns
- Payment methods
- Order status
- Store policies

Store Product Information:

{PRODUCT_CATALOG}

Rules:

1. Only answer questions related to MiniStore.
2. Use the product catalog when answering product questions.
3. If users ask unrelated questions such as:
   - programming
   - math
   - history
   - politics
   - general knowledge
   - coding
   politely redirect them back to MiniStore support topics.
4. Never pretend to know information not provided.
5. Be professional, friendly, and concise.
6. If a user asks about an order number, explain that this is a demo store and no real order lookup exists.
"""

# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------
user_prompt = st.chat_input(
    "Ask about products, shipping, refunds, returns, or payments..."
)

if user_prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Build conversation
    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    conversation.extend(st.session_state.messages)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=conversation,
                temperature=0.3
            )

            assistant_reply = response.choices[0].message.content

            st.markdown(assistant_reply)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:

    st.header("Support Topics")

    st.markdown("""
    - Products
    - Orders
    - Delivery
    - Returns
    - Refunds
    - Payments
    """)

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
```

