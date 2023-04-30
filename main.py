def next_hsn(c):
    if c % 2 == 0:
        return c // 2
    else:
        return 3 * c + 1


def hsn(c):
    sequence = [c]
    while c > 1:
        c = next_hsn(c)
        sequence.append(c)
    return sequence


highest_value = 0
highest_value_number = 0
T = []
L = []
S = []

for i in range(1001):
    n = 1
    x = next_hsn(i)
    T.append(hsn(i))
    if max(T[i]) > highest_value:
        highest_value = max(T[i])
        highest_value_number = T[i].count(max(T[i]))
        S.clear()
        S.append(i)
    elif max(T[i]) == highest_value:
        highest_value_number = highest_value_number + T[i].count(max(T[i]))
        S.append(i)
    L.append(len(T[i]))

R = [0] * max(L)

for x in range(len(L)):
    R[L[x]-1] = R[L[x]-1] + 1

mcs_length = R.index(max(R))

mcs_noc = max(R)

A =[]

for y in range(len(L)):
    if L[y] == mcs_length:
        A.append(y)

longest_length = max(L)

longest_length_seed = L.index(max(L))

for i in range(len(S)):
    S[i] = str(S[i])

for j in range(len(A)):
    A[j] = str(A[j])

print("Problem 1 (for range 1-1000):")
print(f"- longest sequence contains {longest_length}")
print(f"- starts from seed: {longest_length_seed}\n")
print("Problem 2 (for range 1-1000):")
print(f"- highest element value is {highest_value}")
print(f"- found {highest_value_number} times")
print(f"- in sequences starting from seeds: {', '.join(S)}\n")
print("Problem 3 (for range 1-1000):")
print(f"- most common sequence length is {mcs_length}")
print(f"- found {mcs_noc} times")
print(f"- in sequences starting from seeds: {', '.join(A)}")