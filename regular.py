import re
pattern=r'\d+'
text="I am vidya @ 33"
match=re.search(pattern,text)
print(match.group())