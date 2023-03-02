a = "カミュ"
print(a[0])
print(a[1])
print(a[2])

# what = input("何を：")
# whom = input("誰に：")
# b = "私は昨日{}を書いて、{}に送った！".format(what,whom)
# print(b)

print("aldous Huxley was born in 1894.".title())

c = "どこで？ だれが？ いつ？"
c = c.split(" ")
print(c)

words = ["The","fox","jumped","over","the","fence","."]
words = " ".join(words[:6])+(words[6])
print(words)

d = "A screaming comes across the sky."
d = d.replace("s","$")
print(d)

e = "Hemingway".index("m")
print(e)

f = "He said 'yes we can!'."
print(f)

g = "three"
print(g+g+g)
print(g*3)

h = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(h[:11])
print(h[12:])
