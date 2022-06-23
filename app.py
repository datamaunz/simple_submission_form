import streamlit as st

def main():
    st.set_page_config(
    layout="wide",
    page_title="Test",
    page_icon = "🦉")
    
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