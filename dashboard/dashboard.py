import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

# Assuming 'original_df' is your DataFrame containing the data
all_df = pd.read_csv("all_data.csv")
# Calculate no_1
no_1 = all_df.groupby(by="product_category_name_english").agg({
    "order_id": "nunique",
    "payment_value": "sum",
}).sort_values(by="payment_value", ascending=False)

# Calculate no2
no2 = all_df.groupby("customer_state").agg({
    "customer_id": "nunique"
})

# Set up Seaborn for styling
sns.set(style='dark')

# Helper function to create a scatter plot
def scatter_plot(df, x_column, y_column, x_label, y_label, title):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column], color='blue', alpha=0.7)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Streamlit app
st.title("Dashboard E Commerce Public Dataset")

# Visualization 1: Scatter plot for no2
st.subheader("Visualization 1: Scatter Plot for most categorize customers based on state")
scatter_fig = scatter_plot(no2, "customer_id", "customer_id", "Number of Unique Customers", "Number of Unique Customers", "Scatter Plot for no2")
st.pyplot(scatter_fig)

# Visualization 2: Bar chart for no_1
st.subheader("Visualization 2: Bar Chart for most sold products")
bar_fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(no_1.index, no_1["order_id"], color='blue', alpha=0.7, label='Number of Unique Orders')
ax.bar(no_1.index, no_1["payment_value"], color='orange', alpha=0.7, label='Sum of Payment Value')
ax.set_xlabel('Product Category')
ax.set_ylabel('Value')
ax.set_title('Comparison of Number of Unique Orders and Sum of Payment Value by Product Category')
ax.set_xticklabels(no_1.index, rotation=45, ha='right')
ax.legend()
plt.tight_layout()
st.pyplot(bar_fig)

# Additional functionalities can be added based on your requirements
st.caption('Copyright © Siti Isyaroh 2024')