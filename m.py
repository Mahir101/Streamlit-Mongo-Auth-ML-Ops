import streamlit as st

def show_login():
    st.title("Login")
    # Add login page content here
    if st.button("Login"):
        # Perform login logic here
        st.session_state.logged_in = True

def show_sidebar():
    st.sidebar.title("Navigation")
    # Add sidebar content here

def show_page1():
    st.title("Page 1")
    # Add content for Page 1 here

def main():
    if not st.session_state.get("logged_in"):
        show_login()
    else:
        show_sidebar()
        show_page1()

if __name__ == "__main__":
    main()