from random import randrange
from time import time
class Sort:
  __previousList = []
  __except = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'
      ,'v','w','x','y','z','"','<','>','\'','.',';',':','?','/','+','=','|','\\','_','-','[',']','{'
      ,'}','(',')','`','~','!','@','#','$','%','^','&','*']

  # Memilih algoritma yang akan digunakan
  @staticmethod
  def ChooseAlgorithm(data):
    print('\nData awal\t: ', data)
    while True:
      index = input('Silahkan pilih algoritma yang digunakan:\n  [1] Selection Algorithm\n  [2] Bubble Algorithm\n  Pilihanmu\t? ')
      if index.isnumeric():
        index = int(index); break
      # elif index is None:
      #   pass
    if index == 1:
      Sort.Selection(data)
    if index == 2:
      Sort.Bubble(data)
    
  # Melakukan Swap
  @staticmethod
  def Swap(data1, data2):
    return data2, data1
  
  # Melakukan input data
  @staticmethod
  def InputData():
    while True:
      data = input('Masukkan angka  : ')
      if (data is None) or (data is ''):
        dataLength = input('  Masukkan banyak data  : ')
        data = Sort.RandomData(dataLength); break
      else:
        data = data.lower()
        for ch in Sort.__except:
          data = str.replace(data, ch, ',')
        data = str.split(data, ',')
        print(data.count(''))
        while data.count('') > 0:
          data.remove('')
        i = 0
        while i < len(data):
          data[i] = int(data[i])
          i+=1
        break
      print(data)
    Sort.__previousList = data.copy()
    Sort.ChooseAlgorithm(Sort.__previousList.copy())
  
  # Konfirmasi mencoba sorting lagi atau tidak
  @staticmethod
  def TryAgain():
    while True:
      confirm = input('Coba Lagi (y/N)? ')
      if confirm == 'n' or confirm is '' or confirm is 'N':
        break
      elif confirm == 'y' or confirm is 'Y':
        Sort.ChooseAlgorithm(Sort.__previousList.copy()); break
  
  # Memberikan angka acak
  @staticmethod
  def RandomData(dataLength):
    if not dataLength.isnumeric():
      dataLength = randrange(2, 10)
    else:
      if int(dataLength) < 1:
        dataLength = randrange(2, 10)
    return [randrange(0,100) for i in range(0, int(dataLength))]
  
  # Menggunakan Algoritma Selection
  @staticmethod
  def Selection(data):
    timeStart = time()
    i = 0
    # Pengulangan pertama untuk mendapatkan elemen dengan nilai terkecil
    while i < len(data):
      j = i
      # Pengulangan kedua untuk membandingkan nilai yang belum diurutkan
      while j < len(data):
        if (data[i] > data[j]):
          data[j], data[i] = Sort.Swap(data[j], data[i])
        j+=1
      i+=1
      # Menampilkan Pengulangan yg dilakukan
      if not i >= len(data)-1:
        print('Iterasi ke-'+ str(i) + '\t: ', data)
      elif i is len(data)-1:
        print('Hasil Akhir\t: ', data)
    timeEnd = time()
    print('Waktu yang dibutuhkan : ', timeEnd - timeStart)
    Sort.TryAgain()
  
  # Menggunakan Algoritma Bubble
  @staticmethod
  def Bubble(data):
    timeStart = time()
    i = 1; iterastion = 1
    while True:
      # Pengulangan kedua untuk membandingkan nilai yang belum diurutkan
      if data[i-1] > data[i]:
        data[i-1], data[i] = Sort.Swap(data[i-1], data[i])
        i = 0
      # Menampilkan Pengulangan yg dilakukan
      if not i >= len(data)-1:
        print('Iterasi ke-'+ str(iterastion) + '\t: ', data)
        iterastion+=1
      elif i is len(data)-1:
        print('Hasil Akhir\t: ', data)
        break
      i+=1
    timeEnd = time()
    print('Waktu yang dibutuhkan : ', timeEnd - timeStart)
    Sort.TryAgain()