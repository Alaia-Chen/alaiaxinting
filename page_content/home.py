import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Alaia Chen</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        KAK TIN STREET, SHATIN, NEW TERRITORIES, HK<br>
        <a href="mailto:alaiachen0703@gmail.com">alaiachen0703@gmail.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        Marketing specialist with experience across FMCG, fashion, and e-commerce, currently pursuing a Master’s in Marketing at The Chinese University of Hong Kong. I have a strong background in brand strategy, market research, data analytics, and product planning, with a proven track record of driving sales growth and optimizing brand positioning. I am passionate about leveraging data-driven insights to create impactful marketing strategies and staying ahead of consumer trends. 

        Particularly interested in fashion, beauty, and lifestyle industries, I am actively seeking internship and job opportunities. Happy to connect and exchange ideas!
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Machine Learning: Scikit-learn, TensorFlow, Keras
        - Data Visualization: Tableau, Power BI
        - Statistical Analysis: Hypothesis Testing, Regression Analysis
        - MS Office software: PowerPoint, Excel(VLOOKUP & Pivot Table), Outllok
        - Communication: Presentation Skills, Technical Writing
        - Languages: Mandarin (Native), English (Fluent), Cantonese (Basic)
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 
