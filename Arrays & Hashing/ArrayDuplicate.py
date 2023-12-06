from os import system

#Time: O(n) Memory: O(n)

def checkIfArrayDuplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        else:
            hashset.add(n)
    return False

subject = [1, 2, 3, 4, 3]

system('cls')

result = checkIfArrayDuplicate(subject)
if result:
    print("Has duplicate")
else:
    print("Has no duplicates")