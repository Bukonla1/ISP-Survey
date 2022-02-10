import streamlit as st
from PIL import Image

img = Image.open("isp.png")

st.image(img, width=500)

st.title("Internet Service Providers Survey")

st.subheader("Please answer the following questions")

st.text("How long have you been using the internet?")
    
status = st.radio("Select year: ", ('0-2 years', 'Above 2 years'))

if status == '0-2 years':
    st.success("0-2 years")
else:
    st.success("Above 2 years")   
    
st.text("Which internet service provider do you use?")    
    
internet = st.selectbox("Select internet: ",
                     ['MTN', 'GLO', 'Airtel'])

st.write("You have selected: ", internet)
                  
                  
st.text("Would you recommend your internet service provider to your friend?")
    
status = st.radio("Select answer: ", ('YES', 'NO'))

if (status == 'YES'):
    st.success("YES")
else:
    st.success("NO")   

st.text("How fast is your internet?")
    
speed = st.selectbox("Select speed: ",
                     ['Slow', 'Fast', 'Very Fast'])

st.write("You have selected: ", speed)   

level = st.slider("How satisfied are you with your internet service provider on a scale of 1-5?", 1, 5)

st.text('Selected: {}'.format(level))

name = st.text_input("Enter Your name", "Type Here ...")                                  

if(st.button('Submit')):
    result = name.title()
    st.success(result)
    



 
 