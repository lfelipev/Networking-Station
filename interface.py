from Tkinter import *
from client import Client

counter = 0

class App:
    def __init__(self, master):
        self.data = "none"
        frame = Frame(master)
        frame.pack()
        self.connect()
        #self.button = Button(frame,
         #                    text="connect",
          #                   command=self.connect)
        #self.button.pack(side=LEFT)


    def connect(self):
        client = Client()
        self.data = client.getData()
        label = Label()
        label.pack()
        #label.config(text=str(self.data))

        def update():
            global data
            data = data
            label.config(text=str(data))
            label.after(1000, update)
        update()



def main():
    root = Tk()
    root.title("Wheather Station")
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()