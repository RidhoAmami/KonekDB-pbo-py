import tkinter as tk
from koneksi import connect_database
from koneksi import close_database


class Ui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Koneksi Database")

        # Label dan entry untuk username
        self.label_username = tk.Label(text='Username')
        self.label_username.grid(padx=5, pady=5, row=0, column=0)
        self.username=tk.StringVar()
        self.entry_username = tk.Entry(textvariable=self.username)
        self.entry_username.grid(padx=5, pady=5, row=0, column=1)

        # Label dan entry untuk password
        self.label_password=tk.Label(text='Password')
        self.label_password.grid(padx=5, pady=5, row=1, column=0)
        self.password=tk.StringVar()
        self.entry_username = tk.Entry(textvariable=self.password)
        self.entry_username.grid(padx=5, pady=5, row=1, column=1)


        # Tombol untuk koneksi dan tutup
        self.button_connect = tk.Button(text="LOGIN", command=self.connect_database)
        self.button_connect.grid(padx=5, pady=5, columnspan=2, column=0, row=2, sticky=tk.EW)

        self.label_status = tk.Label(text="Database Terputus")
        self.label_status.grid(padx=5, pady=5, columnspan=2, row=4, column=0, sticky=tk.EW)

        # Sesion
        self.connection = None
        self.connection_status = False

        self.window.mainloop()

    def connect_database(self):
        username = self.username.get()
        password = self.password.get()

        connection = connect_database(username, password)

        if connection is not None:
            print("Koneksi berhasil!")
            self.connection_status = True
            self.update_connection_status()

        else:
            print("Koneksi gagal!")
            self.connection_status = False
            self.update_connection_status()

    def close_database(self):
        close_database(self.connection)
        self.connection_status = False
        self.update_connection_status()
        self.button_connect.config(text='LOGIN', command=self.connect_database)
    
    def update_connection_status(self):
        if self.connection_status:
            self.label_status.config(text="Database Terhubung")
            self.button_connect.config(text='LOGOUT', command=self.close_database)
        else:
            self.label_status.config(text="Database Terputus")