import requests
from uagents import Agent, Context
import asyncio
import time

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
bluesense = Agent("Bluesense",endpoint=["http://127.0.0.1:8001/submit"])

@bluesense.on_interval(period=300.0)
async def Tempreach(ctx: Context):
    ctx.logger.info(f'Temperate Excedded by {int(temp_celsius) - int(limit_temp_up)}')
    st.write("Current Temp",temp_celsius)
    if int(temp_celsius) not in range(int(limit_temp_down),int(limit_temp_up)+1):
        st.write(" Temperature subceeded the Limit") 
        time.sleep(60)
        loop.stop
    else:
        st.write("Normal Temperture")
        time.sleep(60)
        loop.stop()

#bluesense.start_background_tasks()

import streamlit as st
st.title("Temperature Alert")
st.sidebar.title("Threshold Settings") 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = open('api_key.txt', 'r').read()
city = st.text_input("Enter the city name: ")
limit_temp_up = st.sidebar.text_input("Enter the Limit of the Temperature (Upper Limit) ")
limit_temp_down = st.sidebar.text_input("Enter the Limit of the Temperature (Lower Limit) ")

submit = st.button("Submit")

print("down temp = ",limit_temp_down)
print("up temp = ",limit_temp_up)

def kelvin_to_celsius(temp):
    return temp - 273.15

if submit:
    if city is not None and len(city) > 0:
        url = base_url + "appid=" + api_key + "&q=" + city

        response = requests.get(url).json()
        print(response)
        temp_kelvin = response['main']['temp']
        temp_celsius = kelvin_to_celsius(temp_kelvin) 
        print(int(temp_celsius))
        if limit_temp_up is not None and len(limit_temp_up) > 0 and limit_temp_down is not None and len(limit_temp_down) > 0:
            if int(temp_celsius) not in range(int(limit_temp_down),int(limit_temp_up)+1):
                print("Exceptional Temperature")
                bluesense.run()
        st.write("Temp Normal")
        st.write("Current TEMP",temp_celsius)
    #print(response)