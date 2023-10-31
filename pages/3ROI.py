import streamlit as st

# Function to calculate Return on Investment (ROI)
def calculate_roi(net_profit, marketing_costs):
    roi = net_profit / marketing_costs
    return roi

# Create a new Streamlit page for ROI calculation
st.title('Return on Investment (ROI) Calculation')

# Allow user input for Net Profit and Marketing Costs
net_profit = st.number_input('Enter Net Profit', value=10000)
marketing_costs = st.number_input('Enter Marketing Costs', value=5000)

# Button to trigger ROI calculation
if st.button('Calculate ROI'):
    roi_value = calculate_roi(net_profit, marketing_costs)

    # Display the calculated ROI
    st.subheader('Calculated ROI')
    st.write(f'The Return on Investment (ROI) is: {roi_value:.2f}')
