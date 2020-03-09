from random import randrange
data = []; i = 0
data = [randrange(0,100) for i in range(0, randrange(2,10))]
print('Data awal\t: ', data); i = 0
while i < len(data):
  j = i
  while j < len(data):
    if (data[i] > data[j]):
      temp = data[j]
      data[j] = data[i]
      data[i] = temp
    j+=1
  print(('Iterasi ke-'+ str(i+1) + '\t: '), data); i+=1