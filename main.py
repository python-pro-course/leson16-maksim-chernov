from tkinter import *
import os
#создание окон
main = Tk() #делает окно
main.title('банк') #заголовок окна
main.geometry('500x500') #размер окна
#регистрация
def sing_up():
    sing_up_screen = Toplevel(main)
    sing_up_screeen.title('Sing Up')
    main.geometry('200x200')

    labes(main, text=',логин и пароль').grid(row=0) #ров это строчка
    labes(main, text=',логин').grid(row=1, sticky = w)
    labes(main, text=',пароль').grid(row=2, sticky= W)

mainloop()
#создание кортанки
img = Image.open()
ing = Img.resize((150,150))
img = ImageTk.PhotoImage(ing)


# labels
labes(main, text=',безопасный банк').pack(side=TOP)
label(main, image=img).pack(side=TOP)

#кнопки
Button(main, text ='Sing Up', font=('Calibri', 12),width=15), command =sing_up).pack(side=TOP,pady=10)
Button(main, text ='Log In', font=('Calibri', 12),width=15).pack(side=TOP)

main.mainloop()