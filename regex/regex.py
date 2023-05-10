import re

file = input("Enter file name:")
try:
  fh = open(file)
except:
  print('Invalid file')
  quit()
numlist = list()
count = 0
for line in fh:
  line = line.rstrip()
  nums = re.findall('[0-9]+', line)
  for num in nums:
    count += 1
    num = int(num)
    numlist.append(num)
total = sum(numlist)
print(count, total)