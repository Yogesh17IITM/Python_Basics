s="  Du bist sehr nett  "

#printing without spaces
print(s)
print(s.strip()) #printing without spaces
print(s.lstrip()) #removing space at the front(left)
print(s.rstrip()) #removing space at the back(right)

#finding substrings
print(s.find("sehr")) #finding the substring "sehr"
print(s.find("bist",0,5)) #finding the substring "bist", search from idx 0 to 5
print(s.find("bist",0,10)) #finding the substring "bist", search from idx 0 to 10

#replace the substring
print(s.replace("nett", "klug")) #find the string "nett" and replace it by "klug"

#printing string in upper,lower,camel case
print(s.upper())
print(s.lower())
print(s.title())

#count repeated characters
print(s.count("s"))


