import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Disable the warning for using Matplotlib's global figure object
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load your data
data = pd.read_csv('Marketingdata.csv')

# Define the pages using Streamlit's `st.sidebar`
page = st.sidebar.selectbox("Select a page", ["Heatmaps", "Product Profits", "Earnings Analysis", "Gender Analysis", "Age Group Analysis"])

if page == "Heatmaps":
    st.title('Heatmaps')
    
    st.subheader('Correlation Heatmap 1: Spending Limit vs. Revenue')
    x = data['Spending Limit']
    y = data['Revenue']
    corr = np.corrcoef(x, y)
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, fmt=".1f", linewidth=.1, ax=ax)
    st.pyplot(fig)

    st.subheader('Correlation Heatmap 2: Revenue vs. Net Profit')
    x = data['Revenue']
    y = data['Net Profit']
    corr = np.corrcoef(x, y)
    fig2, ax2 = plt.subplots()
    sns.heatmap(corr, annot=True, fmt=".1f", linewidth=.1, ax=ax2)
    st.pyplot(fig2)

elif page == "Product Profits":
    st.title('Product Profits')
    
    data['Profit'] = data['Revenue'] - data['Marketing Costs']
    product_profit = data.groupby('Purchased Product Type')['Profit'].sum()
    st.subheader('Profit by Purchased Product Type')
    fig3, ax3 = plt.subplots()
    plt.pie(product_profit, labels=product_profit.index, autopct='%1.1f%%', startangle=140)
    st.pyplot(fig3)

elif page == "Earnings Analysis":
    st.title('Earnings Analysis')
    
    st.subheader('Mean Earnings by Marital Status')
    marital_earnings = data.groupby('Marital Status')['Earning'].mean().sort_values(ascending=False)
    fig4, ax4 = plt.subplots()
    marital_earnings.plot(kind='bar', color='skyblue')
    st.pyplot(fig4)

    st.subheader('Earnings Analysis by Age Groups')
    data_above_18 = data[data['Age'] > 18]
    data_above_30 = data[data['Age'] > 30]
    data_above_40 = data[data['Age'] > 40]

    fig5, axes5 = plt.subplots(1, 3, figsize=(15, 5))
    axes5[0].bar(data_above_18['Age'], data_above_18['Earning'], color='skyblue')
    axes5[0].set_title('Earnings (Age > 18)')
    axes5[0].set_xlabel('Age')
    axes5[0].set_ylabel('Earnings')

    axes5[1].bar(data_above_30['Age'], data_above_30['Earning'], color='lightcoral')
    axes5[1].set_title('Earnings (Age > 30)')
    axes5[1].set_xlabel('Age')
    axes5[1].set_ylabel('Earnings')

    axes5[2].bar(data_above_40['Age'], data_above_40['Earning'], color='lightgreen')
    axes5[2].set_title('Earnings (Age > 40)')
    axes5[2].set_xlabel('Age')
    axes5[2].set_ylabel('Earnings')
    st.pyplot(fig5)



elif page == "Gender Analysis":
    st.title('Gender Analysis')

    st.subheader('Earnings by Gender')
    earnings_by_gender = data.groupby('Gender')['Earning'].mean().sort_values(ascending=False)
    fig6, ax6 = plt.subplots()
    earnings_by_gender.plot(kind='bar', color='lightcoral')
    st.pyplot(fig6)
    plt.close(fig6)

    st.subheader('Spending Limit by Gender')
    spending_limit_by_gender = data.groupby('Gender')['Spending Limit'].mean().sort_values(ascending=False)
    fig7, ax7 = plt.subplots()
    spending_limit_by_gender.plot(kind='bar', color='lightblue')
    st.pyplot(fig7)
    plt.close(fig7)

elif page == "Age Group Analysis":
    st.title('Age Group Analysis')

    st.subheader('Earnings by Age Groups')
    earnings_above_18 = data[data['Age'] > 18]
    earnings_above_30 = data[data['Age'] > 30]
    earnings_above_40 = data[data['Age'] > 40]

    fig8, axes8 = plt.subplots(1, 3, figsize=(15, 5))
    axes8[0].bar(earnings_above_18['Age'], earnings_above_18['Earning'], color='skyblue')
    axes8[0].set_title('Earnings (Age > 18)')
    axes8[0].set_xlabel('Age')
    axes8[0].set_ylabel('Earnings')

    axes8[1].bar(earnings_above_30['Age'], earnings_above_30['Earning'], color='lightcoral')
    axes8[1].set_title('Earnings (Age > 30)')
    axes8[1].set_xlabel('Age')
    axes8[1].set_ylabel('Earnings')

    axes8[2].bar(earnings_above_40['Age'], earnings_above_40['Earning'], color='lightgreen')
    axes8[2].set_title('Earnings (Age > 40)')
    axes8[2].set_xlabel('Age')
    axes8[2].set_ylabel('Earnings')
    st.pyplot(fig8)
    plt.close(fig8)
