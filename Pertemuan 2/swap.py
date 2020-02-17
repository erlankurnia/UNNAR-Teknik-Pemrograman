teks1 = input("Masukkan Sembarang Teks 1: ")
teks2 = input("Masukkan Sembarang Teks 2: ")

def swap(teks1, teks2):
  return teks2, teks1

def swap2(teks1, teks2):
  temp = teks1
  teks1 = teks2
  teks2 = temp
  return teks1, teks2

print("\tSebelum di Swap :",teks1, teks2)
teks1, teks2 = swap(teks1, teks2)
# teks1, teks2 = swap2(teks1, teks2)
print("\tSetelah di Swap :",teks1, teks2)