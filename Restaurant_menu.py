import streamlit as st

# Menu dictionary with optional images
menu = {
    'Pizza': {"price": 319, "image": "Imaages\Pizza.jpg"},
    'Pasta': {"price": 279, "image": "Imaages\Pasta.jpg"},
    'Burger': {"price": 249, "image": "Imaages\Burger.jpg"},
    'Salad': {"price": 299, "image": "Imaages\Fresh Salad.jpg"},
    'Coffee': {"price": 299, "image": "Imaages\Cappuccino.jpg"},
}

st.set_page_config(page_title="🍽️ Python Restaurant", page_icon="🍴", layout="wide")
st.title("🍽️ Welcome to Python Restaurant")

# Initialize session state
if 'order_total' not in st.session_state:
    st.session_state.order_total = 0
if 'ordered_items' not in st.session_state:
    st.session_state.ordered_items = []

st.subheader("Menu")

# Display menu items in columns
cols = st.columns(len(menu))
for idx, (item, info) in enumerate(menu.items()):
    with cols[idx]:
        st.image(info['image'], width="stretch")
        st.write(f"**{item}**")
        st.write(f"Rs {info['price']}")
        if st.button(f"Add {item}", key=item):
            st.session_state.order_total += info['price']
            st.session_state.ordered_items.append(item)
            st.success(f"{item} added to your order!")

st.markdown("---")

# Show current order
if st.session_state.ordered_items:
    st.subheader("🛒 Your Current Order")
    for i, item in enumerate(st.session_state.ordered_items, start=1):
        st.write(f"{i}. {item} - Rs {menu[item]['price']}")
    st.write(f"**Total: Rs {st.session_state.order_total}**")

    if st.button("✅ Finish Order"):
        st.success(f"Your order is complete! Total amount to pay: Rs {st.session_state.order_total}")
        # Reset order
        st.session_state.order_total = 0
        st.session_state.ordered_items = []
else:
    st.info("Select items from the menu to start your order.")