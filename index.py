import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Md Arshad Hussain | Portfolio",
    page_icon="💻",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "About", "Skills", "Projects", "Education", "Contact"]
)


# ---------------- HOME ----------------
if page == "Home":

    st.write("""
    Welcome to my Portfolio Website.

    """)

    st.title("Md Arshad Hussain")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Projects","1+")

    with col2:
        st.metric("Programming Languages:", "Python , C")

# ---------------- ABOUT ----------------

elif page == "About":

    st.header("About Me")

    st.write("""
Hello!

I am **Md Arshad Hussain**, currently pursuing B.Tech in Computer Science
(Data Science).
             
I enjoy solving real-world problems using Python, SQL,
Machine Learning and Data Analytics.

My career goal is to become a Data Analyst/Data Scientist
at leading companies.
""")

# ---------------- SKILLS ----------------

elif page == "Skills":

    st.header("Technical Skills")

    st.subheader("Programming")

    st.progress(90)
    st.write("Python")

    st.progress(80)
    st.write("C")

    st.subheader("Libraries")

    st.write("""
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
""")

    st.subheader("Tools")

    st.write("""
- Jupyter Notebook
- VS Code
""")

# ---------------- PROJECTS ----------------

elif page == "Projects":

    st.header("Project")

    st.success("🎓 Student Performance Prediction")

    st.write("""
Built a Machine Learning model to predict student performance.

Technologies:
- Python
- Pandas
- Scikit-Learn
- Matplotlib
""")

# ---------------- EDUCATION ----------------

elif page == "Education":

    st.header("Education")

    st.write("""
### B.Tech (Computer Science & Engineering - Data Science)

College:
Narula Institute of Technology

Graduate in :
2028
""")

    st.write("""
### I have compeleted Class XII from the 
             
CBSE Board
             
""")

    st.write("""
### I have compeleted Class X from the 

CBSE Board
""")

# ---------------- CONTACT ----------------

elif page == "Contact":

    st.header("Contact Me")

    name = st.text_input("Your Name")

    email = st.text_input("Email")

    message = st.text_area("Message")

    if st.button("Send"):
        st.success("Thank you! Your message has been received.")

    st.write("---")

    st.write("📧 Email: mdarshadhussain04@gmail.com")
    st.write("💼 LinkedIn: https://linkedin.com/in/MdArshadHussain")
    st.write("💻 GitHub: https://github.com/arshad")