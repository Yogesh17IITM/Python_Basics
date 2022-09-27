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

review="""Anacell provides the best services in the city,
betacellular has awesome services,
Best services provided by anacell, everyone should use anacell"""

lst_keyword=["anacell", "cetracular", "betacellular"]

lower_review=review.lower()
print(lower_review.count(lst_keyword[0]), lower_review.count(lst_keyword[1]),lower_review.count(lst_keyword[2]))
print(lst_keyword[::])