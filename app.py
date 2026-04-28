import streamlit as st

st.set_page_config(page_title = "My First App")

st.title("Streamlit Demo App")
st.header("User Input Section")

st.write("Please provide your details below:")

age = st.number_input("Enter your age:", min_value = 0, max_value = 120, value = 25) 
# no need try-except because only number is allowed
# default value = 25

color = st.selectbox("Choose your favorite color:", ["Red", "Blue", "Green"])
# "selectbox" = pass in different options im box 

name = st.text_input("Enter your name:", placeholder="Type your name here")

if st.button("Submit"):
    st.success(f"Thank you {name}! Age: {age}, Favorite Color: {color}")
