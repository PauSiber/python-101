from random import randint
import time

puan=0

while(True):
  bs = randint(1,10)
  ıs = randint(1,10)
  
  if(puan>20):
    bs = bs + 10
    ıs = randint(10,20)

  dogru = bs + ıs
  print(bs,"+",ıs,"=", end=' ')
  suan=time.time()
  cevap = int(input(''))
  süre = time.time() - suan
  
  if(cevap == dogru and süre < 5 ):
    print("Doğru cevap")
  elif(cevap != dogru and süre < 5):
    print("Yanlış cevap")
    break;
  elif(cevap == dogru and süre > 5):
    print("Maalesef yavaşsın")
    break;
  elif(cevap != dogru and süre > 5 ):
    print("Yavaşsın ve yanlış cevap")
    break;
print("Oyun bitti")
