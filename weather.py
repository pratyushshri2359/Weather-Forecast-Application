import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import requests

Height= 500
Width= 600

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature(°F): %s' % (name,desc,temp)
    except:
        final_str='There was a problem'

    return final_str


# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# 455d98c2b7234c98af85ccd5d1911d76

def get_weather(city):
    weather_key = 'XYZ' #you can enter your own key here instead of XYZ
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

root = tk.Tk()

canvas= tk.Canvas(root, height=Height, width=Width)
canvas.pack()

image = Image.open('WEW.JPG')
photo= ImageTk.PhotoImage(image)
back_label = tk.Label(root, image=photo)
back_label.place(relwidth=1, relheight=1)

frame= tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


entry= tk.Entry(frame, font=('Courier',18))
entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text='Get Weather', font=('Courier',10), command= lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth= 0.75, relheight= 0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier',18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)




root.mainloop()
