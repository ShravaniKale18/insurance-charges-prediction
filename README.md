# 🏥 Insurance Charges Prediction

This is a Machine Learning project that predicts a person's insurance charges based on their details such as age, BMI, number of children, smoking status, sex, and region.

I built this project to practice **Multiple Linear Regression** and deployed it using **Streamlit**.

---

## 📌 Project Objective

The goal of this project is to predict the medical insurance charges of a person using Multiple Linear Regression.

---

## 📂 Dataset

The dataset contains the following features:

- Age
- Sex
- BMI
- Children
- Smoker
- Region
- Charges (Target)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle

---

## 📊 Project Workflow

- Loaded the dataset
- Performed Exploratory Data Analysis (EDA)
- Checked missing values
- Visualized the data using histograms and a correlation heatmap
- Converted categorical columns into numerical values using one-hot encoding
- Split the dataset into training and testing sets
- Trained a Multiple Linear Regression model
- Evaluated the model using R² Score, MAE, and MSE
- Saved the trained model using Pickle
- Built a Streamlit web application for predictions

---

## 📈 Model Performance

- **R² Score:** 0.759
- **Mean Absolute Error (MAE):** 4207.29
- **Mean Squared Error (MSE):** 35314912.03

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/insurance-charges-prediction.git
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📸 Application

The application allows users to enter:

- Age
- BMI
- Number of Children
- Sex
- Smoker Status
- Region

After clicking **Predict Charges**, the application estimates the insurance charges using the trained machine learning model.

---

## 📁 Project Structure

```
insurance-charges-prediction/
│
├── app.py
├── insurance.csv
├── insurance_model.pkl
├── Insurance Prediction.ipynb
├── requirements.txt
└── README.md
```

---

## 📚 What I Learned

Through this project, I learned:

- Exploratory Data Analysis (EDA)
- Data Visualization
- Multiple Linear Regression
- Feature Encoding
- Model Evaluation
- Model Serialization using Pickle
- Building Machine Learning apps with Streamlit

---

## 👩‍💻 Author

**Shravani Kale**

If you have any suggestions or feedback, feel free to connect with me.