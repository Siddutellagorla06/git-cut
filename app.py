import streamlit as st 
import numpy as np 
import pandas as pd
import joblib 
model = joblib.load("student_performance_model.h5")

def predict_marks(Hours_Studied,Previous_Scores,Extracurricular_Activities,Sleep_Hours,Sample_Question_Papers_Practiced):
    input_data = np.array([[Hours_Studied,Previous_Scores,Extracurricular_Activities,Sleep_Hours,Sample_Question_Papers_Practiced]])
    predictions = model.predict(input_data)
    return predictions


def main():
    st.title("Student Marks Predictor")
    __name__= st.text_input("Enter your name")
    Hours_Studied = st.number_input("Enter the number of hours you studied")
    Previous_Scores = st.number_input("Enter your previous score")
    Extracurricular_Activities = st.number_input("Enter the extra activities you have done")
    Sleep_Hours = st.number_input("Enter number of hours you slept")
    Sample_Question_Papers_Practiced = st.number_input("Enter number of sample question paper you practiced")

    if st.button("Predict Marks"):
        result = predict_marks(Hours_Studied,Previous_Scores,Extracurricular_Activities,Sleep_Hours,Sample_Question_Papers_Practiced)
        if result >= 80:
            st.success("Congratulations, you have high chances of passing")
        elif result >= 60:
            st.warning("You are likely to pass with 1 class there is a room for improvement")  
        elif result >= 35:
            st.warning("You need to hardwork") 
        else:
            st.error("You are going to fail")       

if __name__ == "__main__":
    main()    
