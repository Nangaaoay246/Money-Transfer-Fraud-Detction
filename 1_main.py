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

def projectOverview():
    st.title('Money Transfer Fraud Detection - Project Overview')

if __name__ == '__main__':
    configure()
    
    main_page = st.Page(projectOverview, title="Project Overview", icon="📒", default=True)
    model_page = st.Page("2_model.py", title="Fraud Detection App", icon="🤖")

    pg = st.navigation([main_page, model_page])

    sidebar()
    pg.run()