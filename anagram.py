def are_anagrams(string1, string2):
    l1 = list(string1)
    l2 = list(string2)
    l1.sort()
    l2.sort()
    return l1 == l2


# better way
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


s1 = "banana"
s2 = "anna"
s3 = "anbana"

print(are_anagrams(s1, s2))
print(are_anagrams(s1, s3))
