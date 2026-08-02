
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Visit with Us")
st.subheader("Wellness Tourism Package Prediction")

st.write("Enter Customer Details")

age = st.number_input("Age", 18, 80, 30)
city = st.selectbox("City Tier", [1,2,3])
duration = st.number_input("Duration Of Pitch",0,60,15)

occupation = st.selectbox(
    "Occupation",
    ["Salaried","Small Business","Large Business","Free Lancer"]
)

gender = st.selectbox(
    "Gender",
    ["Male","Female"]
)

persons = st.number_input("Number Of Person Visiting",1,10,2)
followups = st.number_input("Number Of Followups",0,10,2)

product = st.selectbox(
    "Product Pitched",
    ["Basic","Standard","Deluxe","Super Deluxe","King"]
)

star = st.selectbox("Preferred Property Star",[3,4,5])

marital = st.selectbox(
    "Marital Status",
    ["Single","Married","Divorced"]
)

trips = st.number_input("Number Of Trips",0,20,3)
passport = st.selectbox("Passport",[0,1])
pitch = st.slider("Pitch Satisfaction",1,5,3)
owncar = st.selectbox("Own Car",[0,1])
children = st.number_input("Children Visiting",0,5,0)

designation = st.selectbox(
    "Designation",
    ["Executive","Manager","Senior Manager","AVP","VP"]
)

income = st.number_input("Monthly Income",1000,100000,25000)

occupation_map = {
    "Salaried":0,
    "Small Business":1,
    "Large Business":2,
    "Free Lancer":3
}

gender_map = {"Male":1,"Female":0}

product_map = {
    "Basic":0,
    "Standard":1,
    "Deluxe":2,
    "Super Deluxe":3,
    "King":4
}

marital_map = {
    "Single":2,
    "Married":1,
    "Divorced":0
}

designation_map = {
    "Executive":0,
    "Manager":1,
    "Senior Manager":2,
    "AVP":3,
    "VP":4
}

if st.button("Predict"):

    data = pd.DataFrame([[
        age,
        0,
        city,
        duration,
        occupation_map[occupation],
        gender_map[gender],
        persons,
        followups,
        product_map[product],
        star,
        marital_map[marital],
        trips,
        passport,
        pitch,
        owncar,
        children,
        designation_map[designation],
        income
    ]],
    columns=[
        'Age',
        'TypeofContact',
        'CityTier',
        'DurationOfPitch',
        'Occupation',
        'Gender',
        'NumberOfPersonVisiting',
        'NumberOfFollowups',
        'ProductPitched',
        'PreferredPropertyStar',
        'MaritalStatus',
        'NumberOfTrips',
        'Passport',
        'PitchSatisfactionScore',
        'OwnCar',
        'NumberOfChildrenVisiting',
        'Designation',
        'MonthlyIncome'
    ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Customer is likely to Purchase")
    else:
        st.error("Customer is unlikely to Purchase")
