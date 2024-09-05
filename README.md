# Weather App

This is a PyQt5-based desktop application that fetches and displays weather information for a specified location. The application uses the Weatherstack API to retrieve current weather data and provides a graphical representation of the weather conditions.

## Features

- **Real-time Weather Data**: Fetches current weather information for any location.
- **Temperature Units**: Option to display temperature in Celsius or Fahrenheit.
- **Graphical Representation**: Displays weather icons based on the current weather conditions.
- **UV Index Information**: Provides a message based on the UV index to help users take necessary precautions.

## Screenshots

![Weather App Screenshot](path_to_screenshot.png)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Get an API key**:
    - Sign up at [Weatherstack](https://weatherstack.com/) to get a free API key.
    - Create a file named `Api.txt` in the root directory of the project and paste your API key into this file.

4. **Run the application**:
    ```sh
    python main.py
    ```

## Usage

1. **Enter Location**: Type the name of the location for which you want to fetch the weather data in the text field labeled "Enter Location".
2. **Temperature Units**: Check the "Celsius" checkbox if you want the temperature to be displayed in Celsius. Uncheck it for Fahrenheit.
3. **Weather Information**: The application will display the current weather information, including temperature, feels-like temperature, weather descriptions, humidity, wind speed, UV index, and visibility.
4. **Graphical Representation**: The application will also display an icon representing the current weather conditions (sunny, cloudy, or rainy).

## Code Overview

- **fetch_weather**: Fetches weather data from the Weatherstack API and updates the UI with the fetched data.
- **get_uv_message**: Returns a message based on the UV index to help users take necessary precautions.
- **draw_weather**: Draws weather icons based on the current weather descriptions.
- **handle_text_changed**: Handles real-time input changes and debounces the fetch_weather function.

## Dependencies

- `requests`
- `json`
- `PyQt5`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize the content as per your project's specifics, such as adding a screenshot, updating the repository URL, or any other details you find necessary.
