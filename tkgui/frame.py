import tkinter as tk

window=tk.Tk()
window.title("my nine python window GUI")
window.geometry("500x200")

l=tk.Label(window,text="on the window",height=1).pack()
frame=tk.Frame(window).pack()
frame_l=tk.Frame(frame)
frame_l.pack(side="left")
frame_r=tk.Frame(frame)
frame_r.pack(side="right")

tk.Label(frame_l,text="on the framel 1").pack()
tk.Label(frame_l,text="on the framel 2").pack()
tk.Label(frame_r,text="on the framer 1").pack()
window.mainloop()