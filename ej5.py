import zeep
def main():
    wsdl_url = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"
    soap = zeep.Client(wsdl=wsdl_url)
    result = soap.service.FahrenheitToCelsius(90)
    print(result)
    result = soap.service.CelsiusToFahrenheit(32)
    print(result)
if __name__ == '__main__':
    main()