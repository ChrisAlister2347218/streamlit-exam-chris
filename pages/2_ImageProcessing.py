from PIL import Image
import streamlit as st

def app():
    st.subheader("Image Processing")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Original Image', use_column_width=True)

        option = st.selectbox("Select an image processing technique", ("Resize", "Grayscale", "Conversion", "Image Cropping", "Image Rotation"))

        if option == "Resize":
            width = st.slider("Width", min_value=100, max_value=1000, value=500, step=50)
            height = st.slider("Height", min_value=100, max_value=1000, value=500, step=50)
            resized_image = image.resize((width, height))
            st.image(resized_image, caption='Resized Image', use_column_width=True)

        elif option == "Grayscale":
            grayscale_image = image.convert('L')
            st.image(grayscale_image, caption='Grayscale Image', use_column_width=True)

        elif option == "Conversion":
            conversion_type = st.selectbox("Select conversion type", ("RGB", "RGBA", "CMYK"))
            converted_image = image.convert(conversion_type)
            st.image(converted_image, caption=f'Converted Image ({conversion_type})', use_column_width=True)

        elif option == "Image Cropping":
            left = st.slider("Left", min_value=0, max_value=image.width, value=0)
            top = st.slider("Top", min_value=0, max_value=image.height, value=0)
            right = st.slider("Right", min_value=0, max_value=image.width, value=image.width)
            bottom = st.slider("Bottom", min_value=0, max_value=image.height, value=image.height)
            cropped_image = image.crop((left, top, right, bottom))
            st.image(cropped_image, caption='Cropped Image', use_column_width=True)

        elif option == "Image Rotation":
            angle = st.slider("Rotation Angle", min_value=-360, max_value=360, value=0, step=5)
            rotated_image = image.rotate(angle, expand=True)
            st.image(rotated_image, caption='Rotated Image', use_column_width=True)

if __name__ == "__main__":
    app()