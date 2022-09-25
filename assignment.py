import pandas as pd 
import streamlit as st 
import numpy as np 
import plotly.express as px 
st.title('Unemployment rate around the world')

st.markdown('# Main page')
st.sidebar.markdown('# Main page')

st.sidebar.radio('Pick your gender',['Male','Female'])
st.sidebar.radio('Married',['Yes','No'])
st.sidebar.radio('Employed',['Yes','No'])
st.sidebar.radio('Educatiion',['Graduate','Not Graduate'])
st.sidebar.text_input('Email address')
st.sidebar.date_input('DATE')




        

df = pd.read_csv('output.csv.zip')
df_State = df.groupby(["State"], as_index=False)["Rate"].mean()
df_State.head()
st.header('Bar chart')
fig=px.bar(df_State, x = "State", y="Rate", title = "Rate by State", color = "State")
st.plotly_chart(fig, use_container_width=False)
st.caption('This is a bar chart representing the unemployment rate of each state ')




start_color, end_color = st.select_slider(
    'Select the dominant range of color',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


option= st.selectbox(
        'what state has the highest rate?',
        ['Arizona', 'Alabama', 'California','Arkansas']
    )
st.write('You selected' , option)

df_Month = df.groupby(["Month"], as_index = False)["Rate"].mean()

st.subheader('Unemployment rate by month')
fig1 = px.bar(df_Month, x = "Month", y = "Rate")
fig1.update_xaxes(categoryorder = 'array', categoryarray = ["January",'February','March','April','May','June','July','August','September','October','November','December'])
st.plotly_chart(fig1)
st.caption('This is a bar chart representing the unemployment rate by month')

option= st.selectbox(
        'what month has the highest rate?',
        ['January','March','December']
    )
st.write('You selected' , option)

df_Mis = df[df["State"]=="Mississippi"]
fig3=px.box(df_Mis, x = "Rate")
st.plotly_chart(fig3)

df_alabama = df[df["State"]=="Alabama"]
df_alabama_1= df_alabama.drop(columns=['County', 'Month'])
fig4=px.scatter(df_alabama_1, x="Year",y="Rate", title="Unemployment Rate in Alabama overtime")
st.plotly_chart(fig4)

fig5 = px.pie(df_State, values='Rate', names='State', title= ' Rate of Unemployment per State')
st.plotly_chart(fig5)

st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
