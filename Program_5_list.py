#create a list
from re import S


breakfast_menu=["kaffee","brot","wasser","tee","erdbeeren","pizza",90,10.5]
print(breakfast_menu)

#Accessing the list
print(breakfast_menu[3])
print(breakfast_menu[0:-2]) #printing only food items

#deleting operation
breakfast_menu.remove("erdbeeren") #deleting by using value
print(breakfast_menu)
del(breakfast_menu[1]) #deleting by using index
print(breakfast_menu)
del(breakfast_menu[0:4])
print(breakfast_menu)

#appending operations
breakfast_menu.append(23)
breakfast_menu.append(-40)
print(breakfast_menu)

#insert at particular index
breakfast_menu.insert(0,-100)
print(breakfast_menu)

#printing max and min values
print(max(breakfast_menu))
print(min(breakfast_menu))

#sorting
breakfast_menu.sort() #ascending order
print(breakfast_menu)
breakfast_menu.sort(reverse=True) #sorting in reverse
print(breakfast_menu)

#to clear the list
breakfast_menu.clear()
breakfast_menu.append("Nil")
print(breakfast_menu)

#tuple (non modifiable list)
tpl=(10,60,"abc")
print(type(tpl))

#set type (stores only unique values)
s={10,10,90,78,90,100,10}
print(s) #order not guarenteed, indexing not supported,slicing not supported eg:[0:5]
print(type(s))
s.update([1000])
s.remove(78)
print(s)

#frozenset (unmodifiable set)
f=frozenset(s) #update and remove operation not supported
print(f)
