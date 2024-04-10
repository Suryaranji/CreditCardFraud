import streamlit as st
from sklearn.ensemble import IsolationForest
import pandas   as pd
import pickle
column_names = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
                    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']
with open('Isolation_Forest_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
def predict(input_values):
    df = pd.DataFrame(columns=column_names)
    # Add input values as a row to the DataFrame
    df.loc[0] = [input_values[col_name] for col_name in column_names]
    y_pred=loaded_model.predict(df)
    return 0 if y_pred==1  else 1
def main():
    st.title('Credit Card Fraud Detection')


    # Define column names

    # Input fields for each feature
    input_values = {}
    for col_name in column_names:
        input_values[col_name] = st.number_input(col_name, value=0.0)

    if st.button('Submit'):
        st.balloons()
        # Call predict function with input values
        prediction = predict(input_values)
        
        # Display prediction result
        st.write('### Prediction Result')
        if prediction == 0:
            st.write("No Fraud Detected")
        else:
            st.write("Fraud Detected")
if __name__ == "__main__":
    main()
