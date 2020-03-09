from random import randrange
# Memberikan nilai acak pada data array yang jumlahnya juga acak
data = [randrange(0,100) for i in range(0, randrange(2,10))]
print('Data awal\t: ', data); i = 0
# Pengulangan pertama untuk mendapatkan elemen dengan nilai terkecil
while i < len(data):
  j = i
  # Pengulangan kedua untuk membandingkan nilai yang belum diurutkan
  while j < len(data):
    if (data[i] > data[j]):
      temp = data[j]; data[j] = data[i]; data[i] = temp
    j+=1
  i+=1
  # Menampilkan Pengulangan yg dilakukan
  if not i >= len(data)-1:
    print(('Iterasi ke-'+ str(i) + '\t: '), data);
  elif i is len(data)-1:
    print(('Hasil Akhir\t: '), data)