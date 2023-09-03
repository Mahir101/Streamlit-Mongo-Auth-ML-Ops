import streamlit as st
from streamlit_login_auth_mongo.widgets import __login__
import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

__login__obj = __login__(auth_token = "courier_auth_token",
                    company_name = "Shims",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()
username = __login__obj.get_username()

if LOGGED_IN == True:

   st.markdown("Your Streamlit Application Begins here!")
   st.markdown(st.session_state)
   st.write(username)
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




    
                                      
