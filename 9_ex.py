# import os
#
# n = os.path.join("Users","takur","OneDrive","デスクトップ","test.xlsx")
# print(n)
#
# with open("../test.xlsx","r") as f:
#     r = f.read()
# print(r)

n = input("出身地は？：")
with open("ex.txt","w",encoding="utf-8") as f:
    f.write(n)

