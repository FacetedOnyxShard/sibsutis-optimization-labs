from fraction import Fraction


support_element_idx = int(input())
support_element_idx -= 1

input_line = list(map(Fraction.to_fraction, input().split()))

result = []
for element in input_line:
    element = element / input_line[support_element_idx]
    result.append(element)

for e in result:
    print(e, end=" ")
print()
