import os
fname=str(input("Enter the File Name: "))
if len(fname) == 0:
    print("Error, Enter the File Name")
    exit()
c1='sudo unshadow /etc/passwd /etc/shadow >'+fname
cpath = os.getcwd()
if os.path.exists(cpath and fname) is True:
    print("\nThis is FILE Already Exist")
    exit()
else:
    os.system(c1)
c2="john --show ".__add__(fname)
os.system(c2)
test1 = str(input("\nyou got a Password(y/n)"))
if 'yes'.startswith(test1.lower()):
    print("\nFollow for more https://www.instagram.com/jutrmraja/")
else:
    c3="john --format=crypt ".__add__(fname)
    os.system(c3)
