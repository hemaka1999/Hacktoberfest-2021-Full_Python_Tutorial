volume=input("volume: ")
unit=input("Unit (l/ml): ")
convert_to=input("Convert to(l/ml/): ")
if unit=='l':
    convert=int(volume)*1000
    print(f"{convert}ml")
elif unit == 'ml':
    convert = int(volume) /1000
    print(f"{convert}l")
else:
   print("error")