import streamlit as st
import joblib
import pandas as pd


model = joblib.load(r'Q:\\Project\\Salary Pred\\rfsalary.joblib')

st.title('Salary Prediction')

age = st.slider('Age : ',
                min_value=5,
                max_value=120,
                value=25
                )
Education_level = st.radio('Education Level : ',options=['High School','Bachelor','Master','PhD'])

edu_map = {
    'High School' : 3,
    'Bachelor' : 2 ,
    'Master' : 1 ,
    'PhD' : 0
}


Years_of_Experience = st.number_input('Years Of Experience : ',
                                       min_value=0,
                                       max_value=60,
                                        value=25)
gender = st.selectbox('Gender : ',options=['Male','Female','Other'])



job_title  = st.selectbox('Job Title : ',['Data Analyst', 'Data Scientist',
       'Director of Marketing', 'Financial Manager',
       'Front end Developer', 'Full Stack Engineer',
       'Human Resources Manager', 'Junior Sales Associate',
       'Marketing Analyst', 'Marketing Coordinator',
       'Marketing Manager', 'Operations Manager',
       'Other', 'Product Manager',
       'Senior Project Engineer',
       'Senior Software Engineer', 'Software Developer',
       'Software Engineer', 'Software Engineer Manager',
       'Web Developer'])


gender_dic = {
    'Gender_Male' : 0,
     'Gender_Other' : 0
}
gender_dic[f'Gender_{gender}'] = 1


job_dic = {
       'Age' : age ,
       'Education Level' : [edu_map[Education_level]],
       'Years of Experience' : [Years_of_Experience],
       'Gender_Male' : [gender_dic['Gender_Male']] ,
       'Gender_Other' : [gender_dic['Gender_Other']],
       'Job Title_Data Analyst' : [0],
       'Job Title_Data Scientist' : [0],
       'Job Title_Director of Marketing' : [0],
       'Job Title_Financial Manager' : [0],
       'Job Title_Front end Developer' : [0], 
       'Job Title_Full Stack Engineer' : [0],
       'Job Title_Human Resources Manager' : [0],
       'Job Title_Junior Sales Associate' : [0],
       'Job Title_Marketing Analyst' : [0] , 
       'Job Title_Marketing Coordinator' : [0],
       'Job Title_Marketing Manager' : [0], 
       'Job Title_Operations Manager' : [0],
       'Job Title_Other' : [0],
       'Job Title_Product Manager' : [0],
       'Job Title_Senior Project Engineer' : [0],
       'Job Title_Senior Software Engineer' : [0],
       'Job Title_Software Developer' : [0],
       'Job Title_Software Engineer' : [0], 
       'Job Title_Software Engineer Manager' : [0],
       'Job Title_Web Developer' : [0]
}
job_dic[f'Job Title_{job_title}'] = 1



df = pd.DataFrame(job_dic)

if st.button('Predict'):
    val = model.predict(df)
    st.markdown(f"""<b style='color:yellow;
                    border-radius:5px;
                       background-color:black;
                '>&nbsp;{val[0]:.0f}&nbsp; </b>""", unsafe_allow_html=True)
    st.warning('Note : AI can Make Mistake')