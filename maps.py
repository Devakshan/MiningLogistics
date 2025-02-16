import folium
import ChrisData 


southafrica = [-30.5595,22.9375]

m = folium.Map(location=(-26.6692, 27.4823),zoom_start=6)


folium.Marker(
    location=southafrica,
    tooltip="Click me!",
    popup="South Africa",
    icon=folium.Icon(icon="glass"),
).add_to(m)


class funcs:
    def select_route(start,end):
        for TruckRoute in ChrisData.ChatVars.truck_routes:
            
            if ((TruckRoute["name"] == start+" to "+end)):
                folium.PolyLine(TruckRoute["coords"], tooltip="Truck "+ str(TruckRoute["name"]), color="#FF00FF",).add_to(m)
                folium.Marker(location=[48.3311, -120.7113], tooltip="Click me!", popup="Timberline Lodge", icon=folium.Icon(color="green"),).add_to(m)
                folium.Marker(
                location=[45.3311, -121.7113],
                tooltip="Click me!",
                popup="Timberline Lodge",
                icon=folium.Icon(color="red"),).add_to(m)

                m.save("index.html")
        return


#for truck_routes in ChrisData.ChatVars.truck_routes:
#   folium.PolyLine(truck_routes["coords"], tooltip="Truck "+ str(truck_routes["name"]), color="#FF0000",).add_to(m)

#for train_routes in ChrisData.ChatVars.train_routes:
#    folium.PolyLine(train_routes["coords"], tooltip="Train "+ str(train_routes["name"]), color="#0000FF",).add_to(m)

m.save("index.html")


