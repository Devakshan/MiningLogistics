import os
import ChrisData

color_options = [
        "red",        "darkred",        "lightred",        "orange",        "beige",
        "green",      "darkgreen",      "lightgreen",      "blue",          "darkblue",
        "cadetblue",  "lightblue",      "purple",          "darkpurple",    "pink",
        "gray",       "lightgray",      "black",           "lightblue",     "purple",
        "darkpurple",
]


#<head>
head = """<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
        

        <style>
    body {
        font-family: 'Arial', sans-serif;
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #000000;
        margin: 0;
        padding: 0;
    }

    form {
        position: relative;
        top: 0;
        left: 0;
        right: 0;
        height: 100px;
        background: linear-gradient(90deg, #c8d111, #25cc07, #ffc800);
        padding: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        z-index: 1000;
        margin-bottom: -10px;
    }

    .dropdowns {
        display: flex;
        gap: 10px;
    }

    .dropdowns div {
        display: flex;
        flex-direction: column;
    }

    label {
        font-size: 2rem;
        margin-bottom: 4px;
    }

    select, input[type="number"], button {
        height: 35px;
        border: none;
        border-radius: 5px;
        font-size: 1rem;
        padding: 0 10px;
    }

    select {
        background: #ffffff;
        color: #000000;
    }

    select option {
        color: #000000;
    }

    input[type="number"] {
        background: #ffffff;
        color: #000000;
    }

    select:focus, input[type="number"]:focus {
        outline: none;
        box-shadow: 0 0 10px #0078ff;
    }

    button {
        background: linear-gradient(45deg, #00d7ff, #0075ff);
        color: #000000;c
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    button:hover {
        background: linear-gradient(45deg, #0078ff, #00d9ff);
        box-shadow: 0 0 15px #00d9ff;
    }

    .output {
        position: fixed;
        top: 100px;
        left: 0;
        right: 0;
        background: rgba(255, 255, 255);
        //background: linear-gradient(90deg, #c8d111, #25cc07, #ffc800);       
        border-radius: 0 0 15px 15px;
        z-index: 1000;
        text-align: center;
        max-height: 99px;
        overflow-y: auto;
    }
</style>
    
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_ef351b401d0d0ebc9cf28f62d63cb3ee {
                    position: absolute;
                    width: 100.0%;
                    height: 75.0%;
                    left: 0.0%;
                    top: 25.0%;
                }
                .leaflet-container { font-size: 1rem; }
            </style>"""
#</head>

#<body>
body = """<form id+="myForm" method="POST" action="/">
    <!-- Origin and Destination Dropdowns in a Single Row -->
    <div class="dropdowns">
        <div>
            <label for="origin">Origin:</label>
            <select id="origin" name="origin">
                {% for origin in origin %}
                    <option value="{{ origin }}">{{ origin }}</option>
                {% endfor %}
                <!-- Add more origins as needed -->
            </select>
        </div>
        <div>
            <label for="destination">Destination:</label>
            <select id="destination" name="destination">
                {% for destination in destination %}
                    <option value="{{ destination }}">{{ destination }}</option>                    
                {% endfor %}
                <!-- Add more destinations as needed -->
            </select>
        </div>
    </div>

    <!-- Tonnage Input -->
    <div>
        <label for="tonnage">Tonnage:</label>
        <input type="number" id="tonnage" name="tonnage" min="0" step="any" >
    </div>

    <button type="submit" name="action" value="calculate">Calculate</button>
    <button type="submit" name="action" value="reset">Reset</button>
    <button type="submit" name="action" value="options">Generate invoice</button>
    <input type="checkbox" name="route" value="true" {% if show_routes %}checked{% endif %}>
</form>

{% if origin and destination and tonnage is not none %}
    <div class="output">
        <h2>From:{{ selected_origin }} To: {{ selected_destination }} </h2>
        <p>Tonnage: {{ tonnage }} tons<br/>
        
        {% if distance %}
            Distance: {{ distance }} miles<br/>
            Total Cost: R {{ total_cost }}</p>
        {% else %}
            <p>Sorry, no route found for the selected origin and destination.</p>
        {% endif %}
    </div>
{% endif %}


    <div class="folium-map" id="map_ef351b401d0d0ebc9cf28f62d63cb3ee" ></div>"""
#</body>

