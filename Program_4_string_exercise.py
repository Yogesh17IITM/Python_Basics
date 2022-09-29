"""
Solve the problem:

Question:
    Given a list of reviews, a list of keywords and an integer k.
    Find the most popular k keywords in order of most to least frequently mentioned.
    The comparison of strings is case-insensitive.
    Multiple occurances of a keyword in a review should be considered as a single mention.
    If keywords are mentioned an equal number of times in reviews, sort alphabetically.

Sample Input and Output:
    Input:
        k = 2
        keywords = ["anacell", "cetracular", "betacellular"]
        reviews = [
        "Anacell provides the best services in the city",
        "betacellular has awesome services",
        "Best services provided by anacell, everyone should use anacell",]

    Output:
        ["anacell", "betacellular", ]

    Explanation:
        "anacell" is occuring in 3 different reviews and "betacellular" is only occuring in 1 review.
        Since k=2, first 2 popular keywords printed.
"""

import collections
from operator import itemgetter

def List(dictionary):
   return list(map(itemgetter(0), dictionary.items()))

lst_review=["Anacell provides the best services in the city",
"betacellular has awesome services",
"Best services provided by anacell, everyone should use anacell",]

lst_keyword=["cetracular", "betacellular","anacell"]

Dict=dict.fromkeys(lst_keyword, 0)

# Convert all given string into lower case
s=""
for iStr in lst_review:
    s += iStr.lower()+"\n"

# count the key occurrences in the review
for iKey in lst_keyword:
    Dict[iKey] = s.count(iKey)
    if Dict[iKey] == 0:
        del Dict[iKey]

# sort the Dict based on value
sorted_lst = sorted(Dict.items(), key=lambda x: x[1], reverse=True)

# Converting list into dictionary
sorted_dict = collections.OrderedDict(sorted_lst)

# print only (sorted) keys
print(List(sorted_dict))



#lower_review=lst_review[].lower()
#print(lower_review.count(lst_keyword[0]), lower_review.count(lst_keyword[1]),lower_review.count(lst_keyword[2]))
#print(lst_keyword[::])