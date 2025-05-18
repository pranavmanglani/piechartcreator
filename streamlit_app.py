import streamlit as st
import matplotlib.pyplot as plt
import io

# Title of the app
st.title("Interactive Pie Chart Generator with Download Option")

# Instructions
st.write("Enter the categories and their corresponding values below:")

# Input fields for categories and values
categories_input = st.text_area("Enter categories (comma-separated):", "Category A, Category B, Category C")
values_input = st.text_area("Enter values (comma-separated):", "10, 20, 30")

# Convert inputs to lists
categories = [cat.strip() for cat in categories_input.split(",")]
values = [int(val.strip()) for val in values_input.split(",")]

# Check if inputs are valid
if len(categories) == len(values) and all(isinstance(val, int) for val in values):
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart
    st.pyplot(fig)

    # Save the figure to a BytesIO object
    img_bytes = io.BytesIO()
    fig.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    # Provide a download button for the image
    st.download_button(
        label="Download Pie Chart as PNG",
        data=img_bytes,
        file_name="pie_chart.png",
        mime="image/png",
        use_container_width=True
    )
else:
    st.error("Please ensure that the number of categories matches the number of values and that all values are integers.")
st.header("Created By Pranav Manglani Using Python")
