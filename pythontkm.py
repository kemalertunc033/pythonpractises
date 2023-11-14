import random
lst = ["taş","kağıt","makas"]
print("taş kağıt makas oyununa hoşgeldiniz")
print("KURALLAR")
print("taş>makas,kağıt>taş,makas>kağıt")
print("Oyun siz 'bitir' yazdığınızda veya oyunculardan birinin 3 puan ulaştıktan sonra 2 farkla galibiyeti sonucu biter")
print("NOT:5 puan alırsanız veya kaybederseniz de oyun biter.")
print("İyi Eğlenceler")

blg = 0
oync = 0

while blg<5 and oync<5:
    tkm = input("1=> Taş , 2=> Kağıt , 3=> Makas : ")
    tkm = tkm.lower()
    btkm =random.choice(lst)
    
    if tkm==btkm:
        print("Bilgisayar ",btkm," seçti")
        print("Maalesef bu tur puan alamadınız ")
        print("Durum siz: ",oync," Bilgisayar : ",blg)
        
    elif (tkm==("taş" or "tas") and btkm=="makas") or (tkm=="makas" and btkm==("kağıt" or "kağit")) or (tkm==("kağıt" or "kağit") and btkm==("taş" or "tas")):
        print("Bilgisayar ",btkm," seçti")
        print("Bir puan aldınız")
        oync = oync+1
        print("Durum siz: ",oync," Bilgisayar : ",blg)
        
    elif (btkm==("taş" or "tas") and tkm=="makas") or (btkm=="makas" and tkm==("kağıt" or "kağit")) or (btkm==("kağıt" or "kağit") and tkm==("taş" or "tas")):
    
        print("Bilgisayar ",btkm," seçti")
        print("Maalesef bu tur puan alamadınız")
        blg = blg+1
        print("Durum siz: ",oync," Bilgisayar : ",blg)
        
    elif tkm==("bitir" or "bıtır"):
        print("Oyunu bitirdiniz.")   
        print("Durum siz: ",oync," Bilgisayar : ",blg)
        
    else:
        print("Tanımsız kelimme girdiniz  lütfen tanımlı kelimelerle devam ediniz")
    if oync+1<blg and blg>=3:
        print("Üzgünüm kaybettiniz.")
        
    elif oync>blg+1 and oync>=3:
        print("tebrikler kazandınız.")
        