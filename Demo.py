import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('train.csv')

# Display text
st.title('My Passion')
st.header('Coding world')
st.subheader('The first time I deploy my app')

menu = ['Display Text', 'Display Data', 'Display Chart', 'Display Interactive Widget']

choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Display Text':
    
    st.text('The page aim to display my thinking and coding for relaxing and improving coding skill')
    st.markdown('There were 5 topics: ')
    st.write("""
    - Topic 1
    - Topic 2
    - ...""")
    st.write("### Programming language: Python")
    st.code('st.display_text_function("Content")', language='python')

elif choice == 'Display Data':
    st.write("## Display Data")
    st.markdown('DataFrame:')
    st.dataframe(data.head(3))
    st.markdown('Table:')
    st.table(data.head(3))
    st.markdown('Json:')
    st.json(data.head(2).to_json())
elif choice == 'Display Chart':
    
    st.write("## Display Chart")
    count_Pclass = data[['PassengerId', 'Pclass']].groupby(['Pclass']).count()
    st.bar_chart(count_Pclass)

    fig, ax = plt.subplots()
    ax = sns.boxplot(x='Pclass', y = 'Fare', data = data)
    st.pyplot(fig)

else:
    st.write("## Display Interactive Widget")
    st.write("### Input your information")
    name = st.text_input('Name: ')
    sex = st.radio('Sex', options= ['Male', 'Female'])
    age = st.slider('Age', 1, 100, 1)
    jobtime = st.selectbox('You have', options=['Part time job', 'Full time job'])
    hobbies = st.multiselect('Hobbies', options=['Cooking', 'Reading', 'Writing', 'Travel', 'Others'])
    house = st.checkbox('have house/apartment')
    submit = st.button('Submit')

    if submit:
        st.write("### Your Information: ")
        st.write("Name:", name,
        "- Sex:", sex,
        "- Age:", age,
        "- You have a", jobtime,
        "and a house/apartment" if house else ""
        "- Hobbies:", ', '.join(map(str, hobbies)))