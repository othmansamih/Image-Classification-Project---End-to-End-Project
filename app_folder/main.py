import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

st.title("End to End Image Classification project")

classes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/Trained model/trained_model.h5"
print(model_path)
model = tf.keras.models.load_model(model_path)

uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col1, col2 = st.columns(2)

    with col1:
        img = Image.open(uploaded_file)
        st.image(img, caption="uploaded image", use_column_width=True)

    with col2:
        if st.button("Classify", use_container_width=True):
            resized_img = img.resize((28,28))
            grayscale_img = resized_img.convert('L')
            final_img = np.array(grayscale_img).reshape((1,28,28,1))
            final_img = final_img/255
            prediction = model.predict(final_img)
            pred_class = classes[np.argmax(prediction)]

            st.success(f"The predicted class is: {pred_class}")