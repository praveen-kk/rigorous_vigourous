# import re
# import collections


# def log_reader(filename):
#     with open(filename) as f:
#         log = f.read
#         pattern = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
#         ip_list = re.findall(pattern, log)
#         return ip_list
    

# pattern = 'a^..s$'



# if __name__ == '__main__':
#     print(log_reader('log'))

import subprocess
for ping in range(0, 100):
    address = "127.0.0." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0
    


