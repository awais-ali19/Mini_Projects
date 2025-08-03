import streamlit as st
from PIL import Image , ImageFilter
# create the heading
st.markdown("<h1 style='text-align: center;'> Image Editor </h1>" , unsafe_allow_html=True)
st.markdown("---")

# Upload the image
image=st.file_uploader("Upload your image" , type=["jpg" , "png"])
# Placeholder 
size=st.empty()
mode=st.empty()
format_=st.empty()

if image:
    img=Image.open(image)
    size.markdown(f"<h6>Size: {img.size}</h6>" , unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode}</h6>" , unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {img.format}</h6>" , unsafe_allow_html=True)
    # Resizing
    st.markdown("<h2 style='text-align: center;'> Resizing </h2>" , unsafe_allow_html=True)
    width=st.number_input("Width" , value=img.width)
    height=st.number_input("Height" , value=img.height)
    # Rotation
    st.markdown("<h2 style='text-align: center;'> Rotation </h2>" , unsafe_allow_html=True)
    degree=st.number_input("Degree")
    # Degree
    st.markdown("<h2 style='text-align: center;'> Filter </h2>" , unsafe_allow_html=True)
    filter_op=st.selectbox("Filters" , options=("None" , "BLUR" , "SHARPEN" , "CONTOUR" , "SMOOTH" , "EMBOSS" , "DETAIL"))
    
    s_btn = st.button("Submit")  # Submit Button
    if s_btn:
        edited=img.resize((width,height)).rotate(degree)   
        filtered=edited
        filter_map = {                 # Create a Dictionary of Filters
        "BLUR": ImageFilter.BLUR,
        "CONTOUR": ImageFilter.CONTOUR,
        "DETAIL": ImageFilter.DETAIL,
        "EMBOSS": ImageFilter.EMBOSS,
        "SHARPEN": ImageFilter.SHARPEN,
        "SMOOTH": ImageFilter.SMOOTH    }
        if filter_op != "None":
            if filter_op in filter_map:
              filtered=edited.filter(filter_map[filter_op])
        st.image(filtered)    
                         
    
    
    
    
