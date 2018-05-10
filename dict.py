# items = [('name','age'),('tian',23)]
# d = dict(items)
# # del d['age']
# print('name' in d)
people = {
    'Alice':{
        'phone':'2231',
        'addr':'spl'
    },
    'Beth':{
        'phone':'5615',
        'addr':'ypl'
    }
}

lables = {
    'phone':'phone_num',
    'addr':'address'
}
name = input('Name:')
request = input('Phone number(p) or address(a)?')
key = request
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'
person = people.get(name,{})
lable = lables.get(key,key)
result = person.get(key,'not available')
print("{} 's {} is {}.".format(name,lable,result))

