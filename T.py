import os
def Info_Ukuran():
	f3 = open("Info.txt", "r")
	f = f3.read()
	print(f)
	f3.close()
	print(show_menu())
	os.system("cls")

def Insert_Data():
	fo = open("Merk.txt", "r")
	a = fo.read()
	print(a)
	fo.close()
	b = int(input("Pilihan anda : "))
	while((b!=1) and (b!=2) and (b!=3) and (b!=4) and (b!=5)):
		print(Insert_Data())
	if(b==1):
		f1 = open("Ukuran.txt", "r")
		c = f1.read()
		print(c)
		f1.close()
		d = int(input("Pilihan anda : "))
		while((d!=1) and (d!=2)) :
			print(Insert_Data())
		if(d==1):
			ukuran = input("ukuran : ")
			teks = "ukuran :{}".format(ukuran)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
			if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
				harga = 150000
			elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
				harga = 200000
			elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
				harga = 250000
			elif((ukuran=='12') or (ukuran=='12.5')):
				harga = 300000
			
			teks = "ukuran :{}\nharga : {}".format(ukuran, harga)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
		else:
			ukuran = input("ukuran : ")
			teks = "ukuran :{}".format(ukuran)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
			if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
				harga = 150000
			elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
				harga = 200000
			elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
				harga = 250000
			elif((ukuran=='12') or (ukuran=='12.5')):
				harga = 300000
			
			teks = "ukuran :{}\nharga : {}".format(ukuran, harga)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()

		print(show_menu())

	elif(b==2):
		f1 = open("Ukuran.txt", "r")
		c = f1.read()
		print(c)
		f1.close()
		d = int(input("Pilihan anda : "))
		while((d!=1) and (d!=2)) :
			print(Insert_Data())
		if(d==1):
			ukuran = input("ukuran : ")
			teks = "ukuran :{}".format(ukuran)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
			if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
				harga = 150000
			elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
				harga = 200000
			elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
				harga = 250000
			elif((ukuran=='12') or (ukuran=='12.5')):
				harga = 300000
			
			teks = "ukuran :{}\nharga : {}".format(ukuran, harga)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
		else:
			ukuran = input("ukuran : ")
			teks = "ukuran :{}".format(ukuran)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
			if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
				harga = 150000
			elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
				harga = 200000
			elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
				harga = 250000
			elif((ukuran=='12') or (ukuran=='12.5')):
				harga = 300000
		
			teks = "ukuran :{}\nharga : {}".format(ukuran, harga)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()

		print(show_menu())

	elif(b==3):
		f1 = open("Ukuran.txt", "r")
		c = f1.read()
		print(c)
		f1.close()
		d = int(input("Pilihan anda : "))
		while((d!=1) and (d!=2)) :
			print(Insert_Data())
		if(d==1):
			ukuran = input("ukuran : ")
			teks = "ukuran :{}".format(ukuran)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
			if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
				harga = 150000
			elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
				harga = 200000
			elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
				harga = 250000
			elif((ukuran=='12') or (ukuran=='12.5')):
				harga = 300000
			
			teks = "ukuran :{}\nharga : {}".format(ukuran, harga)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
		else:
			ukuran = input("ukuran : ")
			teks = "ukuran :{}".format(ukuran)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
			if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
				harga = 150000
			elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
				harga = 200000
			elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
				harga = 250000
			elif((ukuran=='12') or (ukuran=='12.5')):
				harga = 300000
		
			teks = "ukuran :{}\nharga : {}".format(ukuran, harga)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
	   
		print(show_menu())

	elif(b==4):
		f1 = open("Ukuran.txt", "r")
		c = f1.read()
		print(c)
		f1.close()
		d = int(input("Pilihan anda : "))
		while((d!=1) and (d!=2)) :
			print(Insert_Data())
		if(d==1):
			ukuran = input("ukuran : ")
			teks = "ukuran :{}".format(ukuran)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
			if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
				harga = 150000
			elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
				harga = 200000
			elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
				harga = 250000
			elif((ukuran=='12') or (ukuran=='12.5')):
				harga = 300000
		
			teks = "ukuran :{}\nharga : {}".format(ukuran, harga)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
		else:
			ukuran = input("ukuran : ")
			teks = "ukuran :{}".format(ukuran)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
			if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
				harga = 150000
			elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
				harga = 200000
			elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
				harga = 250000
			elif((ukuran=='12') or (ukuran=='12.5')):
				harga = 300000
	
			teks = "ukuran :{}\nharga : {}".format(ukuran, harga)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()

		print(show_menu())

	else:
		f1 = open("Ukuran.txt", "r")
		c = f1.read()
		print(c)
		f1.close()
		d = int(input("Pilihan anda : "))
		while((d!=1) and (d!=2)) :
			print(Insert_Data())
		if(d==1):
			ukuran = input("ukuran : ")
			teks = "ukuran :{}".format(ukuran)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
			if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
				harga = 150000
			elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
				harga = 200000
			elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
				harga = 250000
			elif((ukuran=='12') or (ukuran=='12.5')):
				harga = 300000
		
			teks = "ukuran :{}\nharga : {}".format(ukuran, harga)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
		else:
			ukuran = input("ukuran : ")
			teks = "ukuran :{}".format(ukuran)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close()
			if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
				harga = 150000
			elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
				harga = 200000
			elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
				harga = 250000
			elif((ukuran=='12') or (ukuran=='12.5')):
				harga = 300000

			teks = "ukuran :{}\nharga : {}".format(ukuran, harga)
			f2 = open("Angka.txt", "w")
			f2.write(teks)
			f2.close() 

		os.system("cls")
		print(show_menu())
		
