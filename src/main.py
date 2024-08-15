import pyautogui as pag
# months dict
months = {"01":'January', "02":'February', "03":'March', "04":'April', "05":'May', "0":'June', "07":'July', "08":'August', "09":'September', "10":'October', "11":'November', "12":'December'}

def main():
    # fees dict
    fees = {}
    pag.displayMousePosition()

    # date
    date = input("Enter date of gig (DD/MM/YY)... ")
    day, month, year = date.split("/")
    date = f" {day} {months[month]} 20{year}"

    # invoice prefix
    invoice_number = f"{year}{month}{(input("Enter invoice suffix... "))}"

    # location
    location = f"{input("Enter location of gig... ")} - {day}/{month}/{year}"
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
    # coords dict
    coords = [[title, (2625, 400)], [invoice_number, (3712, 615)], [date, (3690, 640)], [location, (3347, 1032)], [travel_tier, (3222, 1080)], [carpooling, (3183, 1130)], [travel_tier_fee, (3780, 1080)], [fuel_total, (3780, 1130)], [tolls, (3780, 1180)], [grand_total, (3780, 1260)]]

    print(f"BASE FEE: â‚¬{base_fee}")
    print(f"TRAVEL TIER {travel_tier}: â‚¬{travel_tier_fee:.2f}")
    print(f"FUEL: â‚¬{fuel_total}")
    print(f"TOTAL: â‚¬{grand_total}")

    # fill out google doc using automation with pyautogui

    for coord in coords:
        # click on location to edit
        pag.click(coord[1])
        # delete existing info
        pag.hotkey("shift", "end")
        # add 'â‚¬' to any money values
        if isinstance(coord[0], float):
            pag.hotkey("altright", "4")
            pag.typewrite(f"{coord[0]:.2f}")
            continue
        # type the info
        pag.typewrite(str(coord[0]))

    # save as pdf
    pag.hotkey("ctrl", "p")


# run program
if __name__ == "__main__":
    main()
