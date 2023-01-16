"""
Nombre del programa: App web Polly (con Flask)
Descripción: Realizar una web sencilla que transforme de texto a voz usando AWS Polly.
Esta web presenta un formulario que pide un modelo de voz entre los disponibles en Polly y el texto a transformar.

El formulario se envía a una aplicación Flask que será la encargada de hacer el proceso.
En principio el mp3 se almacena en un bucket. A partir de aquí haz las mejoras que se te ocurran para facilitar
al usuario esta conversión.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 15/1/23
"""
from flask import Flask, render_template, request
import boto3
import time

polly_client = boto3.Session(
    aws_access_key_id="ASIARJ3ETYZUB2WQ3SHM",
    aws_secret_access_key="76nL+7l8ePraQnSGfEM0sFWAmFbrEu8RbIMBWdo8",
    aws_session_token="FwoGZXIvYXdzEMX//////////wEaDMTaq+EhDtbeiaROWSLAAZumPwlM47HAR"
                      "JuJZ5m7LMM6Fx1y5CufuGagtgCe8cbYAO12blzhor4Hho24DZ1jq6H1WRYHj0"
                      "2FOvOpp4oJRxZAY5MA4jTSwPwjboL1oOf/NRvkzfPBVHnSbWeAQrEisgNt8Ys"
                      "gKw+Y5B9BMTI7v45SJISZwyCXRFncN+90VP57Eham3XIYtYbWjYGQJ+5Tfci7"
                      "/OJoK5gmxzfk4viQ5YaDMsdtxbQrCQAu7L3ybX/ybhATRv759UiDWaDTGVNLg"
                      "SjFsJGeBjItk7wAMuJYGOTfWgj6e6ynLfAOlT8HnBrGvgNjkveyQBLtmeWnCOKrysRFFyDS",
    region_name="us-east-1").client('polly')
s3 = boto3.Session(
                  region_name="us-east-1",
                  aws_access_key_id="ASIARJ3ETYZUB2WQ3SHM",
                  aws_secret_access_key="76nL+7l8ePraQnSGfEM0sFWAmFbrEu8RbIMBWdo8",
                  aws_session_token="FwoGZXIvYXdzEMX//////////wEaDMTaq+EhDtbeiaROWSLAAZumPwlM47HAR"
                                    "JuJZ5m7LMM6Fx1y5CufuGagtgCe8cbYAO12blzhor4Hho24DZ1jq6H1WRYHj0"
                                    "2FOvOpp4oJRxZAY5MA4jTSwPwjboL1oOf/NRvkzfPBVHnSbWeAQrEisgNt8Ys"
                                    "gKw+Y5B9BMTI7v45SJISZwyCXRFncN+90VP57Eham3XIYtYbWjYGQJ+5Tfci7"
                                    "/OJoK5gmxzfk4viQ5YaDMsdtxbQrCQAu7L3ybX/ybhATRv759UiDWaDTGVNLg"
                                    "SjFsJGeBjItk7wAMuJYGOTfWgj6e6ynLfAOlT8HnBrGvgNjkveyQBLtmeWnCOKrysRFFyDS"
                  ).client('s3')

app = Flask(__name__, template_folder="./")


@app.route('/')
def inicio():
    return render_template("./polly_data_form.html")


@app.route('/process', methods=['POST'])
def process():
    voices = request.form['voices']
    text_to_synthesize = request.form.get("texto")
    new_filename = request.form.get('new_filename')
    try:
        response = polly_client.start_speech_synthesis_task(
                VoiceId=voices,
                OutputS3BucketName='ceiabd-rjc-bucket',
                OutputFormat='mp3',
                Text=text_to_synthesize,
                TextType='text',
                SampleRate='22050')

        # print(f"Audio file is saved into {response['SynthesisTask']['OutputUri']}")
        uri = response['SynthesisTask']['OutputUri']
        filename = uri.split('/')[4]

        time.sleep(30)

        s3.copy_object(Bucket="ceiabd-rjc-bucket", CopySource=f"ceiabd-rjc-bucket/{filename}", Key=f"{new_filename}")
        s3.delete_object(Bucket="ceiabd-rjc-bucket", Key=f"{filename}")
        s3.download_file('ceiabd-rjc-bucket', new_filename, f'./downloads/{new_filename}')

        audio_path = f'./downloads'

        time.sleep(10)

        return render_template("./results.html", voices=voices, text_to_synthesize=text_to_synthesize,
                               response=response, filename=filename, new_filename=new_filename, audio_path=audio_path)
    except:
        raise


if __name__ == "__main__":
    app.run(debug=True)
