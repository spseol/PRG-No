Tkinter
=============

* <http://tkinter.programujte.com/>
* <http://tkinter.py.cz/>
* <http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html>
* <https://docs.python.org/3/library/tkinter.html>
* <https://docs.python.org/3/library/tkinter.ttk.html>


Helo World
---------------

```python
import tkinter as tk
# from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


# root = tk.Tk()
app = Application()
# print(root == app.master)
app.mainloop()


```
