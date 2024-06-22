from tkinter import *


def click(event):
    global entry
    text = event.text = event.widget.cget("text")
    print(text)
    print(text)
    if text == "=":
        if entry.get().isdigit():
            value = int(entry.get())
        else:
            value = eval(entry.get())
            entry.set(value)
            root.update()
    elif text == "cut":
        entry.set(entry.get()[:-1])

    else:
        entry.set(entry.get() + text)
        root.update()

    if text == "clear":
        entry.set("")
        root.update()


root = Tk()
root.geometry("250x420")
root.maxsize(400, 700)
root.minsize(200, 700)
root.title("calculator")
entry = StringVar()
entry.set("press clear")
f = Frame(root, borderwidth=10, bg="grey")
e = Entry(f, textvariable=entry, font="lucida 30")
e.pack()
f2 = Frame(root, borderwidth=5, bg="white")
b1 = Button(f2, text="7", font="c 30 bold", fg="grey")
b1.pack(side=LEFT, anchor="w", padx=10)
b1.bind("<Button-1>", click)
b2 = Button(f2, text="8", font="c 30 bold", fg="grey")
b2.pack(side=LEFT, anchor="w", padx=10)
b2.bind("<Button-1>", click)
b3 = Button(f2, text="9", font="c 30 bold", fg="grey")
b3.pack(side=LEFT, anchor="w", padx=10)
b3.bind("<Button-1>", click)
f.pack()
f2.pack()
freme = Frame(root, borderwidth=5, bg="white")
b4 = Button(freme, text="4", fg="grey", font="c 30 bold")
b4.pack(side=LEFT, padx=10)
b4.bind("<Button-1>", click)
b5 = Button(freme, text="5", fg="grey", font="c 30 bold", )
b5.pack(side=LEFT, padx=10)
b5.bind("<Button-1>", click)
b6 = Button(freme, text="6", fg="grey", font="c 30 bold")
b6.pack(side=LEFT, padx=10)
b6.bind("<Button-1>", click)
freme.pack()

f3 = Frame(root, borderwidth=5, bg="white")
b7 = Button(f3, text="1", fg="grey", font="c 30 bold")
b7.pack(side=LEFT, padx=10)
b7.bind("<Button-1>", click)
b8 = Button(f3, text="2", fg="grey", font="c 30 bold")
b8.pack(side=LEFT, padx=10)
b8.bind("<Button-1>", click)
b9 = Button(f3, text="3", fg="grey", font="c 30 bold")
b9.pack(side=LEFT, padx=10)
b9.bind("<Button-1>", click)
f3.pack()

fr = Frame(root, bg="white", borderwidth=4)
b10 = Button(fr, text="0", fg="grey", font="c 30 bold")
b10.pack(side=LEFT, padx=15)
b10.bind("<Button-1>", click)
b11 = Button(fr, text=".", fg="grey", font="c 30 bold")
b11.pack(side=LEFT, padx=15)
b11.bind("<Button-1>", click)
b12 = Button(fr, text="*", fg="white", bg="sky blue", font="c 30 bold")
b12.pack(side=LEFT, padx=15)
b12.bind("<Button-1>", click)
fr.pack()

fm = Frame(borderwidth=7, bg="white")
b13 = Button(fm, text="/", fg="white", bg="sky blue", font="c 30 bold")
b13.pack(side=LEFT, padx=10)
b13.bind("<Button-1>", click)
b14 = Button(fm, text="+", fg="white", bg="sky blue", font="c 30 bold")
b14.pack(side=LEFT, padx=25)
b14.bind("<Button-1>", click)
b15 = Button(fm, text="=", fg="white", bg="sky blue", font="c 30 bold")
b15.pack(side=LEFT, anchor="s")
b15.bind("<Button-1>", click)
fm.pack()
fa = Frame(root, borderwidth=7, bg="white")
b15 = Button(fa, text="-", fg="white", bg="sky blue", font="c 30 bold")
b15.pack(side=LEFT)
b15.bind("<Button-1>", click)

b16 = Button(fa, text="cut", fg="white", bg="blue", font="c 30 bold")
b16.pack(side=RIGHT)
b16.bind("<Button-1>", click)
fa.pack()

b = Button(fa, text="%", fg="white", bg="light blue", font="c 30 bold")

b.pack(side=TOP, padx=20)

b.bind("<Button-1>", click)
root.configure(bg="white")

but = Button(root, text="clear", fg="white", bg="blue", font="lucoda 30 bold")
but.pack(side=TOP, pady=10)
but.bind("<Button-1>", click)
Label(root, text="Rajpurohit jugal", fg="blue").pack()

root.mainloop()
