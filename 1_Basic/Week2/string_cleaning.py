# Whitespace cleaning
text = " Engineering ".strip()
print(text)

text ="Engineering ".rstrip() #removing right whitespace
print(text)

text = " Engineering".lstrip()
print(text)

print("""------"Always best to use strip() to make sure all spaces are being removed.
      It will not remove spaces in the middle. It can also remove special characters------        
      """)

text = "*** M".strip("*")
print(text)

print("--- Testing for whitespaces in data")
dino = " Spotty Dinosaur"
print(len(dino))
print(len(dino.strip()))

print (len(dino) - len(dino.strip()))
print (len(dino) == len(dino.strip()))

spaces_there = len(dino) == len(dino.strip())
how_many = len(dino) - len(dino.strip())

print("Are spaces in my data?", spaces_there)
print("If so how many spaces?", how_many)

print("---Python Challenge: Turn messy string into a single clean summary with name, role and age ")

messystg = "968-Maria, (Data Engineer) ;; 27y"

cleanstrg = messystg.strip()
cleanstrg = cleanstrg.replace("968-Maria,", "name: maria | ")
cleanstrg = cleanstrg.replace("(Data Engineer)", "role: data engineer | ")
cleanstrg = cleanstrg.replace(";","")
cleanstrg = cleanstrg.replace("27y", "age:27")
cleanstrg = cleanstrg.strip()

print(cleanstrg)

space_check = len(cleanstrg) - len(cleanstrg.strip())
print(space_check)