"""
Nombre del programa:
Descripción:
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 20/1/23
"""
import boto3
from dotenv import load_dotenv
import os

# Take environment variables from .env file
load_dotenv()
src_bucket_name = os.environ.get('SRC_BUCKET_NAME')

# Create the service Polly and assign credentials
rekognition_client = boto3.Session(
    aws_access_key_id=os.environ.get('ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('ACCESS_SECRET_KEY'),
    aws_session_token=os.environ.get('SESSION_TOKEN'),
    region_name=os.environ.get('REGION')).client('rekognition')


def detect_faces(img):
    try:

        response = rekognition_client.detect_faces(
            Image={'S3Object': {
                'Bucket': f'{src_bucket_name}',
                'Name': f'{img}'}
                   }, Attributes=['DEFAULT']
        )
        print("Image task recognition has been successfully run")
    except:
        raise Exception("An unexpected error was raised recognizing an image")

    return response
