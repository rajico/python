"""
Nombre del programa:
Descripción:
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 20/1/23
"""
import cv2 as cv
import numpy as np


def anonymize_face(buffer, response):
    # Read image from buffer
    nparr = np.fromstring(buffer, np.uint8)
    img = cv.imdecode(nparr, cv.IMREAD_COLOR)
    height, width, _ = img.shape

    for faceDetail in response['FaceDetails']:
        box = faceDetail['BoundingBox']
        x = int(width * box['Left'])
        y = int(height * box['Top'])
        w = int(width * box['Width'])
        h = int(height * box['Height'])

        roi = img[y:y+h, x:x+w]

        roi = cv.GaussianBlur(roi, (83, 83), 30)

        img[y:y+roi.shape[0], x:x+roi.shape[1]] = roi

    _, res_buffer = cv.imencode('.jpg', img)

    return res_buffer
