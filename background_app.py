import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64
import os

st.set_page_config(layout="wide", page_title="Image Background Remover")

# About Me Section
st.sidebar.header("About the Developer 👨‍💻")
st.sidebar.markdown("👨‍💻 I am a diligent data analyst with a fervent interest in crafting web applications and delving into pioneering projects. My dedication to the field is evident through a robust commitment to data analysis and a constant pursuit of innovative solutions.")

# urls of the images
github_url = "https://img.icons8.com/fluent/48/000000/github.png"
twitter_url = "https://img.icons8.com/color/48/000000/twitter.png"
linkedin_url = "https://images.app.goo.gl/NFb4BsYNbd8t3L9Y9"

# redirect urls
github_redirect_url = "https://github.com/Zeeshan5932/background_remover"
twitter_redirect_url = "https://x.com/S_H_A_N_I18?t=kPSSnXrNh3T8pbvktN9Sgg&s=09"
linkedin_redirect_url = "https://www.linkedin.com/in/zeeshan-younas-919a09253/"

# adding a footer
st.sidebar.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0; 
    width: 100%;
    background-color: #f5f5f5;
    color: #000000;
    text-align: center;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)


st.write("Remove background from your image")
st.write(
    ":🐶: Try uploading an image to watch the background magically removed. Full quality images can be downloaded from the sidebar. This code is open source and available [here](https://github.com/Zeeshan5932/background_remover) on GitHub. Special thanks to the [rembg library](https://github.com/danielgatis/rembg) :grin:"
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 48 * 1024 * 1024  

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("./Zebra.jpg")



st.markdown(f'<div class="footer">Made with ❤️ by Zeeshan Younas<a href="{github_redirect_url}"><img src="{github_url}" width="30" height="30"></a>'
             f'<a href="{twitter_redirect_url}"><img src="{twitter_url}" width="30" height="30"></a>'
             f'<a href="{linkedin_redirect_url}"><img src="{linkedin_url}" width="30" height="30"></a> | Credits: Dr.Ammaar Tufail</div>', unsafe_allow_html=True)
