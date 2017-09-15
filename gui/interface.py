import os
import random
from tkinter import*
from tkinter import messagebox
from cards.card_info import*

class guin():
	def __init__(self):
		#Background frame goes here
		self.bg_frame = Frame(bg="#b8fcf9", height=600, width=700)
		self.bg_frame.pack()
		#Main frame goes here
		self.main_frame = Frame(self.bg_frame ,bg="#246d6a", height=600, width=300)
		self.main_frame.place(x=200, y=0)
		#Of course widgets
		self.start_bu = Button(self.main_frame, text="Oyunu Başlat", width=42, height=4)
		self.start_bu.place(x=0,y=75)
		self.start_bu.config(command=self.baslat)
		##################
		self.about_bu = Button(self.main_frame, text="Hakkında", width=42, height=4)
		self.about_bu.place(x=0,y=175)
		self.about_bu.config(command=lambda:messagebox.showinfo("Hakkında", "Tarot Kartlarını öğrenmek için\nboş zamanında yaptığım bir oyun"))
		##################
		self.exit_bu = Button(self.main_frame, text="Çıkış", width=42, height=4)
		self.exit_bu.config(command=lambda:os._exit(0))
		self.exit_bu.place(x=0,y=275)
		##################
		#Game Frame
		self.ga_frame = Frame(self.bg_frame, height=600, width=500, bg="#b8fcf9")
		##################
		self.ga_lab1 = Label(self.ga_frame, text="Tek Kartlık Tarot Falı", font=("Times",30,"normal"))
		self.ga_lab1.place(x=75, y=0)
		##################
		self.ga_lab2 = Label(self.ga_frame, text="0-78 arasından bir rakam girin\nNot:0 Dahil değil, 78 Dahil", font=("Times",15,"normal"))
		self.ga_lab2.place(x=75, y=75)
		##################
		self.kart_index = IntVar()
		self.kart_index.set(0)
		self.ga_ent = Entry(self.ga_frame, textvariable=self.kart_index)
		self.ga_ent.place(x=75, y=200)
		##################
		self.image1 = PhotoImage(file="gui\\image.gif")
		self.ga_lab3 = Label(self.ga_frame, image=self.image1)
		self.ga_lab3.place(x=250, y=200)
		#################
		self.ga_bu1 = Button(self.ga_frame, text="Hazır olunca bas", command=self.oku, height=10, width=18)
		self.ga_bu1.place(x=75, y=400)
		#################
		

	def baslat(self):
		self.main_frame.place_forget()
		self.bg_frame.config(bg="#181c1e")
		self.ga_frame.place(x=100,y=0)

	def oku(self):
		if self.kart_index.get() in range(1,79):
			kart,hakkında= self.kart_cek(self.kart_index.get())
			ga_to = Toplevel()
			ga_to.geometry("400x400")
			ga_to.title("{} Kartı Hakkında".format(kart))
			Label(ga_to, text=hakkında, width=100).pack()
		else:
			messagebox.showerror("HATA", "Lütfen Talimatları Doğru\nUyguladığınızdan Emin Olunuz")

	def kart_cek(self, indexx):
		self.kart_range = list(range(1,79))
		random.shuffle(self.kart_range)
		indexx = self.kart_range[indexx-1]
		return kart[indexx],hakkında[indexx]