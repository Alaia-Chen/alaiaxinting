import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Jane_Doe_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Alaia Chen")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** alaiachen0703@gmail.com
    - **Phone:** (852) 5957 3793
    - **LinkedIn:** [linkedin.com/in/xinting-chen-0741a832b](https://linkedin.com/in/xinting-chen-0741a832b)
    - **GitHub:** [github.com/Alaia-Chen](https://github.com/Alaia-Chen)
    - **Address:** KAK TIN STREET, SHATIN, NEW TERRITORIES
    """)

    st.header("Professional Summary")
    st.markdown("""
    Marketing specialist with experience across FMCG, fashion, and e-commerce, currently pursuing a Master’s in Marketing at The Chinese University of Hong Kong. I have a strong background in brand strategy, market research, data analytics, and product planning, with a proven track record of driving sales growth and optimizing brand positioning. I am passionate about leveraging data-driven insights to create impactful marketing strategies and staying ahead of consumer trends. 
    """)

    st.header("Work Experience")
    st.markdown("""
    **Marchandising Intern, DFS Group**
    - *May 2025 - Present*
    - Review all Master Data to ensure compliance with company standards, upon registering products in DFS
    - Liaise with Vendor for product Master Data collection, ensuring data quality is compliant with company standards
    - Execute Article listing & delisting by location in SAP, as communicated by the Merchandising group
    - Confirm successful transmission of DFS Purchase Order to external Partners
    
    **Junior Brand Manager, PepsiCo Inc**
    - *May 2022 - Jul. 2023*
    - Responsible for strategic branding, sales analysis,  inventory tracking, and new product launch planning for multiple non-carbonated beverage brands such as energy drinks (Gatorade) and fruit juices (Tropicana)
    - Communicated with sales managers, identified the factors influencing sales, developed targeted strategies; conducted market research on competitors; organized promotional activities
    - Achieved an average sales attainment rate exceeding 105% across all non-carbonated beverage brands, with Aquafina (bottled water) surging 65% and Gatorade growing 34% year-over-year
    
    **Product Planning Trainee, Xtep Co.**
    - *Jul. 2021 - Jan. 2022*
    - Conducted market research & data analysis to determine product positioning, identifying opportunities for growth; drafted business plans
    - Coordinated product training for seasonal buying sessions through cross-departmental collaboration, while implementing visual merchandising strategies to elevate display impact and drive wholesale buyers’ engagement
    - Devised product storytelling, collaborated with designers on new product designs (140-150 per year);  highest single-item sales volume: 2,800 pairs (a limited edition for Chinese Valentine’s Day)
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - The Chinese University of Hong Kong
    - *Graduated: July 2025*
    - GPA: 3.6/4.0

    **Bachelor of Engineering in Fashion Design and Engineering**
    - Donghua University
    - *Graduated: June 2021*
    - GPA: 3.5/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, JavaScript, Java, C++
    - **Web Technologies:** HTML, CSS, React, Node.js, Django
    - **Databases:** MySQL, PostgreSQL, MongoDB
    - **Tools:** Git, Docker, Jenkins, AWS
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Languages")
    st.markdown("""
    - **Mandarin:** Native
    - **English:** Fluent
    - **Cantonese:** Basic
    """)

    st.header("Interests")
    st.markdown("""
    - Citywalk
    - Photography
    - Outdoor activities
    """)

    st.markdown("---") 
