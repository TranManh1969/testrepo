CURRENT_YEAR = 2021
MET_TO_FEET = 3.281

firstname = input("your firstname: ")
lastname = input("your lastname: ")
year_born = input("when you were born: ")
height_meter = input("your height (meter): ")

year_born = int(year_born)
age = CURRENT_YEAR - year_born

height_meter = float(height_meter)
height_feet = height_meter * MET_TO_FEET
height_feet = round(height_feet,1)

print("\n---")
print("your name is " + firstname + " " + lastname)
print("{0} is {1} years old in {2} ".format(firstname,age,CURRENT_YEAR))
print(" your are " + str(height_feet) + " feet tall")