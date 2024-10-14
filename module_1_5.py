from statistics import multimode

immutable_var = tuple([1, 10, 20.2, 'word'])
print (immutable_var)
# решение пункта 2

#immutable_var[0] = 2
#print (immutable_var)
# TypeError: 'tuple' object does not support item assignment
# Главное свойство кортежа - это невозможность изменить содержимое кортежа
# после его создания

mutable_list =['ma', 'pa', 1, 2]
print (mutable_list)
mutable_list[1] = 'la'
print(mutable_list)

# примеры изменения списка
mutable_list.append(True) # добавить текст
print(mutable_list)
mutable_list.remove('ma') # убрать элемент из списка
