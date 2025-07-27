# Week 10 Project: Weather Dashboard 🌤️

## Overview

Create a weather dashboard that fetches real-time weather data from the internet and displays it in a graphical interface. This project combines API requests, JSON parsing, and GUI development - bringing together web data and visual presentation!

## Learning Objectives

By completing this project, you will:
- ✓ Make API requests to web services
- ✓ Parse JSON data from APIs
- ✓ Create graphical user interfaces with tkinter
- ✓ Handle asynchronous data updates
- ✓ Build real-world connected applications

## Core Requirements (🟢 Basic)

Your weather dashboard must:

1. **Fetch weather data** from a weather API:
   - Current temperature
   - Weather description
   - Humidity and wind speed
   - City name validation

2. **Create a GUI window** with:
   - City input field
   - Search button
   - Weather display area
   - Error message handling

3. **Display weather information** clearly:
   - Temperature in both C° and F°
   - Weather icon or emoji
   - Additional details formatted nicely

4. **Handle errors gracefully**:
   - Invalid city names
   - No internet connection
   - API errors

5. **Update display** when searching new cities

### Example Interface
```
┌─────────────────────────────────────┐
│      🌤️ Weather Dashboard 🌤️        │
├─────────────────────────────────────┤
│                                     │
│  City: [London________] [Search]    │
│                                     │
│  ─────────────────────────────      │
│                                     │
│         London, UK                  │
│           ☁️                        │
│         15°C / 59°F                 │
│     "Partly Cloudy"                 │
│                                     │
│  💧 Humidity: 65%                   │
│  💨 Wind: 12 km/h                   │
│  🔥 Feels like: 13°C                │
│                                     │
└─────────────────────────────────────┘
```

## Implementation Guide

### Step 1: API Setup
- Use OpenWeatherMap API (free tier)
- Get API key from: https://openweathermap.org/api
- Understand API documentation

### Step 2: Basic GUI Structure
Create window with input field and display area.

### Step 3: API Integration
Make requests and parse JSON responses.

### Step 4: Data Display
Format and show weather information.

### Step 5: Error Handling
Handle network and data errors gracefully.

## API Request Example

```python
import requests

API_KEY = "your_api_key_here"
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # Process weather data
```

## Challenges

### 🟡 Intermediate Challenges

1. **5-Day Forecast**: Show upcoming weather

2. **Multiple Cities**: Compare weather in different locations

3. **Weather History**: Store and display past searches

4. **Auto-refresh**: Update weather every 10 minutes

5. **Weather Alerts**: Show severe weather warnings

### 🔴 Advanced Challenges

1. **Weather Map**: Show weather on a simple map

2. **Sunrise/Sunset**: Display daylight information

3. **Weather Trends**: Graph temperature over time

4. **Location Detection**: Auto-detect user's city

5. **Custom Themes**: Different colors for weather conditions

### 🟣 AI Partnership Challenge

1. **API Understanding**:
   - Ask AI: "How do I parse nested JSON from weather APIs?"
   - Learn about API authentication
   - Understand rate limiting

2. **GUI Design**:
   - Get AI's input on user-friendly layouts
   - Learn tkinter best practices
   - Create responsive designs

### ⭐ Reflection Exercise

Write a short paragraph answering:
- What challenges did you face with API integration?
- How did you design the GUI for clarity?
- What error cases did you need to handle?
- How would you extend this for mobile use?

## Testing Your Program

Test these scenarios:
- [ ] Valid city names return weather
- [ ] Invalid cities show error message
- [ ] No internet connection handled
- [ ] GUI updates properly
- [ ] Temperature conversion accurate
- [ ] Special characters in city names
- [ ] API key validation

## Common Mistakes to Avoid

1. **Hardcoding API keys** - Use config file
2. **No error handling** - Network can fail
3. **Blocking GUI** - Long requests freeze interface
4. **Poor layout** - Test window resizing
5. **Missing data fields** - Check API response

## GUI Structure Tips

```python
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Weather Dashboard")

# Create widgets
city_label = tk.Label(root, text="City:")
city_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search_weather)

# Layout widgets
city_label.grid(row=0, column=0)
city_entry.grid(row=0, column=1)
search_button.grid(row=0, column=2)
```

## AI Partnership Tips

### ✅ Good Prompts for Learning
- "How do I make HTTP requests in Python?"
- "What's the basic structure of a tkinter GUI?"
- "How do I extract temperature from weather API JSON?"

### ❌ Avoid These Prompts
- "Create a commercial weather app"
- "Add satellite imagery integration"
- "Build weather prediction algorithms"

## JSON Parsing Pattern

```python
def parse_weather_data(data):
    """Extract weather information from API response"""
    weather = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
    return weather
```

## Submission Checklist

Before considering your project complete:
- [ ] GUI window displays properly
- [ ] City search works correctly
- [ ] Weather data displays clearly
- [ ] Error messages are helpful
- [ ] Temperature shows in C° and F°
- [ ] API integration is stable
- [ ] Code handles edge cases
- [ ] Interface is user-friendly

## Extension Ideas

Once you've completed the basic requirements:
- Add weather emoji/icons
- Create hourly forecast view
- Add favorite cities list
- Show weather-appropriate clothing tips
- Create weather journal feature

## Resources

- Chapter 11: API requests and JSON
- Chapter 12: tkinter GUI basics
- OpenWeatherMap API docs
- Python requests library docs

---

Remember: This project connects your Python skills to the real world! You're building something genuinely useful. 🌍✨

