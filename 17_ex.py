import re

sentence = "The ghost that says boo haunts the loo"
ans = re.findall(".oo", sentence)
print(ans)
