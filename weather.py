import requests
import json
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import *

# Function to fetch weather data
def fetch_weather():
    location = location_entry.text()
    if not location:
        weather_label.setText("Please enter a location")
        return

    # Show loading message
    weather_label.setText("Loading...")

    # Step 1: Read the API key from Api.txt
    with open('Api.txt', 'r') as file:
        api_key = file.read().strip()

    # Step 2: Define the base URL and parameters for the API request
    base_url = "http://api.weatherstack.com/current"
    params = {
        'access_key': api_key,
        'query': location,
        'units': 'm' if celsius_checkbox.isChecked() else 'f'
    }

    # Step 3: Make the GET request to the Weatherstack API
    response = requests.get(base_url, params=params)

    # Step 4: Parse the JSON response
    if response.status_code == 200:
        data = response.json()
        if 'current' in data:
            current_weather = data['current']
            uv_index = current_weather['uv_index']
            uv_message = get_uv_message(uv_index)
            weather_info = (
                f"Weather in {location}:\n"
                f"Temperature: {current_weather['temperature']}°{'C' if celsius_checkbox.isChecked() else 'F'}\n"
                f"Feels Like: {current_weather['feelslike']}°{'C' if celsius_checkbox.isChecked() else 'F'}\n"
                f"Weather Descriptions: {', '.join(current_weather['weather_descriptions'])}\n"
                f"Humidity: {current_weather['humidity']}%\n"
                f"Wind Speed: {current_weather['wind_speed']} km/h\n"
                f"UV Index: {uv_index} ({uv_message})\n"
                f"Visibility: {current_weather['visibility']} km"
            )
            weather_label.setText(weather_info)
            draw_weather(current_weather['weather_descriptions'][0])
        else:
            weather_label.setText("Unable to fetch weather data.")
    else:
        weather_label.setText(f"HTTP {response.status_code}")

# Function to get UV index message
def get_uv_message(uv_index):
    if uv_index <= 2:
        return "Low: You can safely enjoy being outside!"
    elif 3 <= uv_index <= 7:
        return "Be cautious: Seek shade during midday hours! Slip on a shirt, slop on sunscreen and slap on hat!"
    elif 8 <= uv_index <= 10:
        return "Danger: Avoid being outside during midday hours! Make sure you seek shade! Shirt, sunscreen and hat are a must"
    else:
        return "Extreme: Take all precautions possible. Avoid being outside during midday hours!"

# Function to draw weather information
def draw_weather(description):
    scene.clear()
    icon_path = ""
    if "sunny" in description.lower() or "clear" in description.lower():
        icon_path = "icons/sunny.png"
    elif "cloud" in description.lower():
        icon_path = "icons/cloudy.png"
    elif "rain" in description.lower():
        icon_path = "icons/rainy.png"
    
    if icon_path:
        pixmap = QtGui.QPixmap(icon_path)
        icon_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(icon_item)
    else:
        text = scene.addText("No drawing available")
        text.setDefaultTextColor(QtCore.Qt.black)

# Function to handle real-time input
def handle_text_changed():
    if fetch_timer.isActive():
        fetch_timer.stop()
    fetch_timer.start(500)  # Debounce time of 500ms

# Create the main window
app = QtWidgets.QApplication([])

window = QtWidgets.QWidget()
window.setWindowTitle("Weather App")
window.setGeometry(100, 100, 400, 600)

# Set gradient background
window.setStyleSheet("""
    QWidget {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 1,
            stop: 0 #87CEEB,
            stop: 1 #FFFFFF
        );
    }
""")

layout = QtWidgets.QVBoxLayout()

# Create and place the widgets
location_label = QtWidgets.QLabel("Enter Location:")
location_label.setFont(QtGui.QFont("Times New Roman", 14))
layout.addWidget(location_label)

location_entry = QtWidgets.QLineEdit()
location_entry.setFont(QtGui.QFont("Times New Roman", 14))
location_entry.textChanged.connect(handle_text_changed)
layout.addWidget(location_entry)

weather_label = QtWidgets.QLabel("")
weather_label.setFont(QtGui.QFont("Times New Roman", 14))
layout.addWidget(weather_label)

# Create a scene and view for drawing weather information
scene = QtWidgets.QGraphicsScene()
view = QtWidgets.QGraphicsView(scene)
view.setFixedSize(400, 200)
layout.addWidget(view)

# Add unit conversion toggle
celsius_checkbox = QtWidgets.QCheckBox("Celsius")
celsius_checkbox.setFont(QtGui.QFont("Times New Roman", 14))
celsius_checkbox.setChecked(True)
layout.addWidget(celsius_checkbox)

window.setLayout(layout)
window.show()

# Create a QTimer for debouncing
fetch_timer = QtCore.QTimer()
fetch_timer.setSingleShot(True)
fetch_timer.timeout.connect(fetch_weather)

# Run the application
app.exec_()