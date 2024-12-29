import tkinter as tk
from tkinter import messagebox
import requests

def category_name(aqi):
    if aqi <= 50:
        return 'Good'
    elif aqi <= 100:
        return 'Moderate'
    elif aqi <= 150:
        return 'Unhealthy for Sensitive Groups'
    elif aqi <= 200:
        return 'Unhealthy'
    elif aqi <= 300:
        return 'Very Unhealthy'
    else:
        return 'Hazardous'

def check_aqi():
    city = city_entry.get()
    api_key = '0e9a22d93a853daaf977c83e514d18c8ead4f360'
    url = f"http://api.waqi.info/feed/{city}/?token={api_key}"
    response = requests.get(url)
    json_data = response.json()
    print(json_data)  
    aqi = json_data['data']['aqi']
    category = category_name(aqi)
    result_label.config(text=f"The AQI in {city} is {aqi}, which is {category}.")
        

# Create the main window
root = tk.Tk()
root.title("AQI Checker")
root.geometry('400x400')

#create title
title_label = tk.Label(root,text='AIR QUALITY DETECTOR',font=('Arial',17))
title_label.pack(pady=14)


# Create and place the city entry label and input field
city_label = tk.Label(root, text="Enter city:" , font=('Arial',13))
city_label.pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# Create and place the check button
check_button = tk.Button(root, text="Check AQI", command=check_aqi)
check_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

#frame to display aqi information
aqi_frame = tk.LabelFrame(root,text='aqi_info',font=('arial',13))
aqi_frame.pack(padx=10,pady=10)

# Start the main event loop
root.mainloop()
