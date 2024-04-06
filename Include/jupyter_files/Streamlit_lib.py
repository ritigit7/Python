import time
import streamlit as st

# st.checkbox('yes')
# st.button('Click')
# st.radio('Pick your gender',['Male','Female'])
# st.selectbox('Pick your gender',['Male','Female'])
# st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
# st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
# st.slider('Pick a number', 0,50)



# st.balloons()
# st.progress(10)
# with st.spinner('Wait for it...'):
#         time.sleep(10)


import streamlit as stimport
import matplotlib.pyplot as plt 
import numpy as np
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)