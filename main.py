# Here is a simple Streamlit app that allows you to upload an image and save it to an AWS S3 bucket. 
# This app uses the boto3 library to interact with AWS.

import streamlit as st
import boto3
from PIL import Image
import io
from datetime import datetime
import re


# AWS credentials
AWS_ACCESS_KEY_ID = st.secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = st.secrets['AWS_SECRET_ACCESS_KEY'] 
AWS_REGION_NAME = st.secrets['AWS_REGION_NAME'] 
AWS_BUCKET_NAME = st.secrets['AWS_BUCKET_NAME'] 

# Create an S3 client
s3 = boto3.client('s3', 
                  aws_access_key_id=AWS_ACCESS_KEY_ID, 
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY, 
                  region_name=AWS_REGION_NAME)

def upload_to_s3(file, image_name):
    try:
        # person name is until the first _{number}
        splitted = image_name.split('_')
        n_pic = splitted[-1].split('.')[0]
        pic_format = splitted[-1].split('.')[1]
        person_idx = splitted[-2]
        person_name = '_'.join(splitted[:-2])
        
        # person_name = image_name
        # current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        folder_name = person_name
        filename = f"{folder_name}/{image_name}"
        
        s3.upload_fileobj(file, AWS_BUCKET_NAME, filename)
        st.success(f"Successfully uploaded {filename} to S3")
    except Exception as e:
        st.error(f"Failed to upload {person_name} to S3: {e}")

def check_format(s):
    # pattern = re.compile("^[a-zA-Z]+_[a-zA-Z]+_[0-9]+_[0-9]+$")
    pattern = re.compile("^([a-zA-Z]+_)+[a-zA-Z]+_[0-9]+_[0-9]+(\.[a-zA-Z]+)?$")

    if pattern.match(s):
        return True
    else:
        return False

def main():
    st.title("העלאת תמונות: כחול")

    image_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
    image_name = st.text_input("הקלד את שם התמונה:", value=image_file.name if image_file else '')
    
    # enfoce format of image name, if there is space in image, streamlit error
    if not check_format(image_name):
        st.error('פורמט שגוי. צריך להיות:    frstname_lastname_id_number')
    else:
        image_name = image_name.lower()
        if image_name and '.' not in image_name:
            image_name += '.png'
            

        if image_file and image_name:
            image = Image.open(image_file)
            # show the image in small size
            # st.image(image, caption='Uploaded Image.', use_column_width=True)
            st.image(image, caption='Uploaded Image.', use_column_width=False, width=300)

            # add an option to rotate the image file
            # if st.button('Rotate'):
            #     image = image.rotate(90)
            #     # st.image(image, caption='Uploaded Image.', use_column_width=True)
            #     st.image(image, caption='Uploaded Image.', use_column_width=False, width=300)
            
            if st.button("העלה תמונה"):
                # Convert the image to bytes
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()

                # Upload to S3
                upload_to_s3(io.BytesIO(img_byte_arr), image_name)

if __name__ == "__main__":
    main()
