from tkinter import *
import api
root=Tk()
root.title('GeoWeather Dector')

city_label=Label(root, text="The city you are in is:"+api.city,font=("Arial",10)).pack()

temp_label=Label(root,text="The temprature is "+str(api.temp)+'°')
temp_label.pack()

feel_label=Label(root,text="The feel like temprature is "+str(api.feel)+'°')
feel_label.pack()

max_label=Label(root,text="The maximum temprature at your city is :"+str(api.max)+'°')
min_label=Label(root,text="The minimum temprature at your city is :"+str(api.min)+'°')

weather_label=Label(text="The weather at your city at the current moment is :"+api.weather_description)

max_label.pack()
min_label.pack()
weather_label.pack()


root.mainloop()
