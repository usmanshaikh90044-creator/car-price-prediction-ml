# 🚗 Car Price Prediction Using Machine Learning  

## 🌐 Live Demo
🔗 **Streamlit App:** https://car-price-prediction-usman.streamlit.app

---

## 📌 Problem Statement  
Estimating the correct selling price of a used car is challenging due to multiple influencing factors such as vehicle age, mileage, fuel type, engine specifications, transmission type, and ownership history. Traditional pricing methods are often subjective and inaccurate. This project aims to solve this problem using machine learning-based regression techniques.

---

## 🎯 Objective  
- Build an accurate machine learning model to predict used car prices  
- Analyze key factors influencing car prices  
- Compare multiple regression models and select the best-performing one  

---

## 📊 Dataset Description  
The dataset contains **8,128 records** with the following features:

- Car Name  
- Year of Manufacture  
- Selling Price (Target Variable)  
- Kilometers Driven  
- Fuel Type  
- Seller Type  
- Transmission Type  
- Owner Type  
- Mileage  
- Engine  
- Max Power  
- Torque  
- Number of Seats  

Several columns contained mixed data types (e.g., `"250 cc"`, `"19 kmpl"`) which were cleaned and converted into numerical format during preprocessing.

---

## ⚙️ Data Preprocessing & Feature Engineering  
- Handling missing values  
- Removing units from numerical features (cc, kmpl, bhp, etc.)  
- Encoding categorical features  
- Outlier detection and treatment  
- Multicollinearity analysis using VIF  

---

## 🤖 Models Implemented  
- Linear Regression  
- Decision Tree Regressor  
- Pruned Decision Tree  
- K-Nearest Neighbors (KNN)  
- Random Forest Regressor  

---

## 🏆 Model Performance Summary  

| Model | R² Score |
|------|----------|
| Linear Regression | 66% |
| Decision Tree | 91% |
| Pruned Decision Tree | 90% |
| KNN | 84% |
| ✅ Random Forest | **94%** |

✅ **Random Forest achieved the best performance with an R² score of 94%.**

---

## ✅ Final Conclusion  
Linear Regression performed poorly due to multicollinearity and outliers. Tree-based models performed significantly better, with **Random Forest emerging as the most accurate and robust model** for used car price prediction.

---

## 🚀 Deployment  
The final model is deployed as a **public web application using Streamlit Cloud**, allowing users to input car details and instantly get a price prediction.

🔗 **Live App:** https://car-price-prediction-usman.streamlit.app

---

## 🚀 Future Scope  
- Integrate real-time car listing data  
- Experiment with boosting algorithms (XGBoost, Gradient Boosting)  
- Improve feature engineering using domain expertise  

---

## 🛠️ Technologies Used  
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib & Seaborn  
- Statsmodels  
- Streamlit  

---

## 📜 License  
This project is licensed under the **MIT License**.

---

## 👨‍💻 Author  
**Usman Shaikh**  
Machine Learning & Data Science Enthusiast  

⭐ If you found this project useful, feel free to star the repository!
