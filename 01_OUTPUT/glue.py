def principal_period(s):
    i = (s + s).find(s, 1, -1)
    return None if i == -1 else s[:i]


items = ['占', '쏙', '옙']
result = list(map(lambda i: i.encode("euc-kr").hex(), items))
str = ''.join(result)
str = principal_period(str)
result2 = ['0x' + str[i]+str[i+1] for i in range(0, len(str), 2)]
print(result2)
str2 = ''.join(result2)

ipdb.set_trace()  ######### Break Point ###########
print('�'.encode('utf-8').hex())

("{0:o}".format(166)).encode('utf-8').decode('utf-8')


print((b'\xef\xbf\xbd').decode('utf-8'))
