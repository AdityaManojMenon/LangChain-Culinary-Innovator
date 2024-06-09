import streamlit as st
import helper_function

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a cuisine",("Mexican", "Italian", "Chinese", "Indian", "Japanese", "French", "Thai", "Greek", "Spanish", "American"))


if cuisine:
    response = helper_function.generate(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items = response["menu_items"].strip().split(",")
    st.write("Menu Items : ")

    for item in menu_items:
        st.write(item)