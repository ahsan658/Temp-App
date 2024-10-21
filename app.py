import streamlit as st

# Temperature conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Streamlit app interface
st.title("App")

# Conversion type selection
conversion_type = st.selectbox(
    "Choose the conversion type:",
    ["Celsius to Fahrenheit", "Fahrenheit to Celsius", 
     "Celsius to Kelvin", "Kelvin to Celsius", 
     "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"]
)

# Input for temperature
temp_input = st.number_input("Enter the temperature:", format="%.2f")

# Perform conversion based on user's choice
if conversion_type == "Celsius to Fahrenheit":
    result = celsius_to_fahrenheit(temp_input)
    st.write(f"{temp_input}°C = {result}°F")
elif conversion_type == "Fahrenheit to Celsius":
    result = fahrenheit_to_celsius(temp_input)
    st.write(f"{temp_input}°F = {result}°C")
elif conversion_type == "Celsius to Kelvin":
    result = celsius_to_kelvin(temp_input)
    st.write(f"{temp_input}°C = {result}K")
elif conversion_type == "Kelvin to Celsius":
    result = kelvin_to_celsius(temp_input)
    st.write(f"{temp_input}K = {result}°C")
elif conversion_type == "Fahrenheit to Kelvin":
    result = fahrenheit_to_kelvin(temp_input)
    st.write(f"{temp_input}°F = {result}K")
elif conversion_type == "Kelvin to Fahrenheit":
    result = kelvin_to_fahrenheit(temp_input)
    st.write(f"{temp_input}K = {result}°F")

