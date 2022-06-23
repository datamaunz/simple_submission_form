import streamlit as st

def main():
    st.set_page_config(
    layout="wide",
    page_title="Test",
    page_icon = "🦉")
    
    # logos
    
    col1, col2 = st.columns(2)
    #col1.image("https://www.principia-advisory.com/wp-content/themes/principia/assets/images/Principia_logo_@2x.png", width=100)
    
    col1.markdown("<img align='left' width='20%' src='https://www.principia-advisory.com/wp-content/themes/principia/assets/images/Principia_logo_@2x.png'>", unsafe_allow_html=True)
    col2.markdown("<img align='right' width='20%' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/150px-Google_%22G%22_Logo.svg.png'>", unsafe_allow_html=True)
    
    # questions
    
    st.markdown("""## Responsible Innovation Best Practice Collector""")
    st.markdown("""---""")
    
    practice = st.text_area("Please describe the practice?", value="")
    why_best_practice = st.text_area("What makes this practice a best practice?", value="")
    where_can_we_learn_more  = st.text_input("Where can we learn more about this?", value="")
    email = st.text_input("Please leave your email address", value="")
    
    
    submit_button = st.button("Submit")
    if submit_button == True:
        st.write(practice, why_best_practice, where_can_we_learn_more, email)

if __name__ == '__main__':
    main()