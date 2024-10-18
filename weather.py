import requests

# Replace with your own API key
API_KEY = '09c8d72c153dc441cc335821c9ccd6a7'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city_name):
    # Construct the complete API URL
    url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY + "&units=metric"
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()
        
        # Extract the relevant information
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        # Print the weather details
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        # Print an error message if the response is not successful
        print("Error in the HTTP request")

# Main function
if __name__ == '__main__':
    # Ask the user for a city name
    city_name = input("Enter city name: ")
    # Get the weather information
    get_weather(city_name)
