import streamlit as st

st.set_page_config(
    page_title="Diet Recommendation System by Smit Bangare",
    page_icon="👋",
)

st.write("# Welcome to Diet Recommendation System! 👋")
st.write("### Developed by Smit Bangare")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    A diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
    You can find more details and the whole project on my [repo](https://github.com/SmitBangare/Diet-Reccomendation-System-for-Healthy-Lifestyle).
    """
)

# Add footer with your details
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p>© 2024 Smit Bangare | Diet Recommendation System</p>
        <p>Contact: [Your Contact Information]</p>
    </div>
    """, 
    unsafe_allow_html=True
)
