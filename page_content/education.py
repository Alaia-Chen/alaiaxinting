import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing
    **The Chinese University of Hong Kong** | *Aug. 2024 - Jul. 2025*
    
    - GPA: 3.6/4.0
    - Core Courses: ·Marketing Management, Marketing Research, Digital Marketing, Big Data Strategy, Marketing Analytics, Customer Analytics, Social Media Analytics, Machine Learning in Marketing
    
    ### Bachelor of Engineering in Fashion Design and Engineering
    **Donghua University** | *Sep. 2017 - Jun. 2021*
    
    - GPA: 3.5/4.0
    - Core Courses: Multimedia Application System Technology, Fashion Industry, Applied Management, Fashion Market Research, Methods and Application of Data Analysis, Advanced Mathematics
    - Honor: Academic Excellence Award (2018), DHU Exchange Student Scholarship (2020)
    """)

    ### Exchange Program in Fashion Marketing
    **Fu Jen Catholic University** | *Sep. 2019 - Jan. 2020*
    
    - GPA: 92/100
    - Core Courses: Management, Social Psychology of Dress, Fashion Store Management, Strategic Fashion Brand Management, Apparel Logistics and Management
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### AWS Certified Data Analytics - Specialty
        **Amazon Web Services** | *March 2022*
        
        Demonstrated expertise in designing, building, securing, and maintaining analytics solutions on AWS.
        """)
        
    with cert2:
        st.markdown("""
        ### TensorFlow Developer Certificate
        **Google** | *January 2022*
        
        Validated ability to develop deep learning models using TensorFlow.
        """)
        
    with cert3:
        st.markdown("""
        ### Microsoft Certified: Azure Data Scientist Associate
        **Microsoft** | *November 2021*
        
        Demonstrated expertise in using Azure services to train, evaluate, and deploy machine learning models.
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### Sentiment Analysis of Product Reviews
    - Developed a deep learning model to analyze customer reviews and predict sentiment
    - Achieved 92% accuracy using BERT and fine-tuning techniques
    - Implemented the model as a web application using Flask
    
    ### Image Classification for Medical Diagnosis
    - Created a convolutional neural network to classify medical images
    - Worked with a dataset of X-ray images to detect pneumonia
    - Achieved 88% accuracy and deployed the model on a cloud platform
    """)
    
    st.markdown("---") 
