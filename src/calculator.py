# main calculation function
def calculate():
    # months dict
    months = {"01":'January', "02":'February', "03":'March', "04":'April', "05":'May', "0":'June', "07":'July', "08":'August', "09":'September', "10":'October', "11":'November', "12":'December'}
    # fees dict
    fees = {}
    # date
    date = input("Enter date of gig (DD/MM/YY)... ")
    day, month, year = date.split("/")
    date = f" {day} {months[month]} 20{year}"

    # invoice prefix
    invoice_number = f"{year}{month}{(input('Enter invoice suffix... '))}"

    # location
    location = f"{input('Enter location of gig... ')} - {day}/{month}/{year}"
    # default fee value
    base_fee = 200
    # travel_tier 0-3
    travel_tier = " " + input("Enter travel tier (0-3)... ")
    travel_tier_fee = float(int(travel_tier) * 20 )

    # petrol calc
    # default efficiency (km / L)
    fuel_efficiency = 14.1602
    # default fuel price per litre (â‚¬)
    fuel_rate = 1.82
    # distance in km
    carpooling = input("Carpooling? (y/n) ")
    if carpooling.upper() == "Y":
        distance = int(input("Enter distance (km) one way... ")) * 2
        carpooling = "(100%)"
    elif carpooling.upper() == "N":
        distance = int(input("Enter distance (km) one way... "))
        carpooling = "(50%)"
    else:
        raise Exception("Invalid answer")
    # total litres
    litres = distance / fuel_efficiency
    # total cost
    fuel_total = round(litres * fuel_rate, 2)

    # toll value
    tolls = round(float(input("Enter toll amount... ")), 2)

    # total of all expenses
    grand_total = base_fee + fuel_total + tolls + travel_tier_fee
    grand_total = round(grand_total, 2)

    # google doc title
    title = f"Invoice {invoice_number}"
    
    # print breakdown of calculations
    print(f"BASE FEE: â‚¬{base_fee}")
    print(f"TRAVEL TIER {travel_tier}: â‚¬{travel_tier_fee:.2f}")
    print(f"FUEL: â‚¬{fuel_total}")
    print(f"TOTAL: â‚¬{grand_total}")

    # return var dict
    var_dict = {"base_fee": base_fee, "travel_tier": travel_tier, "travel_tier_fee": travel_tier_fee, "invoice_number": invoice_number, "date": date, "formatted_date": f"{day} {months[month]} 20{year}", "location": location, "fuel_total": fuel_total, "carpooling": carpooling, "tolls": tolls, "grand_total": grand_total}

def main():
    calculate()

if __name__ == "__main__":
    main()