import tkinter as tk 
# tk._test()
root = tk.Tk()
root.title("Testing")
def on_click():
    print("Ok, this is Running property.....")
lbl = tk.Label(root, text="Hello, it is testing0. If you can see me click me.")
lbl.grid(row= 0, column= 1,)
 
btn = tk.Button(root, text = "Button1", command= on_click)
btn.grid(row= 5, column = 0)
root.mainloop()