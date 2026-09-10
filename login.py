import tkinter as tk
from tkinter import messagebox
import bcrypt

from database import connect_database
from dashboard import open_dashboard


class LoginWindow:

    def __init__(self, root):
        self.root = root
        self.root.title("NTPC IT Asset Management System")
        self.root.geometry("1200x750")
        self.root.minsize(900, 600)
        self.root.configure(bg="#F4F6F9")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        self.create_header()
        self.create_main()

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg="#172033",
            height=115
        )
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)

        header.columnconfigure(0, weight=0)
        header.columnconfigure(1, weight=0)
        header.columnconfigure(2, weight=1)

        logo_container = tk.Frame(
            header,
            bg="#172033",
            width=170,
            height=90
        )
        logo_container.grid(
            row=0,
            column=0,
            padx=(45, 10),
            pady=12
        )
        logo_container.grid_propagate(False)

        try:
            logo = tk.PhotoImage(file="NTPC.png")

            max_width = 105
            max_height = 75

            width = logo.width()
            height = logo.height()

            scale_x = max(1, width // max_width)
            scale_y = max(1, height // max_height)
            scale = max(scale_x, scale_y)

            if scale > 1:
                logo = logo.subsample(scale, scale)

            self.logo = logo

            tk.Label(
                logo_container,
                image=self.logo,
                bg="#172033"
            ).place(
                relx=0.5,
                rely=0.5,
                anchor="center"
            )

        except Exception:

            tk.Label(
                logo_container,
                text="NTPC",
                font=("Arial", 25, "bold"),
                bg="#172033",
                fg="white"
            ).place(
                relx=0.5,
                rely=0.5,
                anchor="center"
            )

        separator = tk.Frame(
            header,
            bg="#526078",
            width=2,
            height=58
        )
        separator.grid(
            row=0,
            column=1,
            pady=28
        )

        tk.Label(
            header,
            text="IT ASSET MANAGEMENT SYSTEM",
            font=("Arial", 25, "bold"),
            bg="#172033",
            fg="white",
            anchor="w"
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=(34, 30)
        )

    def create_main(self):

        main = tk.Frame(
            self.root,
            bg="#F4F6F9"
        )
        main.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        main.columnconfigure(0, weight=1)
        main.rowconfigure(0, weight=1)

        center = tk.Frame(
            main,
            bg="#F4F6F9"
        )
        center.grid(
            row=0,
            column=0
        )

        tk.Label(
            center,
            text="NTPC • KAHALGAON",
            font=("Arial", 13, "bold"),
            bg="#F4F6F9",
            fg="#0878C9"
        ).pack(
            pady=(5, 22)
        )

        tk.Label(
            center,
            text="NTPC IT Asset Management System",
            font=("Arial", 32, "bold"),
            bg="#F4F6F9",
            fg="#172033"
        ).pack()

        tk.Label(
            center,
            text="IT Department",
            font=("Arial", 20, "bold"),
            bg="#F4F6F9",
            fg="#1769E0"
        ).pack(
            pady=(18, 5)
        )

        tk.Label(
            center,
            text="Kahalgaon Super Thermal Power Station",
            font=("Arial", 15),
            bg="#F4F6F9",
            fg="#65758B"
        ).pack()

        tk.Frame(
            center,
            bg="#1769E0",
            height=3,
            width=195
        ).pack(
            pady=(28, 35)
        )

        tk.Label(
            center,
            text="Centralized management of IT assets, equipment, users and departmental records.",
            font=("Arial", 11),
            bg="#F4F6F9",
            fg="#7A8798"
        ).pack(
            pady=(0, 28)
        )

        login_button = tk.Button(
            center,
            text="🔒   ADMINISTRATOR LOGIN",
            font=("Arial", 15, "bold"),
            bg="#1769E0",
            fg="white",
            activebackground="#1259C7",
            activeforeground="white",
            relief="flat",
            bd=0,
            width=34,
            height=2,
            cursor="hand2",
            command=self.open_login_dialog
        )
        login_button.pack()

        login_button.bind(
            "<Enter>",
            lambda event: login_button.config(bg="#1259C7")
        )

        login_button.bind(
            "<Leave>",
            lambda event: login_button.config(bg="#1769E0")
        )

        tk.Label(
            center,
            text="Authorized personnel only",
            font=("Arial", 10),
            bg="#F4F6F9",
            fg="#A0ACBB"
        ).pack(
            pady=(24, 12)
        )

        tk.Label(
            center,
            text="NTPC • IT Department • Asset Management",
            font=("Arial", 9),
            bg="#F4F6F9",
            fg="#AAB4C2"
        ).pack()

        footer = tk.Frame(
            main,
            bg="#172033",
            height=42
        )
        footer.place(
            relx=0,
            rely=1,
            relwidth=1,
            anchor="sw"
        )

        tk.Label(
            footer,
            text="NTPC Kahalgaon Super Thermal Power Station",
            font=("Arial", 9),
            bg="#172033",
            fg="#DCE3ED"
        ).pack(
            side="left",
            padx=30
        )

        tk.Label(
            footer,
            text="IT Department",
            font=("Arial", 9),
            bg="#172033",
            fg="#DCE3ED"
        ).pack(
            side="right",
            padx=30
        )

    def open_login_dialog(self):

        dialog = tk.Toplevel(self.root)
        dialog.title("Administrator Login")
        dialog.geometry("430x390")
        dialog.resizable(False, False)
        dialog.configure(bg="#F4F6F9")
        dialog.transient(self.root)
        dialog.grab_set()

        dialog.update_idletasks()

        x = self.root.winfo_x() + (
            self.root.winfo_width() - dialog.winfo_width()
        ) // 2

        y = self.root.winfo_y() + (
            self.root.winfo_height() - dialog.winfo_height()
        ) // 2

        dialog.geometry(
            f"+{x}+{y}"
        )

        header = tk.Frame(
            dialog,
            bg="#172033",
            height=75
        )
        header.pack(
            fill="x"
        )
        header.pack_propagate(False)

        tk.Label(
            header,
            text="ADMINISTRATOR LOGIN",
            font=("Arial", 17, "bold"),
            bg="#172033",
            fg="white"
        ).pack(
            pady=23
        )

        form = tk.Frame(
            dialog,
            bg="white",
            padx=35,
            pady=25,
            bd=1,
            relief="solid"
        )
        form.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        tk.Label(
            form,
            text="Username",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#344054"
        ).pack(
            anchor="w"
        )

        username_entry = tk.Entry(
            form,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )
        username_entry.pack(
            fill="x",
            ipady=7,
            pady=(7, 18)
        )

        tk.Label(
            form,
            text="Password",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#344054"
        ).pack(
            anchor="w"
        )

        password_entry = tk.Entry(
            form,
            font=("Arial", 11),
            show="*",
            relief="solid",
            bd=1
        )
        password_entry.pack(
            fill="x",
            ipady=7,
            pady=(7, 22)
        )

        login_button = tk.Button(
            form,
            text="LOGIN",
            font=("Arial", 11, "bold"),
            bg="#1769E0",
            fg="white",
            activebackground="#1259C7",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            height=2,
            command=lambda: self.authenticate(
                username_entry,
                password_entry,
                dialog
            )
        )
        login_button.pack(
            fill="x"
        )

        username_entry.focus_set()

        password_entry.bind(
            "<Return>",
            lambda event: self.authenticate(
                username_entry,
                password_entry,
                dialog
            )
        )

    def authenticate(
        self,
        username_entry,
        password_entry,
        dialog
    ):

        username = username_entry.get().strip()
        password = password_entry.get()

        if not username or not password:

            messagebox.showwarning(
                "Login Required",
                "Please enter Username and Password.",
                parent=dialog
            )
            return

        connection = connect_database()

        if connection is None:

            messagebox.showerror(
                "Database Error",
                "Unable to connect to the database.",
                parent=dialog
            )
            return

        cursor = None

        try:

            cursor = connection.cursor(
                dictionary=True
            )

            cursor.execute(
                """
                SELECT
                    User_Id,
                    Username,
                    Password,
                    Full_Name,
                    Role
                FROM Users
                WHERE Username = %s
                """,
                (username,)
            )

            user = cursor.fetchone()

            if not user:

                messagebox.showerror(
                    "Login Failed",
                    "Invalid Username or Password.",
                    parent=dialog
                )

                password_entry.delete(
                    0,
                    tk.END
                )

                password_entry.focus_set()

                return

            stored_password = user["Password"]

            if isinstance(
                stored_password,
                str
            ):
                stored_password = stored_password.encode(
                    "utf-8"
                )

            if not bcrypt.checkpw(
                password.encode("utf-8"),
                stored_password
            ):

                messagebox.showerror(
                    "Login Failed",
                    "Invalid Username or Password.",
                    parent=dialog
                )

                password_entry.delete(
                    0,
                    tk.END
                )

                password_entry.focus_set()

                return

            user_id = user["User_Id"]
            full_name = user["Full_Name"]
            logged_username = user["Username"]

            dialog.destroy()
            self.root.destroy()

            open_dashboard(
                admin_name=full_name,
                admin_username=logged_username,
                admin_user_id=user_id
            )

        except Exception as error:

            messagebox.showerror(
                "Login Error",
                str(error),
                parent=dialog
            )

        finally:

            if cursor is not None:
                cursor.close()

            if connection is not None and connection.is_connected():
                connection.close()


def open_login():

    root = tk.Tk()

    LoginWindow(root)

    root.mainloop()


if __name__ == "__main__":
    open_login()