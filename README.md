# 🚗 Car Price Prediction Using Machine Learning  

This project focuses on predicting the selling price of used cars using various machine learning models. It involves complete data preprocessing, feature engineering, model training, evaluation, and comparison to identify the best-performing algorithm. Among all the models tested, the **Random Forest Regressor achieved the highest accuracy with an R² score of 94%**.

---

## 📌 Problem Statement  
Estimating the correct selling price of a used car is a challenging task due to multiple influencing factors such as vehicle age, mileage, fuel type, engine specifications, transmission type, and ownership history. Traditional pricing methods are often inaccurate and subjective. This project aims to solve this problem using machine learning-based regression techniques.

---

## 🎯 Objective  
- To build an accurate machine learning model to predict used car prices.  
- To analyze the factors that influence car prices the most.  
- To compare multiple regression and ensemble models and select the best-performing one.  

---

## 📊 Dataset Description  
The dataset contains **8,128 records** with the following key features:
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

Several columns contained mixed data types (e.g., "250 cc", "19 kmpl") which were cleaned and converted into numerical format during preprocessing.

---

## ⚙️ Data Preprocessing & Feature Engineering  
- Handling missing values  
- Removing units from numerical features (cc, kmpl, bhp, etc.)  
- Converting categorical features using encoding techniques  
- Outlier detection and treatment  
- Multicollinearity detection using VIF  

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
|--------|----------|
| Linear Regression | 66% |
| Decision Tree | 91% |
| Pruned Decision Tree | 90% |
| KNN | 84% |
| ✅ Random Forest | ✅ **94%** |

✅ **Random Forest performed the best with the highest R² and adjusted R² score of 94%.**

---

## ✅ Final Conclusion  
Linear Regression performed the worst due to violation of regression assumptions such as multicollinearity and presence of outliers. Tree-based models performed significantly better, with Random Forest emerging as the most accurate and reliable model for predicting used car prices.

---

## 🚀 Future Scope  
- Deploy the model using Flask or Streamlit  
- Integrate real-time car data  
- Experiment with boosting algorithms such as XGBoost and Gradient Boosting  
- Improve feature engineering using domain expertise  

---

## 🛠️ Technologies Used  
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib & Seaborn  
- Statsmodels  
- Jupyter Notebook  

---
  


---

## 📜 License  
This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 👨‍💻 Author  
**Usman Shaikh**  
Machine Learning & Data Science Enthusiast  

---

✅ If you found this project useful, feel free to ⭐ star the repository!

