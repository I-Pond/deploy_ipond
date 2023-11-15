import streamlit as st
import pandas as pd
import joblib
from firebase_admin import credentials, db, initialize_app
import firebase_admin

config = {
  "type": "service_account",
  "project_id": "datastreamlit",
  "private_key_id": "c8e713aa8da5e20aa9119294323ae155de2ec330",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDRkicHdKvZKTMX\n+vIP5laavoOQp7+vB12MPLQnVgMoyua9yybhOjvdujqF5scTVN0J23GXo8mYTlGJ\nzyIwgwQkjmrpRwXwP1FSCG4M5x6CV2q+SGVPrQnpC945A16YsZjf2EuCb/DeQsDm\n9sSyJrLzhA2ADh9cbcrfHml5i2w0NDCsG82K1McUE1tZ4PLpM1lVdsS+mkRdRmbC\nFi6IHUfkOsfgQQtc72w0YcBBXM5UmcF0ndnl5gvpb3dV7p7U8gPAuxA1JhTGJuXm\nzzvIWupuHjDXedmJ2fJWyrWmiBQlcog3teC6aV/F0bXCm79ZnKWDGEjdBp+R/Tr+\ncgxK1dqZAgMBAAECggEAB22PmFQucJ+lFdchTAa5IFo7Ec4eTUr8qfcvV/sUmNYr\nPEQmdEJzA4KBp0QVH4ZpILuwUKR/pVg2S+UFdFR6eby6BZtstpWZ8WdG1kp9Unec\nexLYE21BzgqrhVgNGuqljV6OW5jR3+DcEzuhIGLegiLWsyic/DLQh1y9to8GZmm4\nKm5ikcnLV9Ju3Kd5xhT1UnwwNYkRw6PhbA23n5O4nFMLJK//P/QMFTu71H6qkKwH\nln4uZdF9f1kC5jn4/a3MoaAMSnVil6Pm5b+KXl5hJn9qZiEOQiIy51Y/d/EVq5ID\nuThc8yc70vSZDXKBIYEIRLh4KFmzgOC0vRMpkBEPgQKBgQD8clAGwjvltJdDyMai\nef+8/4SK2oiaDTaHoeSLpK3I2E3PQpej0rjYJUmmitqvAEXA39G0O6Mzxx6oGL4c\nL3xm/v9SUGKqpF7SVWuM81vSZap6L71+9swZtDMxQbWd4J97K2jcK2gh69VD1GQn\nSgwKzVjKaJAzHI7h0BqlNNN5gQKBgQDUhVaR5+XHCL96WFmDRn7TGgh3gA1Hbs7T\n/PsT1U3/9SoZVgZRIbsH6XptQM5oThrNl/pEfvKlkPpBSslqAwkbDMsAR5K8/fNi\nViVAOHIiqvlvX4NVXClMOdJ8erFN9PVLGNPWwGKulmVOrDW9SF99hKpVaI/XwGQS\niLykL1t9GQKBgA7jSvbrE487dERKHfTNDxj9VLq/opi7OMEM+iaGIr2ajBQyEDFY\nJxCQOmS5AaaadIKocHyZm8lc7+Dn/KY64rJMTZB0Ly1zHih3Yy1f2MVyu3gTQrCv\nK2BEsVQxVN2ntqAT8k4xvSVq/BvQ9csfYdBtRdRCEGcDQyXsGPYvRF2BAoGAecj/\nVxWBA5HryHygry3St76PY4uqEGlbdPfgGfl+fVNNEL/PVubxexM86SbeIb/AdFjH\nPkFRY7e08X2d9nZO3YVzP3HEkTEmLBAZwLeYEG3SCxS8+kmaEOiBynu052uctbBA\nlSwiYNIms/LTyOiUcCV6Rv9ojsbdkhFxqNTKpOECgYBbPffU8avXVqC8ZiIJ8qzZ\n+dLyGw2K6Sh+6WUs6TJjx4bCIgCdYTDdewu+cd8dChe9MX8obq/67UBnQEFEeZyE\nAIdXZeN1i5YwLil/MtiD1KafKVsKtgUmFFnzFtHsjYBaz9FYctig1+vT18rye2Q5\ncwCn/4frAfaCRPuzWs8SuQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-mvzeo@datastreamlit.iam.gserviceaccount.com",
  "client_id": "103047441403328155275",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-mvzeo%40datastreamlit.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


if not firebase_admin._apps:
    cred = credentials.Certificate(config)
    default_app = initialize_app(cred, {'databaseURL':'https://datastreamlit-default-rtdb.asia-southeast1.firebasedatabase.app/'})

ref = db.reference('prediksi_air')  # Tentukan referensi ke node tertentu di database
# load the pre-trained model and scaler
model = joblib.load('modelss5.pkl')

def predict_water(ph, temperature, turbidity):
    # create a dataframe with the user input
    input_data = pd.DataFrame([[ph, temperature, turbidity]], 
                              columns=['pH','Temperature','turbidity'])
    # make predictions
    prediction = model.predict(input_data)
    return prediction[0]

# db = db.database()

st.title('Water Prediction')
st.header("How is the water quality today?")
ph = st.number_input('pH:')
temperature = st.number_input('Temperature:')
turbidity = st.number_input('turbidity:')


if st.button('Predict'):
    prediction = predict_water(ph, temperature, turbidity)
    if prediction == 0 :
        st.write('Pure')
    elif prediction == 1:
        st.write('Muddy')
    else: 
        st.write('Undefined')
    data = {
        'pH': int(ph),
        'Temperature' : int(temperature),
        'turbidity': int(turbidity),
        'prediksi': int(prediction)
    }
    new_data_ref = ref.push()  # Buat child baru di bawah node 'prediksi_air'
    new_data_ref.set(data)  # Set data ke child yang baru saja dibuat

    st.success('Successfully Predicted')

