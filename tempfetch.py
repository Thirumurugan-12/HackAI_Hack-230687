import requests
from uagents import Agent, Context
import asyncio


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
bluesense = Agent("Bluesense",endpoint=["http://127.0.0.1:8001/submit"])

@bluesense.on_interval(period=300.0)
async def Tempreach(ctx: Context):
    ctx.logger.info(f'Temperate Excedded by {int(temp_celsius) - int(limit_temp)}')
    st.write(temp_celsius)
    st.write(" Temperature Exceeded the Limit")

bluesense.start_background_tasks()

import streamlit as st
st.title("Temperature Alert")
st.sidebar.title("Threshold Settings") 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = open('api_key.txt', 'r').read()
city = st.text_input("Enter the city name: ")
limit_temp = st.sidebar.text_input("Enter the Limit of the Temperature ")


def kelvin_to_celsius(temp):
    return temp - 273.15

if city is not None and len(city) > 0:
    url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(url).json()
    temp_kelvin = response['main']['temp']
    temp_celsius = kelvin_to_celsius(temp_kelvin) 
    print("Ex")
    if limit_temp is not None and len(limit_temp) > 0:
        if int(limit_temp) > int(temp_celsius):
            print("Exceptional Temperature")
            bluesense.run()
    st.write("Temp Normal")
    st.write(temp_celsius)
    #print(response)