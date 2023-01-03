#Kullanıcıdan isim,yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise yada üniversite olmalıdır.
isim = input ('isminiz: ')
yas = int(input('yaşınız: '))
eğitim = input('eğitim:')

if (yas>=18 ) :
    if (eğitim== 'lise' or eğitim== 'üniversite'):
    print(f'{isim}ehliyet alabillirsin.')
    else:
     print(f'{isim}ehliyet alamazsın eğitim durumun yetersiz.')
else:
    print(f'{isim}ehliyet alamazsın yaşın tutmuyor.')

     
#Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
# 0-24 => 0
#25-44 => 1
#45- 54=> 2
#55-69 => 3
#70-84 => 4
#85-100 =>5
yazılı1= float(input('yazılı1: '))
yazılı2= float(input('yazılı2: '))
sozlu= float(input('sozlu: '))

ortalama= (yazılı1+yazılı2+sozlu)/3

if (ortalama>=0) and (ortalama<25):
    print(f'ortalamanız: {ortalama} notunuz: 0')
elif (ortalama>=25) and (ortalama< 45):
    print(f'ortalamanız: {ortalama} notunuz: 1')  
elif (ortalama>=45) and (ortalama< 55):
    print(f'ortalamanız: {ortalama} notunuz: 2') 
elif (ortalama>=55) and (ortalama< 70):
    print(f'ortalamanız: {ortalama} notunuz: 3')  
elif (ortalama>=70) and (ortalama< 85):
    print(f'ortalamanız: {ortalama} notunuz: 4') 
elif (ortalama>=85) and (ortalama< 100):
    print(f'ortalamanız: {ortalama} notunuz: 5')
else:
         print('yanlış bilgi girdiniz.')
