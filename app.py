import streamlit as st
import streamlit.components.v1 as stc

from ml_app import run_ml_app
from edu_app import run_eda_app

html_temp = """
            <div style=""> 
                <h1 style="color:white;text-align:center;">Employee Promotion Prediction App</h1>
                <h4 style="color:white;text-align:center;">This website belongs to HR Team</h4>
            </div>
            """
desc_temp = """
                ### Employee Promotion Prediction App
                This app is used by HR team to help predict whether an employee get a promotion or not
                ### App Content
                - Exploratory Data Analysis
                - Machine Learning Section
            """

def main():
    # st.title("Main App")
    stc.html(html_temp)

    menu = ["Home","EDA","Model Section"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "EDA":
        run_eda_app()
    elif choice == "Model Section":
        run_ml_app()
    

if __name__ == '__main__':
    main()

    