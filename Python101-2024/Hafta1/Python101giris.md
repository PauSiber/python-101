# PausiberPython101


### 1. Hafta: Python ve Programlama Temelleri
---

### 1. Bölüm: Programlama Dillerine Giriş 

#### 1. Programlama Nedir?
Programlama, bilgisayarlara belirli görevleri yapmaları için komutlar vermemizi sağlayan bir süreçtir. Bilgisayarlar kendi başlarına herhangi bir işi yapamazlar; onların anlayabileceği bir dille yazılmış talimatlara ihtiyaç duyarlar. Programlama dilleri, bu talimatları yazmamızı sağlayan araçlardır.

Bilgisayarların anladığı dil makine dilidir. Makine dili, 0 ve 1'lerden oluşur ve insanlar için anlaşılması zordur. Bu nedenle, programlama dilleri insanların okuyup yazabileceği şekildedir. Python gibi programlama dilleri bu açıdan kullanıcılara büyük kolaylık sağlar.
 

#### 2. Programlama Dillerinin Sınıflandırılması
Programlama dilleri, insan diline ne kadar yakın olduklarına göre iki ana kategoriye ayrılır:

- **Yüksek Seviyeli Programlama Dilleri** : Python, Java, C++ ,Ruby gibi diller insan diline yakın olan, bilgisayar donanımından bağımsız şekilde çalışan, yazılması ve anlaşılması daha kolay dillerdir. Bunlar genellikle günlük hayatta karşılaştığımız problemleri çözerken kullanılır.
  
- **Düşük Seviyeli Programlama Dilleri**: Assembly ve makine dili gibi diller donanıma daha yakın çalışır. Bilgisayar donanımı üzerinde daha fazla kontrol sağlarlar, işlemcinin komut setine daha yakındır bu yüzden kod daha hızlı ve verimli çalışabilir ancak anlaşılması ve yazılması zordur.

Python, **yüksek seviyeli ve yorumlayıcı bir dil** olduğu için yazılan kod, satır satır çalıştırılır ve anında geri bildirim alınır. Bu da Python'u öğrenmeyi ve hata ayıklamayı kolaylaştırır.

Derleyiciler, yorumlayıcılara göre daha hızlıdır. Çünkü yorumlayıcılar ilk kod satırından son kod satırına kadar her satırını teker teker yorumlar ve kodun karşılığındaki işlemi gerçekleştirir. Derleyiciler ise kodların tamamını bilgisayar diline çevirir. Eğer hata varsa, tüm hataları programcıya bildirir.

#### 3. Neden Python? 
Python, **veri bilimi, yapay zeka, web geliştirme, otomasyon** ve daha birçok alanda popüler bir dildir. Kullanıcı dostu olması, geniş kütüphane desteği ve basit syntax yapısı ile özellikle yeni başlayanlar için ideal bir dil olarak kabul edilir.
Python birçok platformda kullanilabilir(Windows, Mac, Linux, Raspberry Pi, etc). 
Ayni zamanda Python, prosedürel, nesne yönelimli veya fonksiyonel olarak ele alınabilir.
Instagram, Reddit, Dropbox python ile oluşturulmuştur.

Aşağıda bazı diğer diller ve python ile "Hello World" çıktısının nasıl alındığına dair örnekler var.

##  C/C++                                     
![image](https://github.com/user-attachments/assets/85b12dd3-8b93-4ba8-8321-796cd04a18dc)

## Java
![image](https://github.com/user-attachments/assets/32680554-6da8-4efc-98ee-34a524512566)

## C\#
![image](https://github.com/user-attachments/assets/11ae3622-e058-4f2a-8f70-2852166c4fea)

## Python
![image](https://github.com/user-attachments/assets/6e2ed1f5-df12-41c8-ad2a-7a0a3f98d452)


#### 4. Python Kurulum ve IDE Tanıtımı 
Python’u bilgisayarınıza indirip kurabilirsiniz. Python'un resmi sitesinden bilgisayarınıza uygun dosyayı seçip indirebilirsiniz.
- https://www.python.org/downloads/
  
Ayrıca, kod yazmak için kullanabileceğimiz çeşitli **IDE**'ler (Entegre Geliştirme Ortamları) vardır. En popüler IDE’lerden bazıları:
- **PyCharm**
- **VS Code**
- **Jupyter Notebook**
  
Derste VS Code üzerinden anlatım yapacağız.
- https://code.visualstudio.com/download
Bu linkten VS Code'u indirip kurabilirsiniz.

Eğer derse gelmeden kurmadıysanız ya da problem yaşadıysanız online editörler üstünden dersi takip edebilirsiniz:
- https://www.online-python.com/
---

### 2. Bölüm: Python’a Giriş 

#### 1. Python’u Tanıyalım 
Python’u bir dil olarak tanıdıktan sonra, bu dili nasıl kullanacağımızı öğrenelim. Python, hem küçük projeler hem de büyük çaplı sistemler için kullanılabilir. Web uygulamaları, veri analizleri, otomasyon görevleri gibi çeşitli alanlarda Python sıklıkla tercih edilir.

Basit bir "Merhaba Dünya" programı yazalım. Python’da bir program yazmak ve çalıştırmak oldukça basittir:

```python
print("Merhaba Dünya!")
```


Bu kod, ekrana **Merhaba Dünya!** yazdırır. Python'un syntax'ı (yazım kuralları) oldukça basit ve okunaklıdır.

Python'da bir sonraki satıra geçmek için \n ifadesi kullanılır.
```python
print("Merhaba\nDünya")
```

#### 2. Basit Bir Python Programı Yazalım 
Python’da veri tiplerine geçmeden önce, basit bir program yazalım. İlk olarak, kullanıcıdan veri almayı öğrenelim. `input()` fonksiyonu ile kullanıcıdan giriş alabiliriz:

```python
isim = input("Adınızı girin: ")
print("Merhaba, " + isim)
```

Bu program, kullanıcının girdiği ismi alır ve ekrana "Merhaba, [isim]!" yazar.

---

### 3. Bölüm: Python’da Veri Tipleri ve Temel İşlemler

#### 1. Python Temel Veri Tipleri 
Python’da birkaç temel veri tipi vardır. Bunlar:

- **`int`** (Tam Sayı): Tamsayılar, örneğin `5`, `10`, `-3`.
- **`float`** (Ondalıklı Sayı): Ondalıklı sayılar, örneğin `3.14`, `0.5`, `-1.23`.
- **`str`** (String, Karakter Dizisi): Metin verileri, örneğin `"Python"`, `"Merhaba"`.
- **`bool`** (Boolean, Doğru/Yanlış): Mantıksal değerler, `True` veya `False`.

Örnek olarak bazı veri tiplerini inceleyelim:

Python'da değişken tanımlarken veri tipini başta belirtmek gerekmez Bu durum pythonun type-safety'e uymadığını gösterir.

```python
a = 5  # int
b = 3.14  # float
c = "Merhaba"  # str
d = True  # bool
```
Veri tipini öğrenmek için `type()` fonksiyonunu kullanabiliriz:
```python
print(type(a))  # int
print(type(b))  # float
print(type(c))  # str
print(type(d))  # bool
```

#### 2. Veri Tipi Dönüşümleri 
Python’da bir veri tipini diğerine dönüştürebiliriz. Örneğin, bir string’i integer’a çevirebiliriz:
```python
x = "10"
y = 5
print(int(x) + y)  # string -> int dönüşümü
```

Bu kodda, `"10"` string değeri `int()` fonksiyonu ile integer’a çevrilir ve ardından `y` ile toplanır.

#### 3. Matematiksel İşlemler 
Python’da temel matematiksel işlemler şunlardır:

- **Toplama**: `+`
- **Çıkarma**: `-`
- **Çarpma**: `*`
- **Bölme**: `/`
- **Üs Alma**: `**`
- **Mod Alma**: `%`

Örnek:
```python
a = 10
b = 3
print(a + b)  # toplama
print(a - b)  # çıkarma
print(a * b)  # çarpma
print(a / b)  # bölme
print(a ** b)  # üs alma
print(a % b)  # mod alma
```

---

### 4. Bölüm: Python’da String İşlemleri 

Stringler 3 farklı şekilde oluşturulabilir:

```python
my_string = "Python'a Hoş geldin!"
another_string = ' Kırmızı tilki çitten atladı.'
a_long_string = '''Bu bir
multi-line string, birden
fazla satırı kapsıyor.'''
```

Üç tırnak işareti (üç tek tırnak veya üç çift tırnak) kullanarak birden fazla satıra yayılabilen stringler oluşturabilirsiniz. Yazdırdığınızda satır sonları korunur. Tek tırnakları bir string içinde kullanmanız gerekiyorsa, çift tırnakla sarabilirsiniz. 
Aşağıdaki örneklere bakın:

```python
my_string = "I'm a Python programmer!"
otherString = 'The word "python" usually refers to a snake'
tripleString = """Here's another way to embed "quotes" in a string"""
```

#### 1. String Birleştirme ve Dilimleme 
Stringler, metin verilerini temsil eder. Python’da string birleştirme ve dilimleme işlemleri oldukça basittir:

- **Birleştirme**: String’ler `+` operatörü ile birleştirilebilir:
  ```python
  isim = "Python"
  yil = 2024
  print(isim + " " + str(yil))  # Python 2024
  ```

- **Dilimleme**: String içindeki belirli karakterlere erişebiliriz:
  ```python
  kelime = "Python"
  print(kelime[0:3])  # "Pyt"
  ```

#### 2. String Metodları 
Python, string manipülasyonu için birçok metod sunar. En çok kullanılan string metodları şunlardır:

- **`upper()`**: Tüm karakterleri büyük harfe çevirir:
  ```python
  isim = "python"
  print(isim.upper())  # "PYTHON"
  ```

- **`lower()`**: Tüm karakterleri küçük harfe çevirir:
  ```python
  isim = "PYTHON"
  print(isim.lower())  # "python"
  ```

- **`strip()`**: Başında ve sonunda bulunan boşlukları siler:
  ```python
  isim = "  Python  "
  print(isim.strip())  # "Python"
  ```

- **`replace()`**: Sectiginiz harfi istediginiz harf ile degismenizi saglar:
  ```python
  isim = "  Python  "
  print(isim.replace('o','a'))  # "Pythan"
  ```
  
- **`len()`**: Stringimizin uzunlugunu verir:
  ```python
  isim = "  Python  "
  print(len(isim))  # "6"
  ```

- **`format()`**: belirtilen degerleri yer tutucularin icine ekler :
  ```python
  txt1 = "Ben {yil} yildir {dil} yaziyorum!".format(yil = 3 , dil = "Python")
  txt2 = "Ben {0} yildir {1} yaziyorum!".format(3 , "Python")
  txt3 = "Ben {} yildir {} yaziyorum!".format(3 ' "Python")
  ```

  Python 3.6 ile f-strings'i tanıtmıştır.Bu özellik ile format methodu ile yaptığımız gibi stringleri daha rahat bir şekilde biçimlendirebiliriz.
  
```python
 isim = input("İsminizi girin: ")
 yas = input("Yaşınızı girin: ")
 print(f"Ben {isim}. {yas} yaşındayım")
 ```
5. Bölüm: Uygulama

#### 1. Uygulama Örnekleri 

1. Kullanıcıdan iki sayı alın ve bu sayılar üzerinde toplama, çıkarma, çarpma ve bölme işlemleri yapın:

   ```python
   x = int(input("Birinci sayıyı girin: "))
   y = int(input("İkinci sayıyı girin: "))
   print("Toplam:", x + y)
   print("Fark:", x - y)
   print("Çarpım:", x * y)
   print("Bölüm:", x / y)
   ```

2. Girilen bir string üzerinde `upper()`, `lower()`, `strip()`, `len()`, `format()` gibi metodları kullanarak string’i manipüle edin.
    ```python
    isim = input("İsminiz nedir? ")
    yas = input("Yaşınız nedir? ")
    print(f"Merhaba {isim}, {yas} yaşındasınız.")
    ```

3. Tanımlanan iki sayı için boolean ifadelerin nasıl çalıştığını görelim:

    ```python
    a=5
    b=4
    print(a>b) # "true"
    print(a=b) # "false"
    print(a<b) # "false"
    ```
