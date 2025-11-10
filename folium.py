import folium
import webbrowser
import random

lattitude = random.uniform(40.999441, 36.992835)
longitude = random.uniform(-109.051355, -102.041734)

ndlat = random.uniform(48.987802, 45.932179 )
ndlon = random.uniform(-104.000606, -96.577778)



m = folium.Map(location=[39.756927490234375, -105.02362060546875], zoom_starts=5)
folium.Marker([39.756927490234375, -105.02362060546875], popup= "CEC").add_to(m)


userInput = int(input("Enter 1, 2, or 3"))
if userInput == 1:
    print("Youre in Colorado")
    colorPin = input("what color do you want the pin to be?")
    folium.Marker(
    location=[lattitude, longitude],
    tooltip="your pin",
    popup="Random Coord in CO",
    icon=folium.Icon(color= colorPin),
).add_to(m)
    
if userInput == 2:
    print("Youre in North Dakota now")
    colorPin = input("what color do you want the pin to be?")
    folium.Marker(
    location=[ndlat, ndlon],
    tooltip="your pin",
    popup="Random Coord in ND",
    icon=folium.Icon(color= colorPin),
).add_to(m)
    




folium.Marker(
    location=[38.725178, -105.607716],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="green"),
).add_to(m)


#48.987802
#-104.000606

#45.932179 
#-96.577778


print(lattitude)
print(longitude)



m.save("map.html")
webbrowser.open("map.html") #opens map in default browser
