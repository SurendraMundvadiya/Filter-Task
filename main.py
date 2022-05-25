import re

with open('exclude-words.txt', 'r', encoding='utf-8') as f:
    rm = set(f.read().split("\n"))
f.close()


with open('Page1.txt', 'r', encoding='utf-8') as f1:
    l1 = f1.read().replace('\n', ' ').split(" ")
f1.close()

with open('Page2.txt', 'r', encoding='utf-8') as f2:
    l2 = f2.read().replace('\n', ' ').split(" ")
f2.close()

with open('Page3.txt', 'r', encoding='utf-8') as f3:
    l3 = f3.read().replace('\n', ' ').split(" ")
f3.close()
l1 = list(set([i for i in l1 if i not in rm]))
l2 = list(set([i for i in l2 if i not in rm]))
l3 = list(set([i for i in l3 if i not in rm]))

print(l1)

d = dict()
for i in l1:
    if i in d:
        d[i] = d[i]+', 1'
    else:
        d[i] = '1'

for i in l2:
    if i in d:
        d[i] = d[i]+', 2'
    else:
        d[i] = '2'

for i in l3:
    if i in d:
        d[i] = d[i]+', 3'
    else:
        d[i] = '3'

with open('Index.txt', 'w', encoding='utf-8') as Ifile:
    for k, v in d.items():
        string = re.sub(r'[^A-Za-z]+', '', k)
        if string != '':
            Ifile.write(string + ' ' + ':' + ' ' + v + '\n')
Ifile.close()
