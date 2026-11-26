set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}
union = set1.intersection(set2)
total_guest = list(union)
print("Total guests to be invited in party are :", len(total_guest))
print("Guest List :", total_guest)