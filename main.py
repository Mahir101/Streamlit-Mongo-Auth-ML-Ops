import streamlit as st
from pymongo import MongoClient
# import bcrypt
from pages import home, learning, contact
# import authentication


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["trendvision"]  # Replace with your database name
users_collection = db["users"]  # Replace with your collection name

def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state.logged_in:
        show_login()
    else:
        show_sidebar()

# Streamlit login page
def show_login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login", key="login_button"):
        user = users_collection.find_one({"username": username})
        if user and password == user["password"]:
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")

def show_sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Learning Materials", "Contact Me"])

    if page == "Home":
        home.show()
    elif page == "Learning Materials":
        learning.show()
    elif page == "Contact Me":
        contact.show()

if __name__ == "__main__":
    main()
