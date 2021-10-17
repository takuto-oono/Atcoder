print('Hello_Python')

def add_0(_id):
    _id = '0' * (6 - len(_id)) + _id
    return _id

print(add_0('45'))
print(add_0('111111'))