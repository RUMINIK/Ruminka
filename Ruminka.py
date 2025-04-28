def count_jewels(J, S):
    count = 0
    for char in S:
        if char in J:
            count += 1
    return count
J = "ab"
S = "aabbccd"
result = count_jewels(J, S)
print(result)
