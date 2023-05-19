import re

regex = re.compile('\s+')

m = re.search('(?<=abc)def', 'abcdef')
#
print(m.group(0))

result = re.match(r'First', 'First Second Third')
print(result)
print(result.group(0))
# OK
result = re.match(r'Second', 'First Second Third')
print(result)
# None

result = re.search(r'First', 'First Second Third, First Second Third')
print(result.group(0))

result = re.findall(r'First', 'First Second Third, First Second Third')
print(result)
#re.split()
result = re.split(r'i', 'First Second Third, First Second Third')
print(result)
temp = 'First Second Third, First Second Third'
x = re.split("\s", temp)
print(x)
x = re.split(r'i', temp,maxsplit=1)
print(x)
x = re.split("\s", temp,maxsplit=1)
print(x)


result = re.sub(r'India', 'the World', 'AV is largest Analytics community of Indiaics community of India')
print (result)

result = re.sub(r'New-York', 'London', 'New-York is a capital of UK')
print (result)


result = re.sub(r'New-York', 'London', 'New-York is a capital of UK and New-York is heart of UK',count=1)
print (result)

result = re.findall(r'\S', 'New-York is a capital of UK')
print (result)