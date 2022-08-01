import requests;

usr_ip = requests.get('https://ipapi.co/ip/').text

#Obtener la información del formato JSON proporcionado por ipapi
usr_data_json = requests.get('https://ipapi.co/' + usr_ip + '/json').json()

#Crear arreglo para delimitar la información que queremos obtener
usr_data = [["Dirección IP", "Versión", "Código Postal", "Ciudad", "Estado", "País", "Zona Horaria", "ASN", "ISP",], 
        ["ip", "version", "postal", "city", "region", "country_name", "timezone", "asn", "org"]]  

#Imprimir la información obtenida de acuerdo al arreglo

print ("IP Address Lookup Tool")
print ("----------------------")
for x in range(len(usr_data[0])): 
    print(usr_data[0][x] + ": " + usr_data_json[usr_data[1][x]])
