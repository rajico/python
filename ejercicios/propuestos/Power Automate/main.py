"""
Nombre del programa: API REST con Power Automate: Traducción automática
Descripción: Programa con el que realizamos API REST. Le mandamos una petición POST a Power Automate, donde
le pasamos un texto a traducir en formato JSON. El texto se detectará automáticamente y se traducirá a castellano.

Por último, se guardará el texto en Dropbox y se mostrará por pantalla el texto traducido.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 13/3/23
"""

import requests
import json

url = "https://prod-03.westeurope.logic.azure.com:443/workflows/fc62a08eab634dadbecff7db144b169c/triggers/manual" \
      "/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig" \
      "=IoIIBtF0lQN5brcgwHS0RfpKSM70adS3OfOzHTwNsa0"
data = {'text': 'First try: Can this text be translated?'}
headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)
