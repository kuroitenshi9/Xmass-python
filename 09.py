'''
Zaznacz prawidłowe odp:

- c.tzinfo is None.

- a is equal to zero.

- d computes the time that has passed since the epoch.

- Can replace the call to datetime.utcnow with datetime.now and will get the same result

- b is equal to 2018-1-2B
'''

from datatime import datatime

a = (datatime.now() - datatime.now()).total_seconds()
b = datatime(2018, 1, 2, 2, 3).strftime("%Y-%m-%d")
c = datatime.now()
d = datatime.utcnow() - datatime(1970, 1, 1, 0, 0, 0)
d2 = datatime.now() - datatime(1970, 1, 1, 0, 0, 0)

print(a)
print(b)
print(c)
print(d)
print(d1)