import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Function to perform clustering
def perform_clustering(data, k):
    kmeans = KMeans(n_clusters=k, random_state=42)
    data['Cluster'] = kmeans.fit_predict(data[['Earning', 'Earning Potential']])
    return data

# Allow user to upload a CSV file
st.title('Spending Limit Prediction & Clustering App')
st.write("Please upload your 'train.csv' dataset that has ['Earning', 'Earning Potential'] as attributes.")
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    # Load the uploaded CSV data into a DataFrame
    data = pd.read_csv(uploaded_file)

    # Display the first few rows of the uploaded dataset
    st.subheader('Uploaded Dataset')
    st.write(data.head())

    # Clustering
    st.subheader('Clustering')

    k = st.slider('Select number of clusters', min_value=2, max_value=10, value=3)
    clustered_data = perform_clustering(data, k)

    # Display the cluster assignments
    st.subheader('Cluster Assignments')
    st.write(clustered_data[['Earning', 'Earning Potential', 'Cluster']])

    # Data processing and model training
    X = clustered_data[['Earning', 'Earning Potential']]  # Exclude 'Cluster' feature
    y = clustered_data['Spending Limit']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define different algorithms for user selection
    algorithms = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(),
        'Gradient Boosting': GradientBoostingRegressor(),
        'Support Vector Regressor (SVR)': SVR(),
        'Decision Tree': DecisionTreeRegressor()
    }

    # User selects algorithm from the dropdown
    selected_algorithm = st.selectbox('Select a regression algorithm', list(algorithms.keys()))

    model = algorithms[selected_algorithm]
    model.fit(X_train, y_train)

    # Provide input fields for new user data
    st.subheader('Enter new user data to predict Spending Limit:')
    earning = st.number_input('Earning', value=1200)
    earning_potential = st.number_input('Earning Potential', value=2000)

    # Predict Spending Limit for the user input
    predicted_spending_limit = model.predict([[earning, earning_potential]])

    # Display the predicted Spending Limit
    st.subheader('Predicted Spending Limit for the new user:')
    st.write(f'{predicted_spending_limit[0]:.2f}')
