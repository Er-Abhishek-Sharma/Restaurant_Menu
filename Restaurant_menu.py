import streamlit as st

# Menu with IMAGE URLs (Google / internet links)
menu = {
    'Pizza': {
        "price": 319,
        "image": "https://i.pinimg.com/736x/df/11/13/df11137f7ea78702571c15bccc691eb6.jpg"
    },
    'Pasta': {
        "price": 279,
        "image": "https://i.pinimg.com/736x/0e/a1/3e/0ea13e0e7c2afea22b0f6d7301afe04e.jpg"
    },
    'Burger': {
        "price": 249,
        "image": "https://i.pinimg.com/736x/c9/c5/01/c9c5013a47c78dde12d22a8659cdb945.jpg"
    },
    'Salad': {
        "price": 299,
        "image": "https://i.pinimg.com/736x/08/c7/0d/08c70d473888e35bd1c4cd9d1d2983d7.jpg"
    },
    'Coffee': {
        "price": 299,
        "image": "https://i.pinimg.com/736x/f0/65/5f/f0655f2737da76be9b4ac435c65e3d9b.jpg"
    },
}

# Page config
st.set_page_config(page_title="🍽️ Python Restaurant", page_icon="🍴", layout="wide")
st.title("🍽️ Welcome to Python Restaurant")

# Session state
if 'order_total' not in st.session_state:
    st.session_state.order_total = 0

if 'ordered_items' not in st.session_state:
    st.session_state.ordered_items = []

st.subheader("📋 Menu")

# Columns
cols = st.columns(len(menu))

# Display menu
for idx, (item, info) in enumerate(menu.items()):
    with cols[idx]:

        # Directly show image from URL
        st.image(info['image'], use_container_width=True)

        st.write(f"### {item}")
        st.write(f"💰 Rs {info['price']}")

        if st.button(f"Add {item}", key=item):
            st.session_state.order_total += info['price']
            st.session_state.ordered_items.append(item)
            st.success(f"{item} added!")

st.markdown("---")

# Order section
if st.session_state.ordered_items:
    st.subheader("🛒 Your Order")

    for i, item in enumerate(st.session_state.ordered_items, start=1):
        st.write(f"{i}. {item} - Rs {menu[item]['price']}")

    st.write(f"## 💵 Total: Rs {st.session_state.order_total}")

    if st.button("✅ Finish Order"):
        st.success(f"Order complete! Pay Rs {st.session_state.order_total}")
        st.session_state.order_total = 0
        st.session_state.ordered_items = []

else:
    st.info("Select items to start your order 🍔")







# import streamlit as st
# import os

# # Menu dictionary with correct image paths
# menu = {
#     'Pizza': {"price": 319, "image": "Images\Pizza.jpg"},
#     'Pasta': {"price": 279, "image": "Images\Pasta.jpg"},
#     'Burger': {"price": 249, "image": "Images\Burger.jpg"},
#     'Salad': {"price": 299, "image": "Images\Fresh Salad.jpg"},
#     'Coffee': {"price": 299, "image": "Images\Cappuccino.jpg"},
# }

# # Page config
# st.set_page_config(page_title="🍽️ Python Restaurant", page_icon="🍴", layout="wide")
# st.title("🍽️ Welcome to Python Restaurant")

# # Initialize session state
# if 'order_total' not in st.session_state:
#     st.session_state.order_total = 0

# if 'ordered_items' not in st.session_state:
#     st.session_state.ordered_items = []

# st.subheader("📋 Menu")

# # Create columns
# cols = st.columns(len(menu))

# # Display menu
# for idx, (item, info) in enumerate(menu.items()):
#     with cols[idx]:

#         # Check if image exists
#         if os.path.exists(info['image']):
#             st.image(info['image'], use_container_width=True)
#         else:
#             st.warning(f"Image not found")

#         st.write(f"### {item}")
#         st.write(f"💰 Rs {info['price']}")

#         if st.button(f"Add {item}", key=item):
#             st.session_state.order_total += info['price']
#             st.session_state.ordered_items.append(item)
#             st.success(f"{item} added!")

# st.markdown("---")

# # Show current order
# if st.session_state.ordered_items:
#     st.subheader("🛒 Your Order")

#     for i, item in enumerate(st.session_state.ordered_items, start=1):
#         st.write(f"{i}. {item} - Rs {menu[item]['price']}")

#     st.write(f"## 💵 Total: Rs {st.session_state.order_total}")

#     if st.button("✅ Finish Order"):
#         st.success(f"Order complete! Pay Rs {st.session_state.order_total}")

#         # Reset order
#         st.session_state.order_total = 0
#         st.session_state.ordered_items = []

# else:
#     st.info("Select items to start your order 🍔")