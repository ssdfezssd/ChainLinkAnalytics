

# Contents of ~/my_app/streamlit_app.py
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
import plotly.express as px
import numpy as np
import time




# Displaying images on the front end
image = Image.open('images/DeltaPacific_Logo.jpg')
st.image(image, width=200)




col1, col2 = st.columns([2, 1])
with col1:
    st.write("<span style='font-size: 24px;'>Delta Pacific Beverage Co.</span>", unsafe_allow_html=True)
with col2:
    st.write('')



  
st.header("Manage Chain Resets and Gap Analysis")


# Load data
df = px.data.gapminder()
df = df[(df['continent']=='Asia') & (df['year'] >= 1932) & (df['year'] <= 2007)]

# Create animated chart using Plotly
fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='country', log_x=True, hover_name='country', animation_frame='year', range_x=[200, 100000], range_y=[20, 90])

# Create a container for the chart
chart_container = st.container()

# Display the chart in the container
with chart_container:
    chart = st.plotly_chart(fig, use_container_width=True)

# Animate the chart for 5 seconds
end_time = time.time() + 5
while time.time() < end_time:
    for frame in fig.frames:
        with chart_container:
            chart.plotly_chart({"data": frame.data, "layout": frame.layout})
        time.sleep(0.5)






# Add footer
st.markdown("<div style='text-align: center;'>Powered by ChainSight</div>", unsafe_allow_html=True)
