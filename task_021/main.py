# Напишите программу для печати всех уникальных
# значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}]

set_1 = set()

for i in range(len(list_dict)):
    for j in list_dict[i]:
        set_1.add(list_dict[i][j])

print(set_1)