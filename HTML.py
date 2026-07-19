print("Organic Soil Conditioner Survey")

name = input("Enter Farmer Name: ")
age = input("Enter Age: ")
village = input("Enter Village: ")

awareness = input("Are you aware of Organic Soil Conditioner? (Yes/No): ")
usage = input("Are you using Organic Soil Conditioner? (Yes/No): ")

print("\n------ Survey Report ------")
print("Farmer Name :", name)
print("Age :", age)
print("Village :", village)
print("Awareness :", awareness) 
print("Usage :", usage)

if awareness.lower() == "yes":
    print("Farmer is aware of Organic Soil Conditioner.")
else:
    print("Farmer is not aware of Organic Soil Conditioner.")

if usage.lower() == "yes":
    print("Farmer is using Organic Soil Conditioner.")
else:
    print("Farmer is not using Organic Soil Conditioner.")

    print("====== Farmer Registration ======")

# Get details from the farmer
name = input("Enter Farmer Name: ")
village = input("Enter Village Name: ")
mobile = input("Enter Mobile Number: ")
land = input("Enter Land Size (Acres): ")

# Display the details
print("\n----- Farmer Details -----")
print("Farmer Name :", name)
print("Village     :", village)
print("Mobile No.  :", mobile)
print("Land Size   :", land, "Acres")

print("\nRegistration Successful!")

# Soil Conditioner Company Registration Program

print("======================================")
print(" SOIL CONDITIONER PURCHASE REGISTRATION ")
print("======================================")

# Company Details
company_name = input("Enter Company Name: ")

# Farmer Details
farmer_name = input("Enter Farmer Name: ")
village = input("Enter Village Name: ")
mobile = input("Enter Mobile Number: ")

# Purchase Details
product_name = input("Enter Soil Conditioner Name: ")
quantity = int(input("Enter Quantity (Bags): "))
price = float(input("Enter Price per Bag: "))

# Calculate Total Amount
total_amount = quantity * price

# Display Registration Profile
print("\n========== REGISTRATION PROFILE ==========")
print("Company Name      :", company_name)
print("Farmer Name       :", farmer_name)
print("Village           :", village)
print("Mobile Number     :", mobile)
print("Product Name      :", product_name)
print("Quantity          :", quantity, "Bags")
print("Price Per Bag     : ₹", price)
print("Total Amount      : ₹", total_amount)
print("------------------------------------------")
print("Registration Successful!")
print("Thank you for purchasing directly from the company.")