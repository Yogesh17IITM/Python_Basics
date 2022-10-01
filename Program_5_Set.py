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
