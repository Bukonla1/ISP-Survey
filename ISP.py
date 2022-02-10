import streamlit as st
from PIL import Image

img = Image.open("isp.png")

st.image(img, width=500)

st.title("Internet Service Provider Survey")

st.header("How good is your internet?")

st.subheader("please answer the following questions")

st.text("How long have you been using the internet?")

st.success("Success")

if st.checkbox("Select/Unselect"):
    st.text("Selection Ready")
    
status = st.radio("Select internet: ", ('0-2 years', 'Above 2 years'))

if status == '0-2 years':
    st.success("0-2 years")
else:
    st.success("Above 2 years")   
    
internet = st.selectbox("Select internet: ",
                     ['MTN', 'GLO', 'Airtel'])

st.write("You have selected: ", internet)
                  
                  
st.text("Are you satisfied with your current internet service provider?")

st.success("Success")

if st.checkbox("Select/Unselect"):
    st.text("Selection Ready")
    
status = st.radio("Select answer: ", ('YES', 'NO'))

if (status == 'YES'):
    st.success("YES")
else:
    st.success("NO")   
    
speed = st.selectbox("Select speed: ",
                     ['Slow', 'Fast', 'Very Fast'])

st.write("You have selected: ", speed)               
                                  

name = st.text_input("Enter Your name", "Type Here ...")

if(st.button('Submit')):
    result = name.title()
    st.success(result)
    
level = st.slider("How Satisfied are you on a Scale of 5?", 1, 5)

st.text('Selected: {}'.format(level))


 
 