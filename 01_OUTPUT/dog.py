# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|


li = ['|', '\\', '_', '/', 'q', 'p', '}', '(', '0', ')', '"', '^', '`', '=']
print(li[0] + li[1] + li[2] + li[3] + li[0] + '\n' +
      li[0] + li[4] + ' ' + li[5] + li[0] + ' ' * 3 + li[3] + li[6] + '\n' +
      li[7] + ' ' + li[8] + ' ' + li[9] + li[10] * 3 + li[1] + '\n' +
      li[0] + li[10] + li[11] + li[10] + li[12] + ' ' * 4 + li[0] + '\n' +
      li[0] * 2 + li[2] + li[3] + li[13] + li[1] * 2 + li[2] * 2 + li[0])
