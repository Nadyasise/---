
month = input().strip()
month_low = month.lower()
if month_low in ["january","march","may","july","august","october","december"]:
    print(f"{month} has 31 days in it.")
elif month_low in ["april","june","september","november"]:
    print(f"{month} has 30 days in it.")
elif month_low == "february":
    print(f"{month} has 28 or 29 days in it.")
else:
    print("Incorrect month name")