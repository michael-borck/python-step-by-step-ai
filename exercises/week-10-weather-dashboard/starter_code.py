#!/usr/bin/env python3
"""
Weather Dashboard - Starter Code
Week 10 Project

TODO: Create a weather dashboard with GUI and API integration
"""

import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

# API Configuration
API_KEY = "your_api_key_here"  # Get from https://openweathermap.org/api
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Weather Dashboard")
        self.root.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create and layout GUI widgets"""
        # TODO: Create title label
        # TODO: Create city input frame
        # TODO: Create weather display frame
        # TODO: Layout all widgets
        pass
    
    def search_weather(self):
        """Search for weather data and update display"""
        # TODO: Get city name from input
        # TODO: Validate input
        # TODO: Fetch weather data
        # TODO: Update display
        pass
    
    def fetch_weather_data(self, city):
        """Fetch weather data from API"""
        # TODO: Build API URL with city and API key
        # TODO: Make HTTP request
        # TODO: Handle HTTP errors
        # TODO: Parse JSON response
        # TODO: Return weather data dictionary
        return None
    
    def parse_weather_data(self, data):
        """Parse API response into readable format"""
        # TODO: Extract temperature (convert from Kelvin)
        # TODO: Extract weather description
        # TODO: Extract humidity and wind speed
        # TODO: Extract country code
        # TODO: Return organized dictionary
        return {}
    
    def update_weather_display(self, weather_data):
        """Update GUI with weather information"""
        # TODO: Clear previous display
        # TODO: Show city name and country
        # TODO: Display temperature in C and F
        # TODO: Show weather description
        # TODO: Display additional info (humidity, wind)
        pass
    
    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit"""
        # TODO: Implement temperature conversion
        return 0
    
    def show_error(self, message):
        """Display error message to user"""
        # TODO: Show error in GUI or message box
        pass

def main():
    """Main program"""
    # Check if API key is set
    if API_KEY == "your_api_key_here":
        print("⚠️  Please set your API key in the script!")
        print("Get a free key from: https://openweathermap.org/api")
        return
    
    # Create and run the app
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

