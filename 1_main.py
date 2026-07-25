import streamlit as st
from components.sidebar import sidebar

def configure():
    st.set_page_config(
         page_title='Money Transfer Fraud Detection',
            page_icon='🚨',
            layout='wide',
            initial_sidebar_state='expanded'
    ) 

def load_css():
    st.markdown("""
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """, unsafe_allow_html=True)

    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
    )

if __name__ == '__main__':

    configure()
    #load_css()
    sidebar()