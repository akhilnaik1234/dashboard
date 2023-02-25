import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
from PIL import Image


st.title(":green[IRIS DASHBOARD]")

image = Image.open(r'C:\Users\Administrator\Desktop\ds_internship\proj_3\resources\images\iris.jpg')

st.image(image, caption='image ')


df = pd.read_csv(r'C:\Users\Administrator\Desktop\ds_internship\proj_3\resources\data\iris.csv')
st.dataframe(df)


species = st.selectbox("Select the Species:", df['Species'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Species'] == species], x="SepalLengthCm")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Species'] == species], y="SepalLengthCm")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.bar(df[df['Species'] == species], y="SepalLengthCm")
st.plotly_chart(fig_3, use_container_width=True)

