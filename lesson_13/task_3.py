#Создайте функцию honest, которая принимает произвольный список, а возвращает список, состоящий только из четных элементов. Список от 0 до 20 создайте любым способом.
def honest(lst):
    return [a for a in lst if a % 2 == 0]
mlist = list(range(21))
print(honest(mlist))