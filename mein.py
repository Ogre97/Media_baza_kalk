from tkinter import *
import math  
  
window = Tk()
window.title("Калькулятор Mediabaza")  
window.geometry(('235x400'))

# Функция расчета 
def clicked():
	#res = "Кол. кВ.м {}".format(txt_1.get())  
	#Tekst_1.configure(text=res)

	# Переменные
	shirina = float(txt_0.get())
	dlina = float(txt_1.get())
	kol = int(txt_2.get())
	mat = float(txt_3.get())
	chena_2 = int(txt_4.get())
	chena_1 = int(txt_5.get())

	# Количество кв
	kv = (shirina * dlina) * kol
	kv = round(kv + 0.001,2)
	# Отход
	otxod = ((mat - shirina) * dlina) * kol
	# Цена за отход
	chena_otxod = otxod * chena_1
	# Цена за печать за кв
	chena_pechat = kv * chena_2
	# Цена за печать и за отход
	chena_za_vse_toch = chena_otxod + chena_pechat
	# Цена за все не точная
	chena = chena_za_vse_toch / kv
	# Округление
	a = math.ceil(chena)

	# Проверка на остаток цену за 1кв
	while a % 50 != 0:
		a += 1
	# Цена Кв * цена за 1кв
	b = a * kv


	k_1 = 'Всего кВ.м {}'.format(kv)
	Tekst_1.configure(text=k_1)

	k_2 = 'Цена за 1кВ.м {}'.format(a)
	Tekst_2.configure(text=k_2)

	k_3 = 'Цена за все {}'.format("{:.2f}".format(b))
	Tekst_3.configure(text=k_3)

	# Тест потом можно удалить ________

	k_4 = 'Цена отход {}'.format("{:.2f}".format(chena_otxod))
	Tekst_4.configure(text=k_4)

	k_5 = 'Цена печать {}'.format("{:.2f}".format(chena_pechat))
	Tekst_5.configure(text=k_5)


	#____________

# Ширина_0
lbl_0 = Label(window, text="Ширина: ",  font=("Arial Bold", 12))  
lbl_0.grid(column=0, row=1, sticky=W)  
txt_0 = Entry(window, width=10)  
txt_0.grid(column=1, row=1, sticky=W)

# Длинай_1
lbl_1 = Label(window, text="Высота: ",  font=("Arial Bold", 12))  
lbl_1.grid(column=0, row=2, sticky=W)  
txt_1 = Entry(window, width=10)  
txt_1.grid(column=1, row=2,)

# Количество_1
lbl_2 = Label(window, text="Количество: ",  font=("Arial Bold", 12))  
lbl_2.grid(column=0, row=3, sticky=W)  
txt_2 = Entry(window, width=10)  
txt_2.grid(column=1, row=3,)

# НА чем печатаь_2
lbl_3 = Label(window, text="На чем печатать: ",  font=("Arial Bold", 12))  
lbl_3.grid(column=0, row=4, sticky=W)  
txt_3 = Entry(window, width=10)  
txt_3.grid(column=1, row=4,)

# Цена_3
lbl_4 = Label(window, text="Цена-1кв.м: ", font=("Arial Bold", 12))  
lbl_4.grid(column=0, row=5, sticky=W)  
txt_4 = Entry(window, width=10)  
txt_4.grid(column=1, row=5,)

# Цена за отход _4
lbl_5 = Label(window, text="Цена за отход-1кв.м: " ,  font=("Arial Bold", 12))  
lbl_5.grid(column=0, row=6, sticky=W)  
txt_5 = Entry(window, width=10)  
txt_5.grid(column=1, row=6,)

# Кнопка расчета
btn = Button(window, text="Рассчитать", bg ='#00CED1', command = clicked)
btn.grid(column=0, row=7, columnspan=2)

# Кнопка Очистить
# btn = Button(window, text="Очистить", bg ='#FF4500')
# btn.grid(column=0, row=8, columnspan=2)

Tekst_1 = Label(window, text=" ",  font=("Arial Bold", 10))  
Tekst_1.grid(column=0, row=9, sticky=W)

Tekst_2 = Label(window, text=" " ,  font=("Arial Bold", 10))  
Tekst_2.grid(column=0, row=10, sticky=W)

Tekst_3 = Label(window, text=" " ,  font=("Arial Bold", 10))  
Tekst_3.grid(column=0, row=11, sticky=W)

Tekst_7 = Label(window, text="___________________" ,  font=("Arial Bold", 10))  
Tekst_7.grid(column=0, row=12, sticky=W)

Tekst_4 = Label(window, text=" " ,  font=("Arial Bold", 10))  
Tekst_4.grid(column=0, row=13, sticky=W)

Tekst_5 = Label(window, text=" " ,  font=("Arial Bold", 10))  
Tekst_5.grid(column=0, row=14, sticky=W)


	
window.mainloop()