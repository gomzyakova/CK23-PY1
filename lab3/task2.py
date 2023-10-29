# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, sep_=","):
    set_1 = set(group_1.split(sep_))
    set_2 = set(group_2.split(sep_))
    ans = list(set_1.intersection(set_2))
    return sorted(ans)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, sep_="|")