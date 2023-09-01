import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

def register():
    try:
        if authenticator.register_user('Register user', preauthorization=False):
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)
st.button('Don\'t have an account? SignUp!', on_click=register, key='register')


if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")


if authentication_status:
    def home():
        st.title("Home Page")
        st.text_input("Enter your homepage")
    
    def landing():
        st.title("Landing Page")
        st.text_input("Enter your landing id")

    @st.cache_resource(hash_funcs={"_thread.RLock": lambda _: None})
    def init_router():
        return stx.Router({"/home": home, "/landing": landing})
    
    router = init_router()
    router.show_route_view()
   
    
    authenticator.logout('Logout')



    