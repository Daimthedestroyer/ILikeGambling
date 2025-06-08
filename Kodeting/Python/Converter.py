def km_to_miles(amount_of_km):
    return round(amount_of_km / 1.6, 2)

def kg_to_pounds(amount_of_kg):
    return round(amount_of_kg * 2.2, 2)

def C_to_F(amount_of_C):
    return round(amount_of_C * (9/5) + 32, 2)

def miles_to_km(amount_of_miles):
    return round(amount_of_miles * 1.6, 2)

def pounds_to_kg(amount_of_pounds):
    return round(amount_of_pounds / 2.2, 2)

def F_to_C(amount_of_F):
    return round(5/9 * (amount_of_F - 32), 2)

while True:
    type_of_unit = (input("Which unit are you converting from? (Metric or Imperial) Type 'Stop' to end program. ")).lower()

    if type_of_unit == "stop":
        break

    if type_of_unit == "metric":
        metric_conversion_type = (input("What are you converting? (Kilometers, Kilograms and Celsius) ")).lower()
        if metric_conversion_type == "kilometers":
            amount_of_km = float(input("How many km to miles? "))
            print(f"{amount_of_km} kilometers is approximately {km_to_miles(amount_of_km)} miles.")
        elif metric_conversion_type == "kilograms":
            amount_of_kg = float(input("How many kg to pounds? "))
            print(f"{amount_of_kg} kilograms is approximately {kg_to_pounds(amount_of_kg)} pounds.")
        elif metric_conversion_type == "celsius":
            amount_of_C = float(input("How many Celsius to Fahrenheit? "))
            print(f"{amount_of_C} degrees is approximately {C_to_F(amount_of_C)} degrees Fahrenheit.")
        else:
            print("Unknown Metric unit.")
        
    elif type_of_unit == "imperial":
        imperial_conversion_type = (input("What are you converting? (Miles, Pounds, Fahrenheit) ")).lower()
        if imperial_conversion_type == "miles":
            amount_of_miles = float(input("How many miles to km? "))
            print(f"{amount_of_miles} miles is approximately {miles_to_km(amount_of_miles)} kilometers.")
        elif imperial_conversion_type == "pounds":
            amount_of_pounds = float(input("How many pounds to kg? "))
            print(f"{amount_of_pounds} pounds is approximately {pounds_to_kg(amount_of_pounds)} kilograms.")
        elif imperial_conversion_type == "fahrenheit":
            amount_of_F = float(input("How many Fahrenheit to Celsius? "))
            print(f"{amount_of_F} degrees is approximately {F_to_C(amount_of_F)} degrees Celsius.")
        else:
            print("Unknown Imperial unit.")

    else:
        print("Unknown unit. Please type 'Metric', 'Imperial' or 'Stop'")      