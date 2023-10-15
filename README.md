# Temp-alert-using-ugent

# Screen Shots
<img width="960" alt="tf1" src="https://github.com/Thirumurugan-12/HackAI_Hack-230687/assets/76591903/9c548621-947f-443b-b4a5-9fd162ae1542">
<img width="959" alt="tf2" src="https://github.com/Thirumurugan-12/HackAI_Hack-230687/assets/76591903/3a0683e6-1c01-4b9b-b54b-51fb23b7f6ea">
<img width="959" alt="tf3" src="https://github.com/Thirumurugan-12/HackAI_Hack-230687/assets/76591903/ce98cc2e-fc25-4fd2-bbe5-63295c32684d">


<img width="741" alt="tf3" src="https://github.com/Thirumurugan-12/Temp-alert-using-ugent/assets/76591903/d3ffc45f-2e7f-4bb4-9363-8e1f26e123ba">

# Code Documentation

This code is a Python script that uses the Streamlit framework to create a simple web application for monitoring temperature in a specific city and sending alerts when the temperature exceeds predefined limits. It also leverages the `uagents` library to schedule periodic temperature checks and send alerts. Below is a documentation of the code.

## Code Structure

1. Import necessary libraries:
   - `requests`: For making HTTP requests to fetch weather data.
   - `uagents`: For creating and managing agent tasks.
   - `asyncio`: For managing asynchronous tasks.
   - `time`: For time-related functions.
   - `streamlit`: For creating the web application.

2. Create a new asyncio event loop to run asynchronous tasks.

3. Define a `bluesense` agent using `uagents`. This agent is responsible for sending temperature alerts.

4. Define an interval-based task named `Tempreach` that periodically checks the temperature and sends alerts based on predefined limits.

5. Create a Streamlit web application:

   - Set the web application title.
   - Create a sidebar for setting temperature threshold limits.

6. Define a function `kelvin_to_celsius` to convert temperatures from Kelvin to Celsius.

7. When the "Submit" button is clicked:

   - Fetch the city name and temperature limit inputs from the Streamlit interface.
   - Send an API request to OpenWeatherMap to get the current weather data for the specified city.
   - Convert the temperature from Kelvin to Celsius.
   - Check if the temperature falls outside the specified threshold limits.
   - If the temperature is outside the limits, start the `bluesense` agent to send temperature alerts.

## Instructions to Run the Code

Follow these steps to run the code:

1. Install the required Python libraries if you haven't already. You can install them using pip:

   ```bash
   pip install requests uagents asyncio streamlit
   ```

2. Get an API key for the OpenWeatherMap API by signing up on their website.

3. Create a text file named `api_key.txt` and paste your OpenWeatherMap API key into it. Save it in the same directory as your script.

4. Run the script using the following command:

   ```bash
   python your_script_name.py
   ```

5. The Streamlit web application will launch in your web browser.

6. Enter the city name, upper temperature limit, and lower temperature limit in the respective input fields.

7. Click the "Submit" button to check the temperature and receive alerts if the temperature exceeds the defined limits.

8. The `Tempreach` function will periodically check the temperature, and if it exceeds the limits, it will send an alert via the `bluesense` agent.

9. The application will display the current temperature and whether it is within the specified limits.

10. To exit the application, simply close the web browser or stop the Python script.

**Note:** Make sure you have an active internet connection while running the code since it fetches weather data from the OpenWeatherMap API.