def Edit_Pesanan():
	f2 = open("Angka.txt", "r")
	c = f2.read()
	print(c)
	f2.close()

	e = input("Apakah sudah yakin dengan ukurannya ? ")
	while(e =='y'):
		print(show_menu())
	if (e=='t'):
		ukuran = input("ukuran : ")
		if((ukuran=='4.5') or (ukuran=='5') or (ukuran=='5.5') or (ukuran=='6') or (ukuran=='6.5')):
			harga = 150000
		elif((ukuran=='7') or (ukuran=='7.5') or (ukuran=='8') or (ukuran=='8.5') or (ukuran=='9')):
			harga = 200000
		elif((ukuran=='9.5') or (ukuran=='10') or (ukuran=='10.5') or (ukuran=='11') or (ukuran=='11.5')):
			harga = 250000
		elif((ukuran=='12') or (ukuran=='12.5')):
			harga = 300000
		teks = "ukuran :{}\n Harga :{}".format(ukuran, harga)
		f2 = open("Angka.txt", "w+")
		f2.write(teks)
		f2.close()   

	os.system("cls")

	f2 = open("Angka.txt", "r")
	teks = f2.read()
	print(teks)
	f2.close()
	print(show_menu()) 

def Batalkan_pesanan_atau_lanjut_Memesan() :
	f2 = open("Angka.txt", "r")
	teks = f2.read()
	print(teks)
	f2.close()

	h = input("\n Lanjutkan Membeli? \n ")
	while(h == 'y'):
		print ("Selamat Anda berhak mendapatkannya,silahkan Melakukan pembayaran via transfer")
		print(show_menu())
	if(h == 't') :
		print("Anda telah Membatalkan pemesanan")
		print(show_menu())

def show_menu():
	import os
	print("PROGRAM BELI SEPATU ONLINE")
	print("======SELAMAT DATANG======") 
	print ("\n")
	print ("----------- MENU ----------")
	print ("1. Info Ukuran")
	print ("2. Insert Data")
	print ("3. Edit pesanan")
	print ("4. Batalkan Pemesanan atau Lanjut Memesan")
	indeks = int(input("PILIH MENU : "))
	if(indeks == 1):
		os.system("cls")
		Info_Ukuran()
	elif(indeks == 2):
		os.system("cls")
		Insert_Data()
	elif(indeks == 3):
		os.system("cls")
		Edit_Pesanan()
	elif(indeks == 4):
		Batalkan_pesanan_atau_lanjut_Memesan()
	else:
		os.system("cls")
		print(show_menu())
	
print(show_menu()) 