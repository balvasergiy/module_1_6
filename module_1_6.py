my_dict={'Petr': 1980, 'ivan': 2000, 'Elena': 1988}
print(my_dict)
print(my_dict['Elena'])
print(my_dict.get('Ruslan'))
my_dict.update({'Marina': 2001, 'Irina': 2002})
print(my_dict)
my_dict.pop('Petr')
print(my_dict)
my_dict['Petr']=1980 # прищлось добавить снова, чтобы получить значение, без доб. выдает ошибку!
print(my_dict)
a=my_dict.pop('Petr')
print(a)
print(my_dict)
my_set_={1,2,3,4,5,'Apple',1,2,3,4}
print(my_set_)
my_set_.update({'True','False'})
print(my_set_)
my_set_.discard('False')
print(my_set_)
