import streamlit as st 
import tensorflow as tf 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
import pickle 
import pandas as pd 
import numpy as np 


# Loading the model

model = tf.keras.models.load_model('model-1.h5')

# Loading the pickle files and encoders

with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file)

with open('onehot_encoder_geo.pkl','rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('label_encoder_yes_no.pkl', 'rb') as file:
    label_encoder_yes_no = pickle.load(file)


# Streamlit heading

st.title('Customer retention predictor')


# User input

geography = st.selectbox('Geography',onehot_encoder_geo.categories_[0])
gender = st.selectbox('Gender',label_encoder_gender.classes_)
age = st.slider('Age',18,90)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure',0,10)
num_of_products = st.slider('Number of products',1,4)
has_cr_card = st.selectbox('Has Credit Card', label_encoder_yes_no.classes_)
is_active_member = st.selectbox('Is Active Member',label_encoder_yes_no.classes_)

# User data to data frame

input_data = pd.DataFrame({

        'CreditScore':[credit_score],
        'Gender':[label_encoder_gender.transform([gender])[0]],
        'Age':[age],
        'Tenure':[tenure],
        'Balance':[balance],
        'NumOfProducts':[num_of_products],
        'HasCrCard':[label_encoder_yes_no.transform([has_cr_card])[0]],
        'IsActiveMember':[label_encoder_yes_no.transform([is_active_member])[0]],
        'EstimatedSalary':[estimated_salary]
})


# One hot encode geography

onehot_encoded_geo = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(onehot_encoded_geo, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

# Concat dataframes 

input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df] , axis=1)

# Scale the Input data

scaled_input_data = scaler.transform(input_data)

prediction = model.predict(scaled_input_data)
prediction_prob = prediction[0][0]
num = np.float32(prediction_prob)

if num>0.5:
    st.write('Customer is likely to churn')

else:
    st.write('Customer is not likely to churn')



