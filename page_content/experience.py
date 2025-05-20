import streamlit as st

def experience_page():
    st.markdown("## Work Experience")
    
    st.markdown("""
    ### Marchandising Intern
    **DFS Group, Department of Fashion Planning ** | *May 2025 - Present*
    
    - Analyzed customer data to identify patterns and trends using Python and SQL
    - Developed a machine learning model to predict customer churn with 85% accuracy
    - Created interactive dashboards using Tableau to visualize key performance indicators
    - Presented findings and recommendations to senior management
    """)
    
    st.markdown("""
    ### Junior Brand Manager
    **PepsiCo Inc (Fuzhou Branch)** | *May 2022 - Jul. 2023*
    
    - Responsible for strategic branding, sales analysis,  inventory tracking, and new product launch planning for multiple non-carbonated beverage brands such as energy drinks (Gatorade) and fruit juices (Tropicana)
    - Communicated with sales managers, identified the factors influencing sales, developed targeted strategies; conducted market research on competitors; organized promotional activities
    - Achieved an average sales attainment rate exceeding 105% across all non-carbonated beverage brands, with Aquafina (bottled water) surging 65% and Gatorade growing 34% year-over-year
    """)
    
    st.markdown("""
    ### Product Planning Trainee
    **Xtep Co., Footwear Division** | *Jul. 2021 - Jan. 2022*
    
    - Conducted market research & data analysis to determine product positioning, identifying opportunities for growth; drafted business plans
    - Coordinated product training for seasonal buying sessions through cross-departmental collaboration, while implementing visual merchandising strategies to elevate display impact and drive wholesale buyers’ engagement
    - Devised product storytelling, collaborated with designers on new product designs (140-150 per year);  highest single-item sales volume: 2,800 pairs (a limited edition for Chinese Valentine’s Day)
    """)
    
    st.markdown("""
    ### Operation Intern
    **Poizon, Department of Promotion & Event** | *Mar. 2021 - May 2021*
    
    - Built 120 online sports apparel event venues (categorized by clothing type), created 270 themes and rankings, achieved a maximum conversion rate of 2.7%
    - Responsible for clothing category selection, applied data analysis tools such as Excel functions like Pivot Table and VLOOKUP for quantitative analysis
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Customer Segmentation Analysis",
            "description": "Used K-means clustering to segment customers based on purchasing behavior.",
            "skills": ["Python", "scikit-learn", "Pandas", "Matplotlib"],
            "outcome": "Identified 5 distinct customer segments that informed targeted marketing campaigns."
        },
        {
            "title": "Predictive Maintenance System",
            "description": "Developed a model to predict equipment failures before they occur.",
            "skills": ["Python", "TensorFlow", "Time Series Analysis", "IoT"],
            "outcome": "Reduced downtime by 23% and maintenance costs by 15%."
        },
        {
            "title": "Natural Language Processing for Customer Support",
            "description": "Created a text classification system to automatically categorize customer support tickets.",
            "skills": ["Python", "NLTK", "spaCy", "BERT"],
            "outcome": "Improved response time by 35% and increased customer satisfaction scores."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # 移除交互式图表部分
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, JavaScript
        - **Machine Learning:** scikit-learn, TensorFlow, PyTorch
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** AWS, Azure, Google Cloud
        - **Web Development:** Django, Flask, React
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---")
