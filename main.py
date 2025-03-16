from flask import Flask, render_template, request
import maps
import Statics
import ChrisData
import pdf

app = Flask(__name__)

# Data for facilities, ports, routes, etc.

# Data for facilities

facilities = ChrisData.ChatVars.facilities 

# Data for ports

ports = ChrisData.ChatVars.ports 

# Predefined distances between facilities and ports (in km)

distances = ChrisData.ChatVars.distances

 

# Define the cost per ton (fixed value for now)

COST_PER_TON = 50

def destinations():
    dest_list = []
    for port in ports:
        dest_list.append(port["name"])
    return dest_list

def origins():
    origin_list = []
    for facilitie in facilities:
        origin_list.append(facilitie["name"])
    return origin_list

def dist(start,end):
    try:
        distance = distances[start,end]
        return distance
    except:
        return "No route"
    

def price(start, end, tons):
    
    cost = 0
    flag = False
    '''for trips in ChrisData.ChatVars.truck_routes:
        if((trips["start"] == start ) and (trips["end"] == end )):
            cost = trips["cost"] * tons
            flag = True'''
    if (flag):
        return cost
    else:
        return ""
        


@app.route("/", methods=["GET", "POST"])

def index():
    origin = origins()
    destination = destinations()
    total_cost = 0
    tonnage = 0
    distance = None 
    if request.method == "POST":
        action = request.form.get('action')  # Get the value of the 'action' button
        if action == 'calculate':
            selected_origin = request.form.get("origin")
            selected_destination = request.form.get("destination")
            
            try:
                tonnage = int(request.form.get("tonnage", 0))
            except:
                tonnage = 0
            distance = dist(selected_origin,selected_destination) 
            total_cost = price(selected_origin,selected_destination,tonnage)
            T = Statics.Show_trips(selected_origin,selected_destination)
            Statics.compile(T)
            #print(T)
            # Calculate distance and total cost
            '''route_key = (selected_origin, selected_destination)        
            total_cost = tonnage * COST_PER_TON if distance else None        '''
            return render_template(
                "place.html",
                facilities=facilities,
                ports=ports,
                origin=origin,
                destination=destination,
                total_cost=total_cost,
                tonnage=tonnage,
                distance=distance,
                selected_origin = selected_origin,
                selected_destination = selected_destination,
                ), 200
        
        elif action == 'reset':
            selected_origin = request.form.get("origin")
            selected_destination = request.form.get("destination")
            show_routes = request.form.get("route")
            show_routes_checked = show_routes == "true"
            print(show_routes_checked)
            
            tonnage = 0 
            distance = dist(selected_origin,selected_destination) 
            total_cost = price(selected_origin,selected_destination,tonnage)
            if(show_routes_checked):
                T = Statics.Show_trips(selected_origin,selected_destination)
                Statics.compile(T) 
            else:
                T = Statics.Show_trips("","")
                Statics.compile(T)
            #print(T)
            # Calculate distance and total cost
            '''route_key = (selected_origin, selected_destination)        
            total_cost = tonnage * COST_PER_TON if distance else None
            '''
            return render_template(
                "place.html",
                facilities=facilities,
                ports=ports,
                origin=origin,
                destination=destination,
                total_cost=total_cost,
                tonnage=0,
                distance=distance,
                show_routes = show_routes_checked    
            ), 200
        
        elif action == 'options':
            return render_template(
                "form.html",
                ), 200    

        else:
            return "Invalid action!", 400
        
    elif request.method == "GET":
        shipment = ""
        cargo = ""
        TotCargoWPC = 0
        
        params = []
        for key, value in request.args.items():            
            params.append(f'{key}: {value}')
            print("key:"+key+"\n"+"value:"+ value+"\n")
            if key == "shipment" :
                shipment = value
            if key == "cargo" :
                cargo = value
            if key == "TotCargoWPC" :
                TotCargoWPC = value
        pdf.generate_invoice("logistics_invoice.pdf", pdf.invoice_data)
        print("{}:{}\n".format(shipment, cargo))  
        print("weight:{}".format(TotCargoWPC))         
        return  render_template(
                "place.html",
                facilities=facilities,
                ports=ports,
                origin=origin,
                destination=destination,
                total_cost=total_cost,
                tonnage=0,
                distance=distance,
            ), 200
    else:
        return  render_template(
                "place.html",
                facilities=facilities,
                ports=ports,
                origin=origin,
                destination=destination,
                total_cost=total_cost,
                tonnage=0,
                distance=distance,
            ), 200





if __name__ == "__main__":

    app.run(debug=True, port=8080)