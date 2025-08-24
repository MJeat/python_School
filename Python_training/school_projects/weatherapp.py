
import requests
import matplotlib.pyplot as plt # install matplotlib: pip install matplotlib
                                    # Use for statistic and visualization
from datetime import datetime, timedelta




API_KEY = '6b312807b2abd49cc57001ea6bbec47d'  # Replace this with your actual API key

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")
        return []

    data = response.json()

    if 'list' not in data:
        print("Error: 'list' key not found in the response")
        return []

    temperatures = [data['list'][i]['main']['temp'] for i in range(0, 40, 8)]
    return temperatures

def calculate_average(temps):
    return sum(temps) / len(temps)

def find_highest(temps):
    return max(temps)

def find_lowest(temps):
    return min(temps)

def present_results(average, highest, lowest):
    print("\nWeather Analysis Results:")
    print(f"Average Temperature: {average:.2f}°C")
    print(f"Highest Temperature: {highest}°C")
    print(f"Lowest Temperature: {lowest}°C")

def plot_temperatures_line_chart(temps):
    # Create a list of dates starting from today
    start_date = datetime.now()
    dates = [(start_date + timedelta(days=i)).strftime('%d %b') for i in range(len(temps))]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, temps, marker='o', color='b')  # Use dates for the x-axis
    plt.title('5-Day Temperature Forecast')
    plt.xlabel('Days')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Adjust layout to make room for rotated x-axis labels
    plt.show()

def main():
    city = input("Enter city name: ")
    temperatures = get_weather_data(city)

    if temperatures:
        average = calculate_average(temperatures)
        highest = find_highest(temperatures)
        lowest = find_lowest(temperatures)

        present_results(average, highest, lowest)
        plot_temperatures_line_chart(temperatures)

if __name__ == "__main__":
    main()