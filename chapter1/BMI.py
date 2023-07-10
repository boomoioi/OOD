h, w = input("Enter your High and Weight : ").split()
h = float(h)
w = float(w)
bmi = w/(h*h)

if bmi >= 30:
    print("Fat")
elif bmi >= 25:
    print("Getting Fat")
elif bmi >= 23:
    print("More than Normal Weight")
elif bmi >= 18.5:
    print("Normal Weight")
else:
    print("Less Weight")