import re
with open('pp.txt','r',encoding='utf-8') as f:
    str=f.read()
print(type(str))
# str="<e s a>aa "
pat = re.compile(r'<[ -/"<>=\w]*>')
new_str = pat.sub('\n',str)
print(new_str)