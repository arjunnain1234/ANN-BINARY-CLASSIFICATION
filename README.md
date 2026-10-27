# Customer Retention Predictor 🚀

An interactive web application built with **Streamlit** and a machine learning model (Artificial Neural Network) to predict customer churn and retention based on demographic and financial features.

---

## 🌟 Features

* **Interactive User Interface:** Easily adjust customer parameters such as Age, Geography, Balance, Credit Score, and Estimated Salary using intuitive sliders and dropdowns.
* **Real-time Prediction:** Instantly calculates and visualizes whether a customer is likely to churn.
* **Built with Streamlit:** Fast, lightweight, and responsive web framework for data-driven applications.

---

## 🛠️ Tech Stack

* **Frontend & UI:** [Streamlit](https://streamlit.io/)
* **Machine Learning:** Artificial Neural Network (ANN) using TensorFlow/Keras and Scikit-Learn
* **Language:** Python

---

## 🚀 Getting Started Locally

Follow these steps to set up and run the project on your machine.

### 1. Clone the Repository

```bash
git clone https://github.com/arjunnain1234/AAN-BINARY-CLASSIFICATION.git
cd AAN-BINARY-CLASSIFICATION
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📊 Input Features

The prediction model evaluates the following customer attributes:

* **Geography:** Customer's country of residence (e.g., Spain, France, Germany)
* **Gender:** Male or Female
* **Age:** Customer age (range: 18 - 90)
* **Balance:** Account balance
* **Credit Score:** Customer credit rating
* **Estimated Salary:** Annual estimated salary
* **Tenure:** Number of years the customer has been with the bank
* **Number of Products:** Number of bank products the customer uses
* **Has Credit Card:** Whether the customer holds a credit card (Yes/No)
* **Is Active Member:** Whether the customer is an active member (Yes/No)

---

## ☁️ Live Demo

Check out the live deployment of the app here: [Customer Retention Predictor Live App](https://ann-binary-classification.streamlit.app/)
<img width="1072" height="1390" alt="image" src="https://github.com/user-attachments/assets/b163b4c0-57ae-4324-824e-ae37be590466" />


---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## 📝 License

This project is open source.
