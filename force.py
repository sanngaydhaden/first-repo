print("Newton's Second Law Of Motion")
print("---------------------------------------")

# Determine the missing value
print("select the missing value:")
print("1. Mass (m)")
print("2. Accelerration (a)")
print("3. Force (F)")
missing_value_choice = input("Enter the option for the missing value: ")

# Prompt the user to enter the other two values
if missing_value_choice == "1":
        a = float(input("enter acceleration (a): "))
        F = float(input("enter force (F): "))
        m = F / a
        print(f"mass (m) = {m}")

elif missing_value_choice == "2":
        m = float(input("enter mass (m): "))
        F = float(input("enter force (F): "))
        a = F / m
        print(f"Accelaration (a) = {a}")

elif missing_value_choice == "3" :
        m = float(input("enter mass (m): "))
        a = float(input("enter accelaration (a): "))
        F = m * a 
        print(f"Force (F) = {F}")

else:
        print("invalid option selected for the missing value.")
                                