#<script>
Map_init = """var map_ef351b401d0d0ebc9cf28f62d63cb3ee = L.map(
                "map_ef351b401d0d0ebc9cf28f62d63cb3ee",
                {
                    center: [10, 10],
                    crs: L.CRS.EPSG3857,
                    zoom: 2,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );"""

Map_graphics = """var tile_layer_d332b0be0df238699131b3418790844d = L.tileLayer(
                "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "\\u0026copy; \\u003ca href=\\"https://www.openstreetmap.org/copyright\\"\\u003eOpenStreetMap\\u003c/a\\u003e contributors", "detectRetina": false, "maxNativeZoom": 19, "maxZoom": 19, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            );        
    
            tile_layer_d332b0be0df238699131b3418790844d.addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);"""


Misc = """var popup_c1bfd404112292525114677c96351f7d = L.popup({"maxWidth": "100%"});

                var html_190a209cb5aa8fe4481964b0711c0115 = $(`<div id="html_190a209cb5aa8fe4481964b0711c0115" style="width: 100.0%; height: 100.0%;">Timberline Lodge</div>`)[0];
                popup_c1bfd404112292525114677c96351f7d.setContent(html_190a209cb5aa8fe4481964b0711c0115);"""

Train_TAZARA_Railway = """var poly_line_cc8e45c5ffd31c78326878ce70fd548d = L.polyline(
                [[-6.7924, 39.2083], [-8.2833, 33.8331], [-15.3875, 28.3228]],
                {"bubblingMouseEvents": true, "color": "#0000FF", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "#0000FF", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 3}
            ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);        
    
            poly_line_cc8e45c5ffd31c78326878ce70fd548d.bindTooltip(
                `<div>
                     Train TAZARA Railway
                 </div>`,
                {"sticky": true}
            );"""

Train_Benguela_Railway = """var poly_line_e9569ea122be33360e5ec962c4d66dac = L.polyline(
                [[-12.3646, 13.5304], [-12.0, 20.0], [-11.6692, 27.4823]],
                {"bubblingMouseEvents": true, "color": "#0000FF", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "#0000FF", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 3}
            ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);        
    
            poly_line_e9569ea122be33360e5ec962c4d66dac.bindTooltip(
                `<div>
                     Train Benguela Railway
                 </div>`,
                {"sticky": true}
            );"""


Truck_Lubumbashi_to_Beira = """ var poly_line_af300341ae212266aff1c37ef48d4966 = L.polyline(
                [[-11.6692, 27.4823], [-14.0, 26.0], [-19.8454, 34.8385]],
                {"bubblingMouseEvents": true, "color": "#FF0000", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "#FF0000", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 3}
            ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);
        
    
            poly_line_af300341ae212266aff1c37ef48d4966.bindTooltip(
                `<div>
                     Truck Lubumbashi to Beira
                 </div>`,
                {"sticky": true}
            );"""


Truck_Lubumbashi_to_Lobito = """var poly_line_67c6c51c488b3df0b50f736b6f4be277 = L.polyline(
                [[-11.6692, 27.4823], [-12.5, 20.5], [-12.3646, 13.5304]],
                {"bubblingMouseEvents": true, "color": "#FF0000", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "#FF0000", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 3}
            ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);
        
    
            poly_line_67c6c51c488b3df0b50f736b6f4be277.bindTooltip(
                `<div>
                     Truck Lubumbashi to Lobito
                 </div>`,
                {"sticky": true}
            );"""

Truck_Lubumbashi_to_Dar_es_Salaam = """var poly_line_8971b55457d978dd4546a5247ca6ea7e = L.polyline(
                [[-11.6692, 27.4823], [-8.2833, 33.8331], [-6.7924, 39.2083]],
                {"bubblingMouseEvents": true, "color": "#FF0000", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "#FF0000", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 3}
            ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);     
    
            poly_line_8971b55457d978dd4546a5247ca6ea7e.bindTooltip(
                `<div>
                     Truck Lubumbashi to Dar es Salaam
                 </div>`,
                {"sticky": true}
            );"""


Truck_Lubumbashi_to_Walvis_Bay = """var poly_line_d26c656864e522ef473a5e9ff4252609 = L.polyline(
                [[-11.6692, 27.4823], [-17.499, 24.2891], [-22.9576, 14.5058]],
                {"bubblingMouseEvents": true, "color": "#FF0000", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "#FF0000", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 3}
            ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);
        
    
            poly_line_d26c656864e522ef473a5e9ff4252609.bindTooltip(
                `<div>
                     Truck Lubumbashi to Walvis Bay
                 </div>`,
                {"sticky": true}
            );"""


