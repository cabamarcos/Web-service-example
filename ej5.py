import requests
import xml.etree.ElementTree as ET

# Definir la URL del servicio web
url = "https://www.w3schools.com/xml/tempconvert.asmx?op=ConvertTemp"

# Definir el valor de temperatura a convertir
valor_temp = 20

# Definir la unidad de temperatura original
unidad_origen = "Celsius"

# Definir la unidad de temperatura a la que se desea convertir
unidad_destino = "Fahrenheit"

# Definir los parámetros para la solicitud HTTP POST
params = {"Temperature": valor_temp, "FromUnit": unidad_origen, "ToUnit": unidad_destino}

# Realizar la solicitud HTTP POST al servicio web y obtener la respuesta
response = requests.post(url, data=params)

# Imprimir la respuesta completa de la solicitud HTTP POST
print(response.content)

# Obtener la respuesta del servicio web en formato XML
xml_response = response.text

# Analizar el XML para extraer el valor de temperatura convertido
root = ET.fromstring(xml_response)
valor_convertido = root.find(".//double").text

# Imprimir el resultado de la conversión de temperatura
print(f"{valor_temp} {unidad_origen} = {valor_convertido} {unidad_destino}")
