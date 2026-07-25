import streamlit as st
import pandas as pd
import joblib

model = joblib.load('pkl/fraud_detection_pipeline.pkl')

st.title('Money Transfer Fraud Detection App')
st.markdown('Please enter the transaction details and use the prediction model')
st.divider()
st.header("Transaction Details")

step = st.number_input(
    'Transaaction Hour (Step)',
    min_value=1, max_value=744, value=1,
    help="1 step = 1 hour of simulated time (744 steps ≈ 31 days)"
)

txn_type = st.selectbox(
    'Transaction Type',
    options=["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"]
)

amount = st.number_input(
    "Transaction amount",
    min_value=0.0, value=0.0
)

oldbalanceOrg = st.number_input(
    'User Balance Before Transaction: ',
    min_value=0.0, value=0.0
)

newBalanceOrig = st.number_input(
    'User Balance After Transaction: ',
    min_value=0.0, value=0.0
)

oldBalanceDest = st.number_input(
    'Receiver Balance Before Transaction: ',
    min_value=0.0, value=0.0
)

newBalanceDest = st.number_input(
    'Receiver Balance After Transaction: ',
    min_value=0.0, value=0.0
)

if st.button('Predict'):
    inputData = pd.DataFrame({
        'step': [step],
        'type': [txn_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newBalanceOrig],
        'oldbalanceDest': [oldBalanceDest],  
        'newbalanceDest': [newBalanceDest]   
    })

    pred = model.predict(inputData)[0]

    isPred = ('Transaction is :green[Legitimate!]' if pred == 0 else 'Transaction is :red[Fraudulent!]')

    st.subheader(f'Prediction: {isPred}')

    if pred == 1:
        st.error("🚨 This transaction is predicted to be :red[fraudulent].")
    else:
        st.success("✅ This transaction is predicted to be :green[legitimate].")

