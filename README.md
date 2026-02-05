# 🛍️ Mall Customer Segmentation using K-Means Clustering

### 🚀 Project Overview
As an **AI/ML student** specializing in **Data Science**, I developed this project to demonstrate how Unsupervised Learning can be applied to retail business data. 
This application segments customers based on their annual income and spending habits to help businesses create targeted marketing strategies.

### 🛠️ Tech Stack
* [cite_start]**Programming Language:** Python [cite: 22]
* **Machine Learning:** K-Means Clustering (Scikit-learn)
* [cite_start]**Data Analysis:** Pandas, NumPy [cite: 23]
* **Visualization:** Plotly (3D Interactive Charts), Matplotlib
* **Deployment:** Streamlit



### 📊 Key Features
* **The Elbow Method:** Implemented logic to find the optimal number of clusters (K) by calculating WCSS (Within-Cluster Sum of Squares).
* **Interactive Dashboard:** Users can dynamically change the number of clusters using a slider and see real-time updates.
* **3D Data Mapping:** Visualized Age, Income, and Spending Score in a 3D space for deeper insights.


### 🧪 Business Insights (The 5 Segments)
Through this model, I identified 5 distinct customer groups:
1. **VIPs:** High Income & High Spending.
2. **Careful:** High Income & Low Spending.
3. **Target:** Average Income & Average Spending.
4. **Spendthrifts:** Low Income & High Spending.
5. **Sensible:** Low Income & Low Spending.

### ⚙️ How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
