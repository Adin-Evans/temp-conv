from tkinter import *
def button_click(number):
  current = entryBar.get()
  entryBar.insert(o, str(current) + str(number))  

root = Tk()
root.title("Converter")
entryBar = Entry(root, width = 20).grid(row=0, column=0, columnspan = 3)
button_k = Button(root, text="K", padx = 20, pady = 15,).grid(row=1, column=0)
button_c = Button(root, text="C", padx = 20, pady = 15,).grid(row=1, column=1)
button_f = Button(root, text="F", padx = 20, pady = 15,).grid(row=1, column=2)
button_0 = Button(root, text = "0", padx = 20, pady = 15,).grid(row =5 , column =0)
button_1 = Button(root, text = "1", padx = 20, pady = 15,).grid(row =2 , column =0 )
button_2 = Button(root, text = "2", padx = 20, pady = 15,).grid(row =2 , column =1 )
button_3 = Button(root, text = "3", padx = 20, pady = 15,).grid(row =2 , column =2 )
button_4 = Button(root, text = "4", padx = 20, pady = 15,).grid(row=3 ,column=0)
button_5 = Button(root, text = "5", padx = 20, pady = 15,).grid(row =3 , column =1 )
button_6 = Button(root, text = "6", padx = 20, pady = 15,).grid(row =3 , column =2 )
button_7 = Button(root, text = "7", padx = 20, pady = 15,).grid(row =4 , column =0 )
button_8 = Button(root, text = "8", padx = 20, pady = 15,).grid(row =4 , column =1 )
button_9 = Button(root, text = "9", padx = 20, pady = 15,).grid(row =4 , column =2 )
button_enter = Button(root, text = "Enter", padx = 41, pady = 15,).grid(row= 5, column=1, columnspan = 2)

root.mainloop()