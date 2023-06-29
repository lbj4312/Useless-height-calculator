import tkinter
root=tkinter.Tk()
tkinter.Label(root,text="请输入你的身高:(单位:cm)").pack()
e=tkinter.Entry(root)
e.pack()
txt=tkinter.StringVar()
txt.set("")
def click():
    nr=e.get()
    try:
        nr=int(nr)
    except ValueError:
        txt.set("请输入数字!")
    else:
        txt.set("你的身高是:"+str(nr)+"cm")  # txt.set("你的身高是:",nr,"cm")
tkinter.Button(root,text="计算",command=click).pack()
tkinter.Label(root,textvar=txt).pack()
