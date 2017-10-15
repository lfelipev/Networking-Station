from Tkinter import *
from client import Client

counter = 0

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame,
                             text="connect",
                             command=self.connect)
        self.button.pack(side=LEFT)

        self.temperature()

    def connect(self):
        client = Client()
        client.connect()

    def temperature(self):
        label = Label()
        label.pack()
        counter = 36
        label.config(text=str(counter))

def main():
    root = Tk()
    root.title("Wheather Station")
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()