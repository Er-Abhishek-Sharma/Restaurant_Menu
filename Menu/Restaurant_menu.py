import streamlit as st
import os

# Menu dictionary with correct image paths
menu = {
    'Pizza': {"price": 319, "image": "Imaages\Pizza.jpg"},
    'Pasta': {"price": 279, "image": "Imaages\Pasta.jpg"},
    'Burger': {"price": 249, "image": "Imaages\Burger.jpg"},
    'Salad': {"price": 299, "image": "Imaages\Fresh Salad.jpg"},
    'Coffee': {"price": 299, "image": "Imaages\Cappuccino.jpg"},
}

# Page config
st.set_page_config(page_title="🍽️ Python Restaurant", page_icon="🍴", layout="wide")
st.title("🍽️ Welcome to Python Restaurant")

# Initialize session state
if 'order_total' not in st.session_state:
    st.session_state.order_total = 0

if 'ordered_items' not in st.session_state:
    st.session_state.ordered_items = []

st.subheader("📋 Menu")

# Create columns
cols = st.columns(len(menu))

# Display menu
for idx, (item, info) in enumerate(menu.items()):
    with cols[idx]:

        # Check if image exists
        if os.path.exists(info['image']):
            st.image(info['image'], use_container_width=True)
        else:
            st.warning(f"Image not found")

        st.write(f"### {item}")
        st.write(f"💰 Rs {info['price']}")

        if st.button(f"Add {item}", key=item):
            st.session_state.order_total += info['price']
            st.session_state.ordered_items.append(item)
            st.success(f"{item} added!")

st.markdown("---")

# Show current order
if st.session_state.ordered_items:
    st.subheader("🛒 Your Order")

    for i, item in enumerate(st.session_state.ordered_items, start=1):
        st.write(f"{i}. {item} - Rs {menu[item]['price']}")

    st.write(f"## 💵 Total: Rs {st.session_state.order_total}")

    if st.button("✅ Finish Order"):
        st.success(f"Order complete! Pay Rs {st.session_state.order_total}")

        # Reset order
        st.session_state.order_total = 0
        st.session_state.ordered_items = []

else:
    st.info("Select items to start your order 🍔")