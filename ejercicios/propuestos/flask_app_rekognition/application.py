"""
Nombre del programa:
Descripción:
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 20/1/23
"""
import base64
from flask import Flask, request, abort, Response
from api.detect_faces import detect_faces
from api.blur_faces import anonymize_face
from dotenv import load_dotenv
import os
import boto3

# Take environment variables from .env file
load_dotenv()

aws_access_key_id = os.environ.get('ACCESS_KEY_ID'),
aws_secret_access_key = os.environ.get('ACCESS_SECRET_KEY')
src_bucket_name = os.environ.get('SRC_BUCKET_NAME')
dst_bucket_name = os.environ.get('DST_BUCKET_NAME')

s3 = boto3.Session(
    aws_access_key_id=os.environ.get(str(aws_access_key_id)),
    aws_secret_access_key=os.environ.get(aws_secret_access_key)).resource('s3')

application = Flask(__name__)


@application.route('/api/analyze', methods=['POST'])
def analyzeImage():
    key = request.get_json()['key']
    if key is None:
        abort(400)

    try:
        response = detect_faces(key)

        fileObject = s3.Object(src_bucket_name, key).get()
        fileContent = fileObject['Body'].read()
        buffer_anon_img = anonymize_face(fileContent, response)

        img_enc = base64.b64encode(buffer_anon_img)
        img_dec = base64.b64decode(img_enc)
        s3.Object(dst_bucket_name, f"result_{key}").put(Body=img_dec)
    except Exception as error:
        print(error)
        abort(500)
    return Response(status=200)


# Run the app
if __name__ == "__main__":
    application.debug = True
    application.run()
