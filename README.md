# 🛒 Market Basket Recommendation System

An AI-powered recommendation system that suggests products based on user selections using the **Apriori Algorithm** and **Association Rule Mining**.

---

## 📌 Features

* 🎯 Smart Product Recommendations
* 🛒 Frequently Bought Together Items
* 🔥 Most Popular Products
* 📊 Interactive Product Relationship Graph
* 🎛️ Sidebar Filters (Support & Confidence)
* 💡 Clean and Modern UI (Dashboard Style)

---

## 🧠 How It Work

This system uses the **Apriori Algorithm** to analyze transaction data and generate association rules.

* **Antecedents** → Selected products
* **Consequents** → Recommended products
* **Confidence** → Likelihood of recommendation
* **Support** → Frequency of item combination

---

## 🛠️ Tech Stack

* **Frontend/UI** → Streamlit + HTML + CSS
* **Backend** → Python
* **ML Algorithm** → Apriori (mlxtend)
* **Visualization** → Plotly + NetworkX
* **Data Processing** → Pandas

---

## 📂 Project Structure

```
market-basket-recommendation/
│── app.py
│── association_rules.csv
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/market-basket-recommendation.git
cd market-basket-recommendation
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Application

```
streamlit run app.py
```

---

## 📊 Input Example

Select products like:

```
milk, bread
```

### Output:

```
butter, jam (Recommended)
```

---

## 📸 Screenshots

* Dashboard UI
* Recommendations Section
* Graph Visualization

*(Add screenshots here)*

---

## 📈 Future Improvements

* 🔥 Real-time recommendation API (FastAPI)
* 🖼️ Product images (Amazon-style UI)
* 🔐 User login system
* ☁️ Cloud deployment (AWS / GCP)
* 📦 Integration with real e-commerce datasets

---

## 💼 Use Cases

* E-commerce platforms
* Retail analytics
* Inventory optimization
* Cross-selling strategies

---

## 👨‍💻 Author

**Kanha Patidar**
B.Tech CSIT (IT)
Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
