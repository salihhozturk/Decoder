import sys
#------------------------------------------------------------------------------
def Base36():
    try:
        cevap =''
        a = int(a)
        l=[]
        sonuc=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        i=1
        while(i==1):
            kalan=(a%36)
            l.append(kalan)
            bolum=int(a/36)
            if (bolum>=36):
                i=1
                a=bolum
            else:
                l.append(bolum)
                i=0
            
        l.reverse()
        uzunluk=len(l)
        for i in range(uzunluk):
            b=l[i]
            cevap += sonuc[b]
        print(cevap)
    except:
        print("Base36 ile uyuşmadı !!!")
        return 1
#------------------------------------------------------------------------------
def Base64():
    try:
        o , girdi = sys.argv
        l=[]
        m=[]
        v=[]
        z=[]
        c=[]
        cevap = ''
        sonuc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
               "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
               "0","1","2","3","4","5","6","7","8","9","+","/","="]
        l=girdi
        a=len(l)
        
        for i in range(a):
            for j in range(64):
                if l[i]==sonuc[j]:
                    index=sonuc.index(sonuc[j])
                    break
                else:
                    continue 
            bolum=0
            if (index<=31):
                dongu=5
                if (index<=15):
                    dongu=4
                    if (index<=7):
                        dongu=3
                        if (index<=3):
                            dongu=2
                            if (index<=1):
                                dongu=1
                            else:
                                print("hata var")
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                dongu=6
            
            for i in range(dongu):
                mod=index%2
                index=int(index/2)
                m.append(mod)
            m.reverse()
            kontrol=(6-dongu)
            for i in range(kontrol):
                m.insert(i,0)
            for i in range(6):
                v.append(m[i])
            m.clear()    
        
        dongutwo=(len(v))
        bolum=int(dongutwo/8)
        for i in range(bolum):
            for j in range(8):
                z.append(v[j])
            z.reverse()
            toplam=0
            for i in range(8):
                deger=z[i]
                if (deger!=0):
                    carpım=(deger*(2**i))
                    toplam=toplam+carpım
                else:
                    continue
            c.append(toplam)
            for j in range(8):
                v.pop(0)
                z.pop(0)

        for i in range(len(c)):
            cevap += chr(c[i])
        print("Base64 Decryption--->",cevap) 
    except:
        print("Base64 ile uyuşmadı !!!")
        return 1
#------------------------------------------------------------------------------
def vigenere():
    try:   
        o , cevap , key = sys.argv
        string = ''
        key = key.lower()
        sayac = 0
        a = cevap
        
        while len(key) < len(cevap):
            key += key[sayac]
            sayac += 1
        for i in range(0,(len(cevap))):
            if ord(cevap[i]) <= 90 and ord(cevap[i]) >= 65:
                kontrol = ord(cevap[i]) - ((ord(key[i])+11)%27)
                if kontrol < 65:
                    string += chr(kontrol + 26)
                else :
                    string += chr(kontrol)
            else :
                kontrol = ord(cevap[i]) - ((ord(key[i])+11)%27)
                if kontrol < 97:
                    string += chr(kontrol + 26)
                else:
                    string += chr(kontrol)
        print("Vigenere Cipher Decryption-->",string)
    except:
        print("Vigenere Cipher ile uyuşmadı !!!")
        return 1
#------------------------------------------------------------------------------
def AsciiToText():
    try:
        o , x = sys.argv
        string = ''
        y = len(x) // 3
        for i in range(0,y):
            string += chr( int ( x[ (i*3) : ((i+1)*3) ]))
        print("Ascii To Text-->",string)
    except:
        print("Ascii To Text ile uyuşmadı !!!")
        return 1
#------------------------------------------------------------------------------
def BinaryToText():
    try:
        o , x = sys.argv
        uzunluk = len(x) // 8
        veri = ' '
        if uzunluk == 0 :
            print("Girilen sayının çevirisi =",char(int(x,2)))
        else:
            for i in range(0,uzunluk):
                veri = veri + chr(int((x[(i*8):((i+1)*8)]),2))
        print("Binary To Text-->",veri) 
    except:
        print("Binary To Text ile uyuşmadı !!!")
        return 1
#------------------------------------------------------------------------------
def hexa():
    try :
        o , girdi = sys.argv
        a = girdi
        string =''
        
        for i in range (0 , int (len (girdi)/2)) :
            string += chr (int ((girdi [(i*2):((i+1)*2)] ) , 16))
        print("Hexadecimal to Text-->",string)
    except:
        print("Hexadecimal To Text ile uyuşmadı !!!")
        return 1
#------------------------------------------------------------------------------
def xor_func():
    try: 
        o , girilen , key = sys.argv
        uzunluk = len(girilen)
        sonuc = ""
        
        for i in range(0,uzunluk):
            current = girilen[i]
            current_key = key[i%len(key)]
            sonuc += chr(ord(current) ^ ord(current_key))
        print("XOR-->", sonuc )
    except:
        print("XOR ile uyuşmadı !!!")
        return 1
#------------------------------------------------------------------------------
def sezar():
    try:
        o,metin,anahtar = sys.argv
        anahtar = int(anahtar)
        yenimetin = ""
        deger=0
        for i in range(0,len (metin)):
            deger = ord (metin[i]) - anahtar
            if(ord (metin[i]) < 123 and ord (metin[i]) > 96):
                while(deger<97):
                    deger+=26
                yenimetin += chr(deger)
            else:
                while(deger<64):
                    deger+=26
                yenimetin += chr(deger)
        print("Caesar Cipher-->",yenimetin)
    except:
        print("Caesar Cipher ile uyuşmadı !!!")
        return 1
#------------------------------------------------------------------------------            
print("Decryptionsss")
xor_func()
vigenere()
hexa()
BinaryToText()
AsciiToText()
Base36()
Base64()
sezar()