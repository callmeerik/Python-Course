weight = float(input("Enter your bag weight in kg: "))

if weight <= 23:
    print("✅ Your bag is within the allowed limit.")
elif weight <= 32:
    print("⚠️ Your bag is overweight. You need to pay an extra fee.")
else:
    print("❌ Your bag exceeds the maximum allowed weight. It cannot be checked in.")
