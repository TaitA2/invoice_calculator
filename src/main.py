def main():
    # fees dict
    fees = {} 

    # default fee value
    base_fee = 200
    # travel_tier 0-3
    travel_tier = int(input("Enter travel tier (0-3)..."))
    

    # toll value
    tolls = float(input("Enter toll amount..."))

    # petrol calc
    # default efficiency (km / L)
    fuel_efficiency = 14.1602
    # default fuel price per litre (€)
    fuel_rate = 1.82
    # distance in km
    carpooling = input("Carpooling? (y/n)")
    if carpooling.upper() == "Y":
        distance = int(input("Enter distance (km) one way...")) * 2
    elif carpooling.upper() == "N":
        distance = int(input("Enter distance (km) one way..."))
    else:
        raise Exception("Invalid answer")      
    # total litres
    litres = distance / fuel_efficiency
    # total cost 
    fuel_total = round(litres * fuel_rate, 2)

    # total of all expenses
    grand_total = base_fee + fuel_total + tolls

    print(f"BASE FEE: €{base_fee}")
    print(f"TRAVEL TIER {travel_tier}: €{travel_tier * 20}")
    print(f"FUEL: €{fuel_total}")
    print(f"TOTAL: €{grand_total}")

if __name__ == "__main__":
    main()
