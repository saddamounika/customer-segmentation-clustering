import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Customer Segmentation", layout="wide")
st.title("🛍️ Mall Customer Segmentation (K-Means)")

# Load Data
df = pd.read_csv(r"C:\Users\91630\OneDrive\Desktop\Mouni\projects\Customer segmentation\Mall_Customers.csv")

# Feature Selection (Annual Income and Spending Score)
X = df.iloc[:, [3, 4]].values 

# Sidebar for User Input
st.sidebar.header("Settings")
k_value = st.sidebar.slider("Select Number of Clusters (k)", 2, 10, 5)

# 1. Elbow Method Calculation
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# 2. Run Final Model
kmeans = KMeans(n_clusters=k_value, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X)
df['Cluster'] = df['Cluster'].astype(str)

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("The Elbow Method")
    fig, ax = plt.subplots()
    ax.plot(range(1, 11), wcss, marker='o')
    ax.set_title('Finding the Optimal K')
    ax.set_xlabel('Number of Clusters')
    ax.set_ylabel('WCSS')
    st.pyplot(fig)
    st.info("The 'Elbow' point shows the best number of clusters.")

with col2:
    st.subheader("3D Customer Clusters")
    # 3D Plot: Age vs Income vs Spending Score
    fig_3d = px.scatter_3d(df, x='Age', y='Annual Income (k$)', z='Spending Score (1-100)',
                           color='Cluster', 
                           title="Customer Segments in 3D Space",
                           color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig_3d, use_container_width=True)

st.subheader("Segmented Data Table")
st.write(df.sort_values('Cluster'))