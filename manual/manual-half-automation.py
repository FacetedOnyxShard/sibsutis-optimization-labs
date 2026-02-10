from fraction import Fraction

support_line_string = "-7 5 4 1 -1 -96"
support_element_idx = 1
support_element_idx -= 1

support_line_str = support_line_string.split()
support_element_str = support_line_str[support_element_idx]

support_element = Fraction.to_fraction(support_element_str)
support_line = list(map(Fraction.to_fraction, support_line_str))

input_line = list(map(Fraction.to_fraction, input().split()))
line_element = input_line[support_element_idx]

result = []

for i, current_element in enumerate(input_line):
    if i == support_element_idx:
        result.append(0)
        continue

    current_element = current_element - Fraction(
        line_element * support_line[i], support_element
    )
    result.append(current_element)

for element in result:
    print(element, end=" ")
print()
