import requests
input_city = input("Enter the city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={input_city}&appid=YOUR_API_KEY"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Weather in {data['name']}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}K")
else:    print("Failed to retrieve data")
