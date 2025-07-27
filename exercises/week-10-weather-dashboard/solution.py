#!/usr/bin/env python3
"""
Weather Dashboard - Complete Solution
Week 10 Project

This solution implements a weather dashboard with GUI and API integration
using OpenWeatherMap API.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime

# API Configuration
API_KEY = "your_api_key_here"  # Get from https://openweathermap.org/api
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Weather Dashboard")
        self.root.geometry("450x500")
        self.root.configure(bg="#f0f0f0")
        
        # Store recent searches
        self.recent_searches = []
        
        self.create_widgets()
        
    def create_widgets(self):
        """Create and layout GUI widgets"""
        # Title
        title_label = tk.Label(self.root, text="🌤️ Weather Dashboard", 
                              font=("Arial", 20, "bold"),
                              bg="#f0f0f0", fg="#333")
        title_label.pack(pady=15)
        
        # Input frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10, padx=20, fill="x")
        
        # City label and entry
        city_label = ttk.Label(input_frame, text="Enter City:", 
                              font=("Arial", 12))
        city_label.grid(row=0, column=0, padx=5, sticky="w")
        
        self.city_var = tk.StringVar()
        self.city_entry = ttk.Entry(input_frame, textvariable=self.city_var, 
                                   width=25, font=("Arial", 11))
        self.city_entry.grid(row=0, column=1, padx=5, pady=5)
        self.city_entry.bind('<Return>', lambda e: self.search_weather())
        
        # Search button
        search_btn = ttk.Button(input_frame, text="Search 🔍", 
                               command=self.search_weather)
        search_btn.grid(row=0, column=2, padx=5)
        
        # Recent searches dropdown
        self.recent_var = tk.StringVar()
        self.recent_combo = ttk.Combobox(input_frame, textvariable=self.recent_var,
                                        width=22, state="readonly")
        self.recent_combo.grid(row=1, column=1, padx=5, pady=5)
        self.recent_combo.bind('<<ComboboxSelected>>', self.on_recent_selected)
        
        recent_label = ttk.Label(input_frame, text="Recent:", font=("Arial", 10))
        recent_label.grid(row=1, column=0, padx=5, sticky="w")
        
        # Weather display frame
        self.weather_frame = tk.Frame(self.root, bg="white", relief="ridge", bd=2)
        self.weather_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Initial message
        self.show_initial_message()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var,
                             bd=1, relief="sunken", anchor="w",
                             font=("Arial", 9))
        status_bar.pack(side="bottom", fill="x")
        
        # Set focus to entry
        self.city_entry.focus()
        
    def show_initial_message(self):
        """Show initial message in weather frame"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
            
        msg_label = tk.Label(self.weather_frame, 
                            text="Enter a city name to see the weather",
                            font=("Arial", 12), bg="white", fg="#666")
        msg_label.place(relx=0.5, rely=0.5, anchor="center")
        
    def on_recent_selected(self, event):
        """Handle recent search selection"""
        city = self.recent_var.get()
        if city:
            self.city_var.set(city)
            self.search_weather()
            
    def update_recent_searches(self, city):
        """Update recent searches list"""
        # Capitalize city name properly
        city = city.title()
        
        # Remove if already exists
        if city in self.recent_searches:
            self.recent_searches.remove(city)
            
        # Add to beginning
        self.recent_searches.insert(0, city)
        
        # Keep only last 5
        self.recent_searches = self.recent_searches[:5]
        
        # Update dropdown
        self.recent_combo['values'] = self.recent_searches
        
    def search_weather(self):
        """Search for weather data and update display"""
        city = self.city_var.get().strip()
        
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name!")
            self.city_entry.focus()
            return
            
        # Show loading message
        self.show_loading()
        self.status_var.set(f"Searching for {city}...")
        self.root.update()
        
        # Fetch weather data
        weather_data = self.fetch_weather_data(city)
        
        if weather_data:
            # Parse and display weather
            parsed_data = self.parse_weather_data(weather_data)
            self.update_weather_display(parsed_data)
            self.update_recent_searches(city)
            self.status_var.set(f"Weather data for {parsed_data['city']} updated at {datetime.now().strftime('%I:%M %p')}")
        else:
            self.status_var.set("Failed to fetch weather data")
            
    def show_loading(self):
        """Show loading message"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
            
        loading_label = tk.Label(self.weather_frame, text="Loading...",
                               font=("Arial", 14), bg="white", fg="#666")
        loading_label.place(relx=0.5, rely=0.5, anchor="center")
        
    def fetch_weather_data(self, city):
        """Fetch weather data from API"""
        try:
            # Build URL with parameters
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric'  # Get temperature in Celsius
            }
            
            response = requests.get(BASE_URL, params=params, timeout=5)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                self.show_error(f"City '{city}' not found!")
                return None
            elif response.status_code == 401:
                self.show_error("Invalid API key! Please check your configuration.")
                return None
            else:
                self.show_error(f"Error: {response.status_code}")
                return None
                
        except requests.exceptions.ConnectionError:
            self.show_error("No internet connection!")
            return None
        except requests.exceptions.Timeout:
            self.show_error("Request timed out!")
            return None
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
            return None
            
    def parse_weather_data(self, data):
        """Parse API response into readable format"""
        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"],
            "wind_deg": data["wind"].get("deg", 0),
            "clouds": data["clouds"]["all"],
            "icon": self.get_weather_emoji(data["weather"][0]["main"]),
            "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p"),
            "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p")
        }
        return weather
        
    def get_weather_emoji(self, weather_type):
        """Get emoji for weather type"""
        emojis = {
            "Clear": "☀️",
            "Clouds": "☁️",
            "Rain": "🌧️",
            "Drizzle": "🌦️",
            "Thunderstorm": "⛈️",
            "Snow": "❄️",
            "Mist": "🌫️",
            "Fog": "🌫️",
            "Haze": "🌫️",
            "Dust": "🌪️",
            "Sand": "🌪️",
            "Ash": "🌋",
            "Squall": "💨",
            "Tornado": "🌪️"
        }
        return emojis.get(weather_type, "🌤️")
        
    def get_wind_direction(self, degrees):
        """Convert wind degrees to direction"""
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        index = round(degrees / 45) % 8
        return directions[index]
        
    def update_weather_display(self, weather_data):
        """Update GUI with weather information"""
        # Clear previous display
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
            
        # Main container
        main_container = tk.Frame(self.weather_frame, bg="white")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Location and time
        location_text = f"{weather_data['city']}, {weather_data['country']}"
        location_label = tk.Label(main_container, text=location_text,
                                 font=("Arial", 18, "bold"), bg="white")
        location_label.pack()
        
        time_label = tk.Label(main_container, text=datetime.now().strftime("%A, %B %d, %Y"),
                             font=("Arial", 10), bg="white", fg="#666")
        time_label.pack()
        
        # Weather icon and description
        icon_label = tk.Label(main_container, text=weather_data['icon'],
                             font=("Arial", 64), bg="white")
        icon_label.pack(pady=10)
        
        desc_label = tk.Label(main_container, text=weather_data['description'],
                             font=("Arial", 14), bg="white")
        desc_label.pack()
        
        # Temperature
        temp_c = weather_data['temp']
        temp_f = self.celsius_to_fahrenheit(temp_c)
        temp_text = f"{temp_c:.1f}°C / {temp_f:.1f}°F"
        temp_label = tk.Label(main_container, text=temp_text,
                             font=("Arial", 28, "bold"), bg="white")
        temp_label.pack(pady=5)
        
        # Feels like
        feels_c = weather_data['feels_like']
        feels_f = self.celsius_to_fahrenheit(feels_c)
        feels_text = f"Feels like: {feels_c:.1f}°C / {feels_f:.1f}°F"
        feels_label = tk.Label(main_container, text=feels_text,
                              font=("Arial", 11), bg="white", fg="#666")
        feels_label.pack()
        
        # Min/Max temps
        min_max_text = f"H: {weather_data['temp_max']:.1f}° L: {weather_data['temp_min']:.1f}°"
        min_max_label = tk.Label(main_container, text=min_max_text,
                                font=("Arial", 11), bg="white", fg="#666")
        min_max_label.pack(pady=5)
        
        # Details frame
        details_frame = tk.Frame(main_container, bg="white")
        details_frame.pack(pady=15, fill="x")
        
        # Create detail items in grid
        details = [
            ("💧 Humidity", f"{weather_data['humidity']}%"),
            ("💨 Wind", f"{weather_data['wind_speed']} km/h {self.get_wind_direction(weather_data['wind_deg'])}"),
            ("🌡️ Pressure", f"{weather_data['pressure']} hPa"),
            ("☁️ Cloudiness", f"{weather_data['clouds']}%"),
            ("🌅 Sunrise", weather_data['sunrise']),
            ("🌇 Sunset", weather_data['sunset'])
        ]
        
        for i, (label, value) in enumerate(details):
            row = i // 2
            col = i % 2
            
            detail_frame = tk.Frame(details_frame, bg="white")
            detail_frame.grid(row=row, column=col, padx=20, pady=5, sticky="w")
            
            label_widget = tk.Label(detail_frame, text=label,
                                   font=("Arial", 10, "bold"), bg="white")
            label_widget.pack(side="left")
            
            value_widget = tk.Label(detail_frame, text=f" {value}",
                                   font=("Arial", 10), bg="white")
            value_widget.pack(side="left")
            
    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32
        
    def show_error(self, message):
        """Display error message to user"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
            
        error_label = tk.Label(self.weather_frame, text=f"❌ {message}",
                              font=("Arial", 12), bg="white", fg="red")
        error_label.place(relx=0.5, rely=0.5, anchor="center")

def main():
    """Main program"""
    # Check if API key is set
    if API_KEY == "your_api_key_here":
        response = messagebox.askyesno(
            "API Key Required",
            "This app requires an OpenWeatherMap API key.\n\n"
            "Would you like to continue with a demo?\n"
            "(Weather data will not be real)"
        )
        if not response:
            print("⚠️  Please set your API key in the script!")
            print("Get a free key from: https://openweathermap.org/api")
            return
    
    # Create and run the app
    root = tk.Tk()
    app = WeatherApp(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()