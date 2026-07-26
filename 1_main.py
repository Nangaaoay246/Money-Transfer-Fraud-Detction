import streamlit as st
from components.sidebar import sidebar
from constants import page_content
import pandas as pd

def configure():
    st.set_page_config(
         page_title='FraudWatch: Money Transfer Fraud Detection',
            page_icon='🚨',
            initial_sidebar_state='expanded'
    ) 

def pages():
    main_page = st.Page("1_main.py", title="Project Overview", icon="📒")
    model_page = st.Page("2_model.py", title="Fraud Watch Demo", icon="🤖")

    return st.navigation([main_page, model_page])

def projectOverview():
    st.image('assets/scam.jpg', width='stretch')
    st.title('Money Transfer Fraud Detection')

    st.header('Project Overview', divider='green')
    st.markdown(page_content['ProjectOverview_1'])
    col_img1, col_text1 = st.columns([1, 2], vertical_alignment="center")
    with col_img1:
        st.image('assets/Smiski-wallet.jpg', width='stretch', caption='My everyday wallet. Current balance: ₱150 and one bus ticket.')
    with col_text1:
        st.markdown(page_content['ProjectOverview_2'])
    col_text2, col_img2 = st.columns([2, 1], vertical_alignment="center")
    with col_img2:
        st.image('assets/bank-transfer.jpg', width='stretch', caption="My e-wallet. ₱175 across MariBank and GCash (strategic diversification)")
    with col_text2:
        st.markdown(page_content['ProjectOverview_3'])
    st.markdown(page_content['projectOverview_4'])

def problemStatement():
    st.header('Problem Statement',  divider='green')
    st.markdown(page_content['problemStatement'])

def businessObjective():
    st.header('Business Objective',  divider='green')
    st.markdown(page_content['businessObjective'])

def datasetDescription():
    st.header('Description of Dataset',  divider='green')
    df_head = pd.read_csv('data/dataset_head.csv')
    st.dataframe(df_head)
    st.markdown(page_content['datasetDescription'])

def modelEvaluation():
    st.header('Evaluation Metrics',  divider='green')
    df_comparison = pd.read_csv('data/model_comparison.csv')
    st.dataframe(df_comparison)
    st.markdown(page_content['modelEvaluation_1'])


def results():
    st.header('Training Results',  divider='green')
    df_comparison = pd.read_csv('data/model_comparison.csv')
    st.dataframe(df_comparison)
    
    col_img1, col_text1 = st.columns([1, 2], vertical_alignment="center")
    with col_img1:
            st.image('assets/PRAUC.png', width='stretch')
    with col_text1:
        st.markdown(page_content['modelEvaluation_2'])
    st.markdown(page_content['modelEvaluation_3'])

def content():
    projectOverview()
    problemStatement()
    businessObjective()
    datasetDescription()
    modelEvaluation()
    results()
    

if __name__ == '__main__':
    configure()
    
    main_page = st.Page(content, title="Project Overview", icon="📒", default=True)
    model_page = st.Page("2_model.py", title="Fraud Detection App", icon="🤖")

    pg = st.navigation([main_page, model_page])

    sidebar()
    pg.run()