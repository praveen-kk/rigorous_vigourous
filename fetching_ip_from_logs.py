import re
class fetch_ips:
    def __init__(self, file):
        self.file = file
    def ip_extract(self):
        with open(self.file) as fh:
            fstring = fh.readlines()
        # declaring the regx pattern
        pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
#       initialising list object
        lst = []
        for line in fstring:
            match = pattern.search(line)
            if match:
                lst.append(match.group(0))
        return lst

file = "log"
fetch = fetch_ips(file)
print(fetch.ip_extract())

