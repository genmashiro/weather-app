import tkinter as tk
import requests

# Enter your API key here
API_KEY = 'YOUR_API'
YOUR_CITY = 'YOUR_CITY'

# URL for the weather API
WEATHER_URL = f'http://api.openweathermap.org/data/2.5/weather?q={YOUR_CITY}&appid={API_KEY}'

# URL for the forecast API
FORECAST_URL = f'http://api.openweathermap.org/data/2.5/forecast?q={YOUR_CITY}&appid={API_KEY}'

# Create the GUI window
window = tk.Tk()
window.title('Weather App')
window.geometry('500x300')

# Create labels to display the weather information
current_temp_label = tk.Label(window, text='Current Temperature: ', font=('Arial', 20, 'bold'))
current_temp_label.pack(pady=20)

current_desc_label = tk.Label(window, text='Current Description: ', font=('Arial', 16))
current_desc_label.pack(pady=10)

forecast_label = tk.Label(window, text='5-day Forecast: ', font=('Arial', 16))
forecast_label.pack(pady=10)

# Function to update the weather information
def update_weather_info():
    # Get the weather data from the API
    weather_data = requests.get(WEATHER_URL).json()
    forecast_data = requests.get(FORECAST_URL).json()

    # Update the current weather labels
    current_temp = round(weather_data['main']['temp'] - 273.15, 2)
    current_temp_label.config(text=f'Current Temperature: {current_temp} C°')

    current_desc = weather_data['weather'][0]['description'].title()
    current_desc_label.config(text=f'Current Description: {current_desc}')

    # Update the forecast label
    forecast = ''
    for i in range(0, 5):
        temp = round(forecast_data['list'][i]['main']['temp'] - 273.15, 2)
        desc = forecast_data['list'][i]['weather'][0]['description'].title()
        forecast += f'{i+1}. {temp} °C, {desc}\n'
    forecast_label.config(text=f'5-day Forecast: \n{forecast}')

    # Check for weather alerts and display notifications if any
    if 'alerts' in weather_data:
        for alert in weather_data['alerts']:
            message = f'{alert["event"]} - {alert["description"]} - {alert["start"]} to {alert["end"]}'
            tk.messagebox.showwarning('Weather Alert', message)

# Button to update the weather information
update_button = tk.Button(window, text='Update', command=update_weather_info, font=('Arial', 14, 'bold'), bg='#4CAF50', fg='white')
update_button.pack(pady=20)

# Run the GUI window
window.mainloop()
