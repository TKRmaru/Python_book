films = ["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ"]
for i in films:
    print(i)
#
# for i in range (25,51):
#     print(i)

for i, g in enumerate(films):
    print(str(i) + ":" + films[i])
    print(i)
    print(g)


number = [10,20,30,40,50,60]
while True:
    n = input("数字を予想するか、qで終了してください：")
    if n == "q":
        break
    try:
        n = int(n)
    except ValueError:
        print("数字を入力するか、qで終了します。")
    if n in number:
        print("正解！")
    else:
        print("不正解！")


list1 = [8,19,148,4]
list2 = [9,1,33,83]
answer = []
for i in list1:
    for j in list2:
        answer.append(i*j)
print(answer)