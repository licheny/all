import tkinter as tk

window=tk.Tk()
window.title("my seven python window GUI")
window.geometry("500x200")

canvas=tk.Canvas(window,bg="blue",width=500,height=100)
img_file=tk.PhotoImage(file="1.png")
img=canvas.create_image(10,10,anchor="nw",image=img_file)
x0,y0,x1,y1=300,10,400,10
line=canvas.create_line(x0,y0,x1,y1)
line=canvas.create_line(x0,y0,x1,y1)
oval=canvas.create_oval(x0,y0,400,110,fill="orange")#代表四周四个点，顺时针方向
arc=canvas.create_arc(300,10,400,110,start=0,extent=60)
rect=canvas.create_rectangle(200,20,300,30)
canvas.pack()

def moveit():
    canvas.move(rect,0,2)
b=tk.Button(window,text="move",bg="red",command=moveit).pack()
window.mainloop()