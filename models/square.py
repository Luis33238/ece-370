import os
boxnumber = 0
x = 0
y = 0
stringx = str(x)
while x < 50:
    os.system('bash script ' + str(x) + ' ' + str(y) + ' ' + str(boxnumber))
    x = x + 2
    boxnumber = boxnumber + 1
x = 49
y = 1
while y < 50:
    os.system('bash script ' + str(x) + ' ' + str(y) + ' ' + str(boxnumber))
    y = y + 2
    boxnumber = boxnumber + 1
y = 49
x = 47
while x > 0:
    os.system('bash script ' + str(x) + ' ' + str(y) + ' ' + str(boxnumber))
    x = x + -2
    boxnumber = boxnumber + 1
x = 0
y = 48
while y > 1:
    os.system('bash script ' + str(x) + ' ' + str(y) + ' ' + str(boxnumber))
    y = y + -2
    boxnumber = boxnumber + 1
