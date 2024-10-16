import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
from pandas.api.types import is_numeric_dtype

#title
st.title('Data Analysis App')
st.write('Application for data analysis')
st.write('''
Testing
Something
         ''')
#google marcdown specs
st.header('Data')
st.header('a header with _italic_ :blue[colors] and b**old** text and emoji! :sunglasses:')

st.markdown('Srteanlit can use **_markdown_**')
st.markdown('this text :red[colored red] and this is **:blue[colored blue]** and bold')

st.markdown(':green[$\sqrt{x^2+y^2}=1$] is Piphagorals theorem :smile:')

st.write('Adding widget is the same as declaring variables, no need for backend, routes, requests etc.')

file= st.file_uploader('upload file in csv or excel', type=['scv', 'xlsx'])

if file is not None:
#     try:
#         df= pd.read_csv(file)
#         st.header(file.name)
#         st.dataframe(df)
#     except:
#         df=pd.read_excel(file)
#         st.header(file.name)
#         st.dataframe(df)
#     try:
#         df2=pd.DataFrame(df.groupby('STATION').mean())
#         st.map(df)
#     except:
#         pass



    try:
        df = pd.read_csv(file, parse_dates=['Time'])

        start_date, end_date = st.select_slider(
        'Select a time range',
        options=list(df['Time']),
        value=(df['Time'].min(), df['Time'].max()))

        mask = (df['Time'] > start_date) & (df['Time'] <= end_date)

        st.line_chart(df.loc[mask], x="Time", y="Price")
    except Exception as e:
        st.write(e)

    


    
  