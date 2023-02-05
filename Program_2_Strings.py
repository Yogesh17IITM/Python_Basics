#program to demonstrate strings

#print the string
s="i love india"
print(s,len(s))

multi_s="""hallo
danke
wie gehts
"""
print(multi_s,len(multi_s))

#print the copy of strings
print(s*3) #print strings 3 times

print("printing strings in different ways")
#syntax string[<start_idx>:<end_idx>:<interval>]
print(s[0]) #printing first character of the string
print(s[0:5]) #print first 5 characters starting from index 0
print(s[1:5]) #print characters from index 1 to 5
print(s[1:5:1]) #print characters from index 1 to 5 with 0 intervals
print(s[:3]) #printing characters till index 3
print(s[5:]) #printing all characters starting from index 5
print(s[::3]) #printing characters with every 2 intervals
print(s[2:10:2]) #printing from 2nd index to 10th index at every 1 intervals
print(s[::-1]) #reverse the string
print(s[-3::]) #printing characters from last 3rd index
print(s[-3::-1]) #printing characters from last 3rd index in reverse
print(s[0:100]) #print all characters
print(s[100:-1]) #prints nothing
print(s[:3:-1]) #printing from reverse till index 3
print(s[:-3:-1]) #printing from reverse till index -3 (3rd index from last)