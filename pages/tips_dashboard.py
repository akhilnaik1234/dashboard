import streamlit as st
from matplotlib import image
import os
from PIL import Image
import pandas as pd
import plotly.express as px

st.title(":blue[Tips Dashboard]")

image = Image.open(r'C:\Users\Administrator\Desktop\ds_internship\proj_3\resources\images\tips.jpg')

st.image(image, caption='image ')

df = pd.read_csv(r'C:\Users\Administrator\Desktop\ds_internship\proj_3\resources\data\tips.csv')
st.dataframe(df)

day = st.selectbox("Select the day:", df['day'].unique())

fig_1 = px.histogram(df[df['day'] == day], x="tip")
st.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.violin(df[df['day'] == day], x="tip")
st.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.bar(df[df['day'] == day], x="total_bill")
st.plotly_chart(fig_3, use_container_width=True)
