from tkinter import *



def save_data():
  name_info = text.get("1.0",END)
  f = open("note", "w")
  f.write(name_info + "\n")
  f.close()

notepad=Tk()
h,w=1200,700
notepad.title("Noter")
notepad.geometry("1200x700")
notepad.config(bg="white")

text=Text(notepad,bg="white"
          ,width=h,height=h,font="100",border=0,fg="red")

text.insert(1.0,"#// Developer >>>>Yuvraj<<<<  \n\n")
text.insert(2.0,"")

but=Button(notepad,text="save",command=save_data)
but.pack()
text.pack()




notepad.mainloop()