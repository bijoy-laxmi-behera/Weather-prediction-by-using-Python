import requests
 
print("Welcome to the Weather Forecaster!\n\n")
print("Enter the City you want the weather report!\n\n")
 
city_name = input("Enter the name of the City : ")
print("\n\n")

def Gen_report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
     
Gen_report(city_name)
