# # sed -nr '/Failed/{s/.*([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*/\1/;p}'| sort | uniq -c
# cmd = '''while read -r x;
#    do ping -c 3 "$x" | grep 'min/avg/max'
#    done <hosts.txt'''
#
# # Trivial but horrible
# results = subprocess.run(
#     cmd, shell=True, universal_newlines=True, check=True)
# print(results.stdout)



import re

with open(r"C:\Users\praveen\PycharmProjects\rigrous_vigrous\ip_address") as fh:
    fstring = fh.readline()
    print(fstring)
    # row = 'today,2008-03-24,food,2012-08-12,nice,5632'
    # txt = re.search(r'\d{4}-\d{2}-\d{2}.*\d{4}-\d{2}-\d{2}', row)[0]
    # print("text is "+txt)
    # # print(fstring)
    # pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    pattern = re.search(r'(^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', fh)[0]
    print(pattern)

# pattern = regex.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.d{1,3})')
# print(pattern.search(fstring))

lst = []
for line in fstring:
    list.append(pattern.search(line[0]))
print(lst)



