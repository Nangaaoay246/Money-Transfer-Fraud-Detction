import streamlit as st
from components.sidebar import sidebar

def configure():
    st.set_page_config(
         page_title='Money Transfer Fraud Detection',
            page_icon='🚨',
            layout='wide',
            initial_sidebar_state='expanded'
    ) 

def pages():
    main_page = st.Page("1_main.py", title="Project Overview", icon="📒")
    model_page = st.Page("2_model.py", title="Fraud Detection App", icon="🤖")

    return st.navigation([main_page, model_page])
    

if __name__ == '__main__':

    configure()
    sidebar()