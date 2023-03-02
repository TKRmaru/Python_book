musicians = ["Jason Mraz", "Zedd", "Skrilex"]

places = ("ny", "paris", "miran")

personal = {"height": 168, "weight": 60, "color": "orange"}
n = input("入力してください：")
if n in personal:
    ans = personal[n]
    print(ans)
else:
    print("false")