Truck_Lubumbashi_to_Durban = """var Truck_Lubumbashi_to_Durban = L.polyline(
                [[-11.6692, 27.4823], [-15.3875, 28.3228], [-22.215, 30.0], [-29.8587, 31.0218]],
                {"bubblingMouseEvents": true, "color": "#FF0000", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "#FF0000", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 3}
            ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);
        
    
            Truck_Lubumbashi_to_Durban.bindTooltip(
                `<div>
                     Truck Lubumbashi to Durban
                 </div>`,
                {"sticky": true}
            );"""

Trip_dict = {
    ("Lubumbashi", "Durban"): Truck_Lubumbashi_to_Durban,
    ("Lubumbashi", "Walvis Bay"): Truck_Lubumbashi_to_Walvis_Bay,
    ("Lubumbashi", "Dar es Salaam"): Truck_Lubumbashi_to_Dar_es_Salaam,
    ("Lubumbashi", "Lobito"): Truck_Lubumbashi_to_Lobito,
    ("Lubumbashi", "Beira"): Truck_Lubumbashi_to_Beira,
   
}


Trip_list = [Truck_Lubumbashi_to_Durban,Truck_Lubumbashi_to_Walvis_Bay,
            Truck_Lubumbashi_to_Dar_es_Salaam,Truck_Lubumbashi_to_Lobito,
            Truck_Lubumbashi_to_Lobito,Truck_Lubumbashi_to_Beira,
            ]

truck_list = []

train_list = []

Show_trip = []

def Show_trips(start,end):
    
    if(start == end):
        Trip_list.clear()
        return Trip_list
    else:
        try:
            Show_trip = []
            index = 0
            TL = make_train_routes()       
            for i in TL:
                Trip_list.append(i)
            TL = make_truck_routes()       
            for i in TL:
                Trip_list.append(i)
            
            for truckroutes in ChrisData.ChatVars.truck_routes:
                
                if ((start == truckroutes["start"]) and (end == truckroutes["end"])):
                    Show_trip.append(Trip_list[index])
                    
                else:
                    index = index + 1
            if index >= (len(ChrisData.ChatVars.truck_routes)-1):
                
                for trainroutes in ChrisData.ChatVars.train_routes:
                    
                    if ((start == trainroutes["start"]) and (end == trainroutes["end"])):
                        Show_trip.append(Trip_list[index])
                        print(index)
                    else:
                        index = index + 1
            
            return Show_trip
        except:        
            print("E")
            Trip_list.clear()
            TL = make_train_routes()       
            for i in TL:
                Trip_list.append(i)
            TL = make_truck_routes()       
            for i in TL:
                Trip_list.append(i)
            for i in TL:
                Trip_list.append(i)
            #print(Trip_list)
            return Trip_list
    

marker_list = []

port_list = []

def make_truck_routes():    
    truck_list.clear()
    for i in range(len(ChrisData.ChatVars.truck_routes)):
        truck = ChrisData.ChatVars.truck_routes[i]
        Truck = ""
        Truck = """var Truck"""+truck["name"]+""" = L.polyline(
                """+ str(truck["coords"]) +""",
                {"bubblingMouseEvents": true, "color": "#FF0000", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "#FF0000", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 3}
            ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);
        

            Truck"""+truck["name"]+""".bindTooltip(
                `<div>
                        """+truck["name"]+"""
                    </div>`,
                {"sticky": true}
            );"""
        truck_list.append(Truck)
    return truck_list


def make_train_routes():    
    train_list.clear()
    for i in range(len(ChrisData.ChatVars.train_routes)):
    #i = 0
        rail = ChrisData.ChatVars.train_routes[i]
        Railway = ""
        Railway = """var poly_line_"""+ str(rail["name"]) +""" = L.polyline(
                    """+ str(rail["coords"]) +""",
                    {"bubblingMouseEvents": true, "color": "#0000FF", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "#0000FF", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 3}
                ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);        
        
                poly_line_"""+ str(rail["name"]) +""".bindTooltip(
                    `<div>
                        """+ str(rail["name"]) +"""
                    </div>`,
                    {"sticky": true}
                );"""
        train_list.append(Railway)
    return train_list
    
def color_flow(i):
    ans = divmod(i,21) 
    return ans[1]

#</script>
def make_port():
    port_list.clear()
    for i in range(len(ChrisData.ChatVars.ports)):
        port = ChrisData.ChatVars.ports[i]
        mark = ""
        mark = mark + """var marker_db4d05cb916673810c235e140cf47374 = L.marker(""" + str(port["coords"]) + """,
                {}
            ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);        
            var icon_0ed051f64532aae3297aa7eea80ba936 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "globe", "iconColor": "white", "markerColor":\""""+color_options[color_flow(i)]+"""\", "prefix": "glyphicon"}
            );
            marker_db4d05cb916673810c235e140cf47374.setIcon(icon_0ed051f64532aae3297aa7eea80ba936);        
            var popup_349b07703dcaf48dada8b6466b920a58 = L.popup({"maxWidth": "100%"});
            var html_0b23c9ea1a551fa307c65d219af76310 = $(`<div id="html_0b23c9ea1a551fa307c65d219af76310" style="width: 100.0%; height: 100.0%;">"""+port["name"]+"""</div>`)[0];
            popup_349b07703dcaf48dada8b6466b920a58.setContent(html_0b23c9ea1a551fa307c65d219af76310);
            marker_db4d05cb916673810c235e140cf47374.bindPopup(popup_349b07703dcaf48dada8b6466b920a58);
            marker_db4d05cb916673810c235e140cf47374.bindTooltip(
                `<div>""" + port["details"] + """</div>`,
                {"sticky": true}
            );"""
        port_list.append(mark)

def marker_maker():
    marker_list.clear()
    #for fac in ChrisData.ChatVars.facilities:
    #print(len(color_options))
    for i in range(len(ChrisData.ChatVars.facilities)):
        fac = ChrisData.ChatVars.facilities[i]
        mark = ""
        mark = mark + """var marker_db4d05cb916673810c235e140cf47374 = L.marker(""" + str(fac["coords"]) + """,
                {}
            ).addTo(map_ef351b401d0d0ebc9cf28f62d63cb3ee);        
            var icon_0ed051f64532aae3297aa7eea80ba936 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "folder-close", "iconColor": "white", "markerColor":\""""+color_options[color_flow(i)]+"""\", "prefix": "glyphicon"}
            );
            marker_db4d05cb916673810c235e140cf47374.setIcon(icon_0ed051f64532aae3297aa7eea80ba936);        
            var popup_349b07703dcaf48dada8b6466b920a58 = L.popup({"maxWidth": "100%"});
            var html_0b23c9ea1a551fa307c65d219af76310 = $(`<div id="html_0b23c9ea1a551fa307c65d219af76310" style="width: 100.0%; height: 100.0%;">"""+fac["name"]+"""</div>`)[0];
            popup_349b07703dcaf48dada8b6466b920a58.setContent(html_0b23c9ea1a551fa307c65d219af76310);
            marker_db4d05cb916673810c235e140cf47374.bindPopup(popup_349b07703dcaf48dada8b6466b920a58);
            marker_db4d05cb916673810c235e140cf47374.bindTooltip(
                `<div>""" + fac["details"] + """</div>`,
                {"sticky": true}
            );"""
        marker_list.append(mark)
    
        

def make_html(head,body,script):
    html="<!DOCTYPE html>\n<html>\n<head>\n"
    for items in head:
        html = html + items +"\n\n"
    html = html +"\n\n</head>\n\n<body>"
    for items in body:
        html = html + items +"\n\n"
    html = html +"\n\n</body>\n\n <script>"
    for items in script:
        html = html + items +"\n\n"
    html = html +"\n\n</script>\n\n </html>"    
    with open('templates/place.html', 'w') as file:
        file.write(html)


def compile(Show_trip1):
    scripts = [Map_init,Map_graphics,Misc]
    for mark in marker_list:
        scripts.append(mark)
    for port in port_list:
        scripts.append(port)
    for Trip in Show_trip1:
        scripts.append(Trip)

    make_html(heads,bodys,scripts)

def reset():
    Show_trip  = Show_trips("","")
    marker_maker()
    make_port()
    heads = [head]
    bodys = [body]
    scripts = [Map_init,Map_graphics,Misc]
    for mark in marker_list:
        scripts.append(mark)
    for port in port_list:
        scripts.append(port)
    for Trip in Show_trip:
        scripts.append(Trip)

    make_html(heads,bodys,scripts)

Show_trip  = Show_trips("","")
marker_maker()
make_port()
heads = [head]
bodys = [body]
scripts = [Map_init,Map_graphics,Misc]

compile(Show_trip)
