from Tkinter import *
from server import Server

class Server:
    def __init__(self, master):
        self.server = Server()
        frame = Frame(master)
        frame.pack()

        self.start_button = Button(frame,
                             text="Start",
                             command=self.start_server(self.server))
        self.start_button.pack(side=LEFT)
        self.stop_button = Button(frame,
                                  text="Stop",
                                  command=self.stop_server(self.server))
        self.stop_button.pack(side=RIGHT)

    def start_server(self, server):
        server.connect_loop()

    def stop_server(self, server):
        server.disconnect()

def main():
    root = Tk()
    root.title("Wheather Station")
    app = Server(root)
    root.mainloop()

if __name__ == '__main__':
    main()