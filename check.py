# To check if a certain phrase or character is present in a string, we can use the keyword in


name = "the sky is blue"
print("sky" in name)
print("the" in name)
print("yes" in name)
print("blue" in name)
print("colorful" in name)

print("   ")

bio = "everybody is a genius"
print("football" in bio)
print("genius" in bio)
print("every" in bio)
print("means" in bio)
if "genius" in bio:
    print("yes'genius' is present")


print("   ")

m = 'all is well'
if "all" in m:
    print("yes 'all' is present")
if "well" in m:
    print("yes 'well' is present")
print("no 'every'is " not in m)


m = 'all is well'
if "much" not in m:
    print(" no 'much' is not present")


bio = "everybody is a genius"
if "super" not in bio:
    print("no 'super' is not present")