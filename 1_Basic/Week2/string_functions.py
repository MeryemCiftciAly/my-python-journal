
print("------------"  "Built-in Functions"  "--------------------------")
#String built-in functions
#Types
name = "Meryem"
print(type(name))

age = 37
print(type(age))

#string value allows you to convert other values to strıng
print("Your age is:" + str(age))
print(type(age)) 

age = str(age) # assigns int data type age as string data type

print(type (age))

comment = "Now age is string you can not do this you will get error: age = age + 5" 
print(comment)
# age = age + 5

print()

print("------------"  "replace()"  "--------------------------")
#Replace Method
price = "12346,90"
print(price.replace(",", "."))
print()

phone = "£176-1235-78"
print(phone.replace("-", "/"))

print(phone.replace("-", " "))

print(phone.replace("£","").replace("-","/"))

#Assign
phone_number = "+49 (176) 123-4567"

#Transform
cleaned_phone_number = (

     phone_number
     .replace("+","00")  
     .replace("(","") 
     .replace(")","")
     .replace("-","")
     .replace(" ","")
    )
print(cleaned_phone_number)

print("------------"  " + Operator"  "--------------------------")

#Transformation with the "+" operator
first_name = "Alice"
last_name = "Bird"
full_name = "Alice" + "-" + "Bird"
full_name = "Alice" + " " + "Bird"

print(full_name)

#concatinate file paths

folder = "C:/User/Meryem/Reports/"
file= "operations.csv"

full_path_name = folder + file
print(full_path_name)

print("------------"  "f-string"  "--------------------------")

#f-string - f means formatted

name = "Tubbi"
age = 2
is_student = False

print(f"""
  My name is {name},
  I am {age},
  and my student status is {is_student}."""
)

print()

print(f"2 + 3 = {{2 + 3}}")

print()

print("------------"  "Split()"  "--------------------------")

#split() - breaking string into multiple string value
stamp = "2026-09-20 14:30"
print(stamp.split(" "))

print()

stamp = "2026-09-20"
print(stamp.split("-"))

print("--" * 23) # This is a multiplier

print(" ---- Indexing is getting only one character----")

m = "Mango"
print(m[-4])

print(m[1])

print(" ---- Slicing is getting multiple characters----")

park = "Dinosaur"

print(park[0:4])

print(park[-3:])

print(park[4:5])

print(park[3:4])

print(park[1:2])