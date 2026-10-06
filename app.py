import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏡",
    layout="wide"
)

st.title("🏠 AI House Price Prediction")

st.write(
    "Enter the house details below and the machine learning "
    "model will estimate the house price."
)

# Load dataset
data = pd.read_csv("house_data.csv")

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

# Features and target
X = data[["area", "bedrooms", "bathrooms", "age"]]
y = data["price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Test predictions
test_predictions = model.predict(X_test)

# Calculate R² score
accuracy = r2_score(
    y_test,
    test_predictions
)

# Sidebar
st.sidebar.header("🏠 Enter House Details")

area = st.sidebar.slider(
    "Area (sq.ft)",
    500,
    3000,
    1500
)

bedrooms = st.sidebar.slider(
    "Bedrooms",
    1,
    6,
    3
)

bathrooms = st.sidebar.slider(
    "Bathrooms",
    1,
    5,
    2
)

age = st.sidebar.slider(
    "House Age",
    0,
    30,
    5
)

# Input data
input_data = pd.DataFrame(
    [[area, bedrooms, bathrooms, age]],
    columns=[
        "area",
        "bedrooms",
        "bathrooms",
        "age"
    ]
)

# Prediction
prediction = model.predict(input_data)[0]

# Convert price to lakhs
price_lakhs = prediction / 100000

# Estimated price
st.subheader("💰 Estimated House Price")

st.metric(
    label="Predicted Price",
    value=f"₹{price_lakhs:.2f} lakhs"
)

# Model performance
st.subheader("🤖 Model Performance")

st.write(
    f"R² Score: **{accuracy:.2f}**"
)

# Selected house details
st.subheader("🏠 Selected House Details")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Area",
    f"{area} sq.ft"
)

col2.metric(
    "Bedrooms",
    bedrooms
)

col3.metric(
    "Bathrooms",
    bathrooms
)

col4.metric(
    "Age",
    f"{age} years"
)

# Area vs Price
st.subheader("📊 Area vs House Price")

fig1, ax1 = plt.subplots()

ax1.scatter(
    data["area"],
    data["price"] / 100000
)

ax1.set_xlabel("Area (sq.ft)")
ax1.set_ylabel("Price (Lakhs)")
ax1.set_title("Area vs House Price")

st.pyplot(fig1)

# Bedrooms vs Average Price
st.subheader("📊 Bedrooms vs Average House Price")

bedroom_prices = (
    data.groupby("bedrooms")["price"]
    .mean()
    / 100000
)

fig2, ax2 = plt.subplots()

ax2.bar(
    bedroom_prices.index,
    bedroom_prices.values
)

ax2.set_xlabel("Bedrooms")
ax2.set_ylabel("Average Price (Lakhs)")
ax2.set_title("Bedrooms vs Average House Price")

st.pyplot(fig2)

# Actual vs Predicted
st.subheader("🎯 Actual Price vs Predicted Price")

fig3, ax3 = plt.subplots()

ax3.scatter(
    y_test / 100000,
    test_predictions / 100000
)

ax3.set_xlabel("Actual Price (Lakhs)")
ax3.set_ylabel("Predicted Price (Lakhs)")
ax3.set_title("Actual vs Predicted Prices")

st.pyplot(fig3)

# Dataset
st.subheader("📋 Housing Dataset")

st.dataframe(data)