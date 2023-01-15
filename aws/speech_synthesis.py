"""
Nombre del programa:
Descripción:
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 11/1/23
"""

import boto3

# Creamos el servicio Polly y asignamos las credenciales.
# ¡IMPORTANTE! Consume tiempo de servicio.
polly_client = boto3.Session(
    aws_access_key_id="ASIARJ3ETYZUNGEATOHW",
    aws_secret_access_key="kVPlCaPHO7dqF1f0d2bZfeFilZ0B0ufKTuZw7Ssu",
    aws_session_token="FwoGZXIvYXdzEGAaDGFXGpJdqcWpQrNQ8yLAATxgK49OgsNfRQ627lPUBIM+KEFMlbdzgPoM4UBIo2CrSMNQ9aKmdxtNNJgqVKRpWAzEQc/hUGGDRuyzy06lITurmGKTiobHu93SdytHN7oUKdOYHiyqcoBWjLT23DeRUTeESNbg/5+EJSTikJcXhf+v2303mQna5JkP+4rJEAeedHVGU6gJSPfqmuTmB81FXANALmTNa19IliI4aH2f1O3iD1A8RKhU8C2ekCeF7D4wUC4Y8q1pV8ix+PrRyBP4RyjEnfudBjItWYIJGhAOsexBpo9jC/qWdPerg5BUR6cnGFMS2cwOyicjHp2i2dfmjxlk7O72",
    region_name="us-east-1").client('polly')

# Creamos los parámetros y lanzamos el servicio
try:
    response = polly_client.start_speech_synthesis_task(
        VoiceId='Lucia',
        OutputS3BucketName='ceiabd-rjc-bucket',
        OutputFormat='mp3',
        Text='¿Cualquier tecnología suficientemente avanzada es indistinguible de la magia?',
        TextType='text',
        SampleRate='22050')

    print(f"Audio file is saved into {response['SynthesisTask']['OutputUri']}")
except:
    print('Oops! An unexpected error was raised')
