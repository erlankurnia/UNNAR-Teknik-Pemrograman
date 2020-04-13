from random import randrange
from time import sleep
class Search:
  __data = []
  __except = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'
      ,'v','w','x','y','z','"','<','>','\'','.',';',':','?','/','+','=','|','\\','_','-','[',']','{'
      ,'}','(',')','`','~','!','@','#','$','%','^','&','*', ' ']

  @staticmethod
  def Start():
    print("-"*15,"Program Pencarian dengan Algoritma Binary Search","-"*15,"\n")
    print('\nNama\t: Erlan Kurnia\nNIM\t: 04316038\nProdi\t: Teknik Informatika\n')
    print('*Jika terdapat banyak angka, pisahkan dengan karakter koma \',\'')
    print('*Silahkan dikosongi, jika datanya menggunakan angka acak\n')
    Search.InputData()

  # Melakukan input data
  @staticmethod
  def InputData():
    while True:
      data = input('Masukkan data  : ')
      if (data is None) or (data is ''):
        dataLength = input('  Masukkan banyak data  : ')
        data = Search.RandomData(dataLength); break
      else:
        data = data.lower()
        for ch in Search.__except:
          data = str.replace(data, ch, ',')
        data = str.split(data, ',')
        while data.count('') > 0:
          data.remove('')
        i = 0
        while i < len(data):
          data[i] = int(data[i])
          i+=1
        break
    Search.__data = data.copy()
    Search.Selection(Search.__data)
    Search.Binary(Search.__data)
    Search.TryAgain()
  
  # Memilih algoritma yang akan digunakan
  @staticmethod
  def ChooseAlgorithm(data):
    print('\nData awal\t: ', data)
    while True:
      index = input('Silahkan pilih algoritma yang digunakan:\n  [1] Linear Algorithm\n  [2] Binary Algorithm\n  Pilihanmu\t? ')
      if index.isnumeric():
        index = int(index); break
    if index == 1:
      Search.Linear(data)
    if index == 2:
      Search.Binary(data)
     
  # Melakukan Swap
  @staticmethod
  def Swap(data1, data2):
    return data2, data1
  
  # Memberikan nilai acak pada data array yang jumlahnya juga acak
  @staticmethod
  def RandomData(dataLength):
    if not dataLength.isnumeric():
      dataLength = randrange(2, 10)
    else:
      if int(dataLength) < 1:
        dataLength = randrange(2, 10)
    return [randrange(0,int(dataLength)) for i in range(0, int(dataLength))]
  
  # Konfirmasi mencoba sorting lagi atau tidak
  @staticmethod
  def TryAgain():
    while True:
      confirm = input('Coba Lagi (y/N)? ')
      if confirm == 'n' or confirm is '' or confirm is 'N':
        break
      elif confirm == 'y' or confirm is 'Y':
        Search.Binary(Search.__data); break
  
  # Mengurutkan data
  @staticmethod
  def Selection(data):
    i = 0
    # Pengulangan pertama untuk mendapatkan elemen dengan nilai terkecil
    while i < len(data):
      j = i
      # Pengulangan kedua untuk membandingkan nilai yang belum diurutkan
      while j < len(data):
        if (data[i] > data[j]):
          data[j], data[i] = Search.Swap(data[j], data[i])
        j+=1
      i+=1
    Search.__data = data
    print('\nData awal\t: ', Search.__data)

  # Menggunakan Algoritma Linear Search
  @staticmethod
  def Linear(data):
    pass

  # Menggunakan Algoritma Binary Search
  @staticmethod
  def Binary(data):
    key = ''
    found = False
    index = 0
    first = 0
    last = len(data)-1
    rudand = index
    while not key.isnumeric():
      key = input("Masukkan Angka yg dicari\t: ")
    key = int(key)
    
    while not found:
      rudand = index
      index = (int)((first + last) / 2)
      print("Mencari pada index ke-"+str(index))
      if data[index] == key:
        found = True
        print("  Angka",key,"Ditemukan.")
      elif data[index] < key:
        first = (int)(index)+1
        last = last
      else:
        first = first
        last = index-1
      if index == rudand:
        found = True
        print("  Angka",key,"Tidak ditemukan.")
      sleep(1)
