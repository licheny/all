import tkinter as tk

window=tk.Tk()
window.title("six python windwo GUI")
window.geometry("500x300")
l=tk.Label(window,bg="orange",width=20,text="empty")
l.pack()

def print_selection(v):
    l.config(text="length"+v)

s=tk.Scale(window,
      label="try me",
      from_=0,  # 设置最小值  
      to=10  ,# 设置最大值  
      resolution=0.01,  # 设置步距值  
      orient=tk.HORIZONTAL,  # 设置水平方向  
    #   variable=v,  # 绑定变量  
    #   digits=8,  # 设置显示的位数为8  
      command=print_selection,  # 设置回调函数  )
      length=200,
      tickinterval=2,#设置间隔距离
      show=0
)
s.pack()

window.mainloop()
