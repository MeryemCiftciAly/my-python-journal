print("# This is about using string to search for data")

phone = "378 897 9 6715"
print(phone.startswith("37"))

map_name = "map_hatka Mara"
print(map_name.endswith("ara"))

print("_" in map_name)

print("--- Searching and slicing---")

longinfo = "jacon-maple A tony labelle Pang.o"

print(longinfo[longinfo.find("A"):-14])

print(longinfo.find("maple")) # find method

print(longinfo[longinfo.find("-")+1:12])

longinfo2 = "jacon-syrup tony labelle Pang.o"

tony = longinfo2[12:17]

syrup = longinfo2[6:11]

print(tony.capitalize(), syrup.capitalize())

print(longinfo2[longinfo2.find("-")+1:17].title())





