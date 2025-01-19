conversion_type = input("Convert from (km to miles or miles to km): ")
distance = float(input("Enter distance: "))

if conversion_type == "km to miles":
    print(f"Distance in miles: {distance * 0.621371}")
elif conversion_type == "miles to km":
    print(f"Distance in kilometers: {distance / 0.621371}")
else:
    print("Invalid conversion type")
