# TODO Напишите функцию find_common_participants
def find_common_participants(p,s,c=','):
    p1=p.split(c)
    s1=s.split(c)
    s2=set(s1)
    p2=[]
    for i in p1:
        if i in s2:
            p2.append(i)
    p2.sort()
    return p2

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
