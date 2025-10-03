age = input("Enter your age: ")
age_in_int = int(age)

if age_in_int < 13 :
    age_group = "child"

elif age_in_int < 20 :
    age_group = "teenager"

elif age_in_int < 60 :
    age_group = "adult"

else :
    age_group = "senior"

print("You are categorized as:", age_group)