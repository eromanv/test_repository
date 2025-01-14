my_dict = {'Alex' : 1989, 'Oly' : 2000, 'Anton' : 2001}
print(my_dict)
print(my_dict.get('Oly'))
print(my_dict.get('Lena'))
my_dict.update({'Kolya' : 2003, 'Nadya' : 2005})
my_dict.pop('Anton')
print(my_dict)









my_set = {1, 2, 3, 'четыре' , (3.0)}
print(my_set)
my_set.update([5], {6})
print(my_set)
my_set.discard(3)
print(my_set)