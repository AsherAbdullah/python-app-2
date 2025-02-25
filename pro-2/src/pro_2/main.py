import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from PIL import Image
import cv2

# Initialize Streamlit App
def main():
    st.set_page_config(page_title="Best Way to Build Python Apps", layout="wide")
    st.title("🚀 The Best Way to Build Python Apps with Streamlit and UV")
    st.sidebar.title("Navigation")
    
    menu = ["Home", "Data Visualization", "Image Processing", "Map Integration", "Data Analytics"]
    choice = st.sidebar.radio("Select a page", menu)
    
    if choice == "Home":
        home_page()
    elif choice == "Data Visualization":
        data_visualization()
    elif choice == "Image Processing":
        image_processing()
    elif choice == "Map Integration":
        map_integration()
    elif choice == "Data Analytics":
        data_analytics()

def home_page():
    st.write("Welcome to the **Best Way to Build Python Apps** using **Streamlit** and **UV**.")
    st.write("""
    - 🌟 Easy to build web applications with Python
    - 📊 Interactive data visualizations
    - 🖼️ Advanced image processing
    - 🗺️ Map integration for geospatial applications
    - 📈 Data analytics for deeper insights
    """)

def data_visualization():
    st.header("📊 Data Visualization")
    df = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["A", "B", "C"]
    )
    st.line_chart(df)

def image_processing():
    st.header("🖼️ Image Processing with OpenCV")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Convert to Grayscale"):
            img_array = np.array(image)
            gray_image = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            st.image(gray_image, caption="Grayscale Image", use_column_width=True, clamp=True)

def map_integration():
    st.header("🗺️ Map Integration with Folium")
    m = folium.Map(location=[30.3753, 69.3451], zoom_start=6)
    folium.Marker([31.5497, 74.3436], popup="Lahore", icon=folium.Icon(color='blue')).add_to(m)
    folium.Marker([24.8607, 67.0011], popup="Karachi", icon=folium.Icon(color='red')).add_to(m)
    folium_static(m)

def data_analytics():
    st.header("📈 Data Analytics with Streamlit")
    df = pd.DataFrame(
        np.random.randn(100, 4),
        columns=["Feature 1", "Feature 2", "Feature 3", "Feature 4"]
    )
    st.write("### Data Overview")
    st.write(df.head())
    st.write("### Summary Statistics")
    st.write(df.describe())
    st.write("### Correlation Heatmap")
    st.bar_chart(df.corr())

if __name__ == "__main__":
    main()
