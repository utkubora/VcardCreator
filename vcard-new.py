import pandas as pd
import random
import sys
from PyQt5 import  QtWidgets
import os


class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.dosya = QtWidgets.QLabel(self)
        self.dosya.setText('Dosya adini giriniz : ')
        self.yazi_alani = QtWidgets.QLineEdit()
        self.dosya1 = QtWidgets.QLabel(self)
        self.dosya1.setText('Sütun adlarini giriniz : ')
        self.yazi_alani2 = QtWidgets.QLineEdit()
        self.dosya2 = QtWidgets.QLabel(self)
        self.dosya2.setText('isim - Soyisim kaçinci sütunda giriniz : ')
        self.yazi_alani3 = QtWidgets.QLineEdit()
        self.dosya3 = QtWidgets.QLabel(self)
        self.dosya3.setText('Numara kaçinci sütunda giriniz : ')
        self.yazi_alani4 = QtWidgets.QLineEdit()
        self.dosya4 = QtWidgets.QLabel(self)
        self.dosya4.setText('V-card dosya ismini giriniz : ')
        self.yazi_alani5 = QtWidgets.QLineEdit()
        self.dosya7 = QtWidgets.QLabel(self)
        self.dosya7.setText('Vcard da kaç kişi bulunsun : ')
        self.yazi_alani7 = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdir = QtWidgets.QPushButton("V-card'i oluştur.")

        self.dosya5 = QtWidgets.QLabel(self)
        self.dosya5.setText('Writed by UTKU BORA')

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.dosya)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.dosya1)
        v_box.addWidget(self.yazi_alani2)
        v_box.addWidget(self.dosya2)
        v_box.addWidget(self.yazi_alani3)
        v_box.addWidget(self.dosya3)
        v_box.addWidget(self.yazi_alani4)
        v_box.addWidget(self.dosya4)
        v_box.addWidget(self.yazi_alani5)
        v_box.addWidget(self.dosya7)
        v_box.addWidget(self.yazi_alani7)
        v_box.addWidget(self.dosya7)
        v_box.addWidget(self.yazi_alani7)
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.yazdir)
        v_box.addLayout(h_box)
        v_box.addWidget(self.dosya5)
        v_box.addStretch()

        self.setLayout(v_box)



        self.temizle.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)

        self.setWindowTitle('V-card Yapici')
        self.setGeometry(100,100,500,500)

        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Temizle":
            self.yazi_alani.clear()

        else:
            print(self.yazi_alani.text())
            file1 = self.yazi_alani.text()
            names = self.yazi_alani2.text()
            print(names)
            names = names.split('*')
            degone = int(self.yazi_alani3.text()) - 1
            degtwo = int(self.yazi_alani4.text()) - 1
            kolay = " " + self.yazi_alani5.text()
            loop = int(self.yazi_alani7.text())
            """names = ['Zaman damgasi','Adiniz - Soyadiniz','Telefon Numaraniz','Mail Adresiniz','E-posta yazarken en çok zorlandiğiniz konu?','Üniversite öğrencisi misiniz?']"""
            """ Zaman damgasi*Adiniz - Soyadiniz*Telefon Numaraniz*Mail Adresiniz*E-posta yazarken en çok zorlandiğiniz konu?*Üniversite öğrencisi misiniz? """
            """   Zaman damgasi*Adiniz - Soyadiniz*Telefon Numaraniz*Mail Adresiniz*Sormak istedikleriniz?*Daha önce girişimcilik eğitimi aldiniz mi?  """
            DataFrame = pd.read_excel(file1)
            DataFrame.fillna(15)
            """kat_name = DataFrame['Adiniz - Soyadiniz']
            kat_numara = DataFrame['Telefon Numaraniz']"""
            print(DataFrame)
            kat_name = DataFrame[names[degone]]
            kat_numara = DataFrame[names[degtwo]]
            print(kat_numara)
            print(kat_name)
            kat_names, kat_surnames = [], []
            for i in kat_name:
                print(i)
                listab = i.split()
                kat_names.append(listab[0])
                kat_surnames.append(listab[1])

            """Data listelerini oluşturdum üst tarafta şimdi bunlari vcard'a yazdirabilirim
                kat_names = katilimcinin ismi
                kat_surnames = katilimcinin soyismi
                kat_numara = katilimcinin telefon numarasi
            """
            uzunluk = len(kat_numara) / loop
            counter = 0
            kolay+="0 "
            while counter < uzunluk:
                with open(f'vcard{kolay}.vcf', 'w', encoding='utf-8') as file:
                    val = (counter+1) * loop
                    val2 = (counter) * loop
                    print(val,val2)
                    for sira in range(val2,val):
                        print(sira,'---------------------------------------------------------')
                        try:
                            isim = kat_names[sira]
                        except Exception:
                            break
                        if len(str(kat_numara[sira])) == 10 or (
                                len(str(kat_numara[sira])) == 11 and str(kat_numara[sira][0]) == '0'):
                            print(sira)
                            isim = kat_names[sira]
                            soyisim = kat_surnames[sira]
                            fullname = kat_name[sira]
                            print(fullname)
                            numara = kat_numara[sira]
                            ref1 = random.randint(1, 24)
                            ref2 = random.randint(1, 58)
                            ref3 = random.randint(1, 58)
                            file.write(
                                f'BEGiN:VCARD\nVERSiON:3.0\nPRODiD:-//Apple inc.//iOS 13.6.1//EN\nN:{soyisim};{kolay}{isim} ;;;\nFN:{kolay}{fullname}\nTEL;type=CELL;type=VOiCE;type=pref:+90{numara}\nREV:2020-09-01T{ref1}:{ref2}:{ref3}Z\nEND:VCARD\n')
                        else:
                            print(sira, 'numara eksik veya hatali')
                            continue

                    counter+=1
                    if counter+30 >= len(kat_numara):
                        counter-=(len(kat_numara)-counter-1)
                    kolay = kolay[:-2] + str(counter) + " "
            """kat-names - kat-surnames - kat-name - kat-numara - ref1 - ref2 - ref3"""




app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())



