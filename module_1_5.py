immutable_var = 1, 2.2, 'Lango', True
print (immutable_var)
#immutable_var[0] = 2   #кортеж - список неизменных данных. После ошибки, код не выполняется, поэтому была закомментирована строка
mutable_list = [1, 2.2, 'Langost', False]
print (mutable_list)
mutable_list[:]= [2.2, 1, 'Mango', True, 'mission_completed']
print (mutable_list)
