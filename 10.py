
'''
Zaznacz prawidłowe odpowiedz/i: 

The first snippet leaves the file open whereas the second does not.

The second snippet iterates more efficiently through the file.

The second snippet opens the file for reading and writing blocks whereas the first only for reading.

The second snippet opens the file for reading and writing blocks whereas the first only for reading.

None of above
'''
#first snippet
with open('file.txt', 'r') as f:
	for line in f:
		print(line)

#second snipped
f = open('file.txt', 'rb')
for line in f.xreadlines():
	print(line)
f.close()

