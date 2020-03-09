import random

def desteYap():
  renkL = ["♥️","♦️","♣️","♠️"]
  renk = [i for i in range(2,11)]
  renk.insert(0, "A")
  renk.append("J")
  renk.append("Q")
  renk.append("K")
  deste = []
  for i in renkL:
    for j in renk:
      deste.append(str(j)+i)
  random.shuffle(deste)                     #Karıştırdı
  return deste
  
def kartVer(deste):
  verilecek = random.sample(deste,4)        #Random 4 kart verir.
  for i in verilecek:
    if i in deste:
      deste.remove(i)                       #Verilen kartları desteden çıkarır.
  return verilecek                          #Verilen kart listesini return'ler

def at(el):

  index = input('Atılcak kart:')
  while( (not index.isdigit()) or (int(index) < 1 or int(index) > len(el))):    #elden fazla sayı ve karakter girmesin
    index = input('Lütfen geçerli sayı girin')

#  index=1

  index = int(index)-1                                                    
  #-1 index 0'dan başladığından
  return el.pop(index)                                                    #Atılacak kartı elden çıkartır ve return'ler

def bastır(liste):
  for i in liste:
    print(i,end='')

def tur(el,yer,Al,isim):
  print("Yer:\t\t\t\t", yer)
  print(isim," Oyuncusunun")
  print("\t\tAldığı kartlar:\t\t", Al)
  print("\t\tElindeki :\t\t\t", el)
#  print("\t\t\t\t\t\t\t",[str(i)+"." for i in range(1,len(el)+1)])             #Kart indexlerini bastırır.
  check = at(el)                                       #Atılacak kartı ister
  print("\t\tAtılan kart: ",check)
  yer.append(check)
  if (check[0] == yer[len(yer)-2][0]) or check[0]=="J":                   #Eğer yerdeki son kağıt atılana eşitse
    Al.extend(yer)
    print("\t\tAldığı kartlar: ", [i for i in Al])
    yer = yer.clear()
    yer = []
  

def puanHesap(deste):
  puan = 0
  kartSayisi = 0
  for i in deste:
    if(i[0] == '2'):
      if(i[1]== '♣'):
        puan +=2
    elif(i[:2] == '10'):
      if(i[2] == '♦'):
        puan +=3
    elif(i[0] == "A"):
      puan += 1
    elif(i[0] == "J"):
      puan += 1

  for i in deste:
    if i != ' ':
      kartSayisi += 1
  return(kartSayisi,puan)

oyuncu1="Mehmet"
oyuncu2="Emrullah"
oyuncu1=input('İsminizi girin:')
oyuncu2=input('İsminizi girin:')
o1Al=[]
o2Al=[]
deste = desteYap()

yer = kartVer(deste)
while(len(deste) != 0):
  print("Kalan kart sayısı: ", len(deste))
  D1 = kartVer(deste)
  D2 = kartVer(deste)
  while(len(D1) > 0 or len(D2) > 0):
    tur(D1,yer,o1Al,oyuncu1)
    tur(D2,yer,o2Al,oyuncu2)

print("\n\n\n")
print(puanHesap(o1Al))
print(puanHesap(o2Al))
