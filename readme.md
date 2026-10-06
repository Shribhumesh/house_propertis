# 🏠 House Price Prediction

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas\&logoColor=white)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn\&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?logo=matplotlib\&logoColor=white)
![Linear Regression](https://img.shields.io/badge/ML-Linear%20Regression-green)
![GitHub](https://img.shields.io/badge/Hosted%20on-GitHub-black?logo=github)

</p>

## 📌 Project Overview

**House Price Prediction** is a Machine Learning web application built with **Python and Streamlit**.

The application predicts the estimated price of a house based on:

* 📐 Area in square feet
* 🛏️ Number of bedrooms
* 🚿 Number of bathrooms
* 🏚️ Age of the house

The prediction is generated using a **Linear Regression** machine learning model trained on a housing dataset.

The application also displays model performance, data visualizations, and the complete housing dataset.

---

## 🚀 Features

### 🏠 House Price Prediction

Users can enter house details using interactive sliders and get an estimated house price in **Indian Lakhs (₹)**.

### 🤖 Machine Learning Model

The project uses:

**Linear Regression**

The model learns the relationship between:

`Area + Bedrooms + Bathrooms + House Age → House Price`

### 📊 Model Evaluation

The application evaluates the model using the:

**R² Score (Coefficient of Determination)**

### 📈 Data Visualization

The application provides three visualizations:

1. **Area vs House Price**
2. **Bedrooms vs Average House Price**
3. **Actual Price vs Predicted Price**

### 📋 Dataset Display

The complete housing dataset can also be viewed directly inside the Streamlit application.

---

## 🛠️ Technologies Used

| Technology           | Purpose                        |
| -------------------- | ------------------------------ |
| 🐍 Python            | Main programming language      |
| 🎈 Streamlit         | Web application interface      |
| 🐼 Pandas            | Data loading and manipulation  |
| 🤖 Scikit-learn      | Machine Learning               |
| 📉 Linear Regression | House price prediction         |
| 📊 Matplotlib        | Data visualization             |
| 📄 CSV               | Housing dataset                |
| 🔀 Git/GitHub        | Version control and repository |

---

## 🧠 Machine Learning Workflow

```text
             Housing Dataset
                    │
                    ▼
             Load CSV Data
                    │
                    ▼
          Select Features & Target
                    │
                    ▼
            Train/Test Split
                    │
                    ▼
          Linear Regression Model
                    │
                    ▼
               Train Model
                    │
                    ▼
             Make Predictions
                    │
                    ▼
               R² Evaluation
                    │
                    ▼
          Streamlit Web Application
                    │
                    ▼
          Estimated House Price
```

---

## 📂 Project Structure

```text
house_propertis/
│
├── app.py
├── train_model.py
├── house_data.csv
├── readme.md
└── README.md
```

### 📄 File Description

#### `app.py`

Main Streamlit application.

It:

* Loads the housing dataset
* Selects input features
* Splits data into training and testing sets
* Creates the Linear Regression model
* Trains the model
* Calculates the R² score
* Predicts house prices
* Displays charts and dataset information

#### `house_data.csv`

Contains the housing data used for training and testing the model.

### Dataset Columns

| Column      | Description               |
| ----------- | ------------------------- |
| `area`      | House area in square feet |
| `bedrooms`  | Number of bedrooms        |
| `bathrooms` | Number of bathrooms       |
| `age`       | Age of the house          |
| `price`     | House price               |

#### `train_model.py`

Python file included in the project for model-training related work.

---

## 📊 Dataset

The project currently uses a small sample housing dataset containing information such as area, bedrooms, bathrooms, house age, and price.

Example:

| Area | Bedrooms | Bathrooms | Age |        Price |
| ---: | -------: | --------: | --: | -----------: |
|  800 |        1 |         1 |  12 |   ₹25,00,000 |
| 1200 |        3 |         2 |   6 |   ₹43,00,000 |
| 1500 |        3 |         2 |   5 |   ₹56,00,000 |
| 2000 |        4 |         3 |   2 |   ₹82,00,000 |
| 2500 |        5 |         4 |   0 | ₹1,10,00,000 |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shribhumesh/house_propertis.git
```

### 2. Open the Project Folder

```bash
cd house_propertis
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Required Libraries

```bash
pip install streamlit pandas matplotlib scikit-learn
```

### 6. Run the Application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🖥️ Application Interface

The application provides an interactive sidebar where users can select:

```text
Area       → 500 - 3000 sq.ft
Bedrooms   → 1 - 6
Bathrooms  → 1 - 5
House Age  → 0 - 30 years
```

After selecting the values, the application displays the predicted house price in Lakhs.

---

## 📈 Model Evaluation

The project uses **R² Score** to evaluate the Linear Regression model.

```python
accuracy = r2_score(
    y_test,
    test_predictions
)
```

The R² score indicates how well the model explains the variation in house prices.

---

## 📊 Visualizations

### 1. Area vs House Price

Shows the relationship between house area and price.

### 2. Bedrooms vs Average House Price

Shows the average house price for different numbers of bedrooms.

### 3. Actual vs Predicted Price

Compares the actual house prices from the test dataset with the prices predicted by the machine learning model.

---

## 🔮 Future Improvements

Some possible improvements for this project are:

* 🔹 Use a larger real-world housing dataset
* 🔹 Add more house features such as location and parking
* 🔹 Compare multiple ML algorithms
* 🔹 Add model accuracy comparison
* 🔹 Add data preprocessing
* 🔹 Add feature scaling where required
* 🔹 Save the trained model using `joblib`
* 🔹 Improve the Streamlit UI
* 🔹 Deploy the application online

---

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

* Python programming
* Data handling with Pandas
* Data visualization with Matplotlib
* Machine Learning fundamentals
* Linear Regression
* Train/Test Split
* Model evaluation using R² Score
* Streamlit application development
* Git and GitHub

---

## 👨‍💻 Author

**Shribhumesh Bandiwadekar**

BCA Student | Web Design | Video Editing | Machine Learning

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is created for educational and learning purposes.

