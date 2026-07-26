import streamlit as st
from components.sidebar import sidebar
from constants import page_content

def configure():
    st.set_page_config(
         page_title='Money Transfer Fraud Detection',
            page_icon='🚨',
            initial_sidebar_state='expanded'
    ) 

def pages():
    main_page = st.Page("1_main.py", title="Project Overview", icon="📒")
    model_page = st.Page("2_model.py", title="Fraud Detection App", icon="🤖")

    return st.navigation([main_page, model_page])

def projectOverview():
    st.image('assets/scam.jpg', width='stretch')
    st.title('Money Transfer Fraud Detection')

    st.header('Project Overview', divider='green')
    st.markdown(page_content['ProjectOverview_1'])
    col_img1, col_text1 = st.columns([1, 2], vertical_alignment="center")
    with col_img1:
        st.image('assets/Smiski-wallet.jpg', width='stretch', caption='My everyday wallet, whose net worth is about ₱150')
    with col_text1:
        st.markdown(page_content['ProjectOverview_2'])
    col_text2, col_img2 = st.columns([2, 1], vertical_alignment="center")
    with col_img2:
        st.image('assets/bank-transfer.jpg', width='stretch', caption='Ate QR nalang po plz')
    with col_text2:
        st.markdown(page_content['ProjectOverview_3'])
    st.markdown(page_content['projectOverview_4'])

def problemStatement():
    st.header('Problem Statement',  divider='green')

def content():
    projectOverview()
    problemStatement()
    

if __name__ == '__main__':
    configure()
    
    main_page = st.Page(content, title="Project Overview", icon="📒", default=True)
    model_page = st.Page("2_model.py", title="Fraud Detection App", icon="🤖")

    pg = st.navigation([main_page, model_page])

    sidebar()
    pg.run()