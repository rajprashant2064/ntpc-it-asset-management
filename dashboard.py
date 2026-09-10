import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import bcrypt

from database import connect_database
from assets import (
    add_asset,
    get_all_assets,
    search_assets,
    get_asset_by_code,
    update_asset,
    assign_asset,
    delete_asset,
    get_asset_statistics
)


BG_COLOR = "#F4F7FB"
WHITE = "#FFFFFF"
PRIMARY = "#005BAC"
PRIMARY_DARK = "#003B73"
TEXT = "#172033"
TEXT_GRAY = "#64748B"
SUCCESS = "#16834B"
WARNING = "#F59E0B"
DANGER = "#D62828"
BORDER = "#D9E2EC"


def open_dashboard(
    admin_name="Prashant Raj",
    admin_username=None,
    admin_user_id=None
):

    dashboard = tk.Tk()

    dashboard.title(
        "NTPC IT Asset Management System - Dashboard"
    )

    dashboard.geometry(
        "1250x780"
    )

    dashboard.minsize(
        1100,
        700
    )

    dashboard.configure(
        bg=BG_COLOR
    )

    style = ttk.Style()

    try:
        style.theme_use("clam")
    except:
        pass

    style.configure(
        "Treeview",
        background=WHITE,
        foreground=TEXT,
        rowheight=32,
        fieldbackground=WHITE,
        font=("Arial", 10)
    )

    style.configure(
        "Treeview.Heading",
        background=PRIMARY_DARK,
        foreground=WHITE,
        font=("Arial", 10, "bold"),
        relief="flat"
    )

    style.map(
        "Treeview",
        background=[
            ("selected", "#DCEBFA")
        ],
        foreground=[
            ("selected", TEXT)
        ]
    )

    style.configure(
        "TCombobox",
        padding=6,
        font=("Arial", 10)
    )

    header = tk.Frame(
        dashboard,
        bg=WHITE,
        height=115
    )

    header.pack(
        fill="x"
    )

    header.pack_propagate(
        False
    )

    logo_frame = tk.Frame(
        header,
        bg=WHITE,
        width=210
    )

    logo_frame.pack(
        side="left",
        fill="y",
        padx=25
    )

    logo_frame.pack_propagate(
        False
    )

    logo_text = tk.Label(
        logo_frame,
        text="NTPC",
        font=("Arial", 25, "bold"),
        fg=PRIMARY,
        bg=WHITE
    )

    logo_text.pack(
        pady=(25, 0)
    )

    logo_subtitle = tk.Label(
        logo_frame,
        text="A Maharatna Company",
        font=("Arial", 8),
        fg=TEXT_GRAY,
        bg=WHITE
    )

    logo_subtitle.pack()

    separator = tk.Frame(
        header,
        bg=BORDER,
        width=2
    )

    separator.pack(
        side="left",
        fill="y",
        pady=20
    )

    title_frame = tk.Frame(
        header,
        bg=WHITE
    )

    title_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=30
    )

    title_label = tk.Label(
        title_frame,
        text="IT ASSET MANAGEMENT SYSTEM",
        font=("Arial", 25, "bold"),
        fg=PRIMARY_DARK,
        bg=WHITE
    )

    title_label.pack(
        anchor="w",
        pady=(28, 2)
    )

    subtitle_label = tk.Label(
        title_frame,
        text="Kahalgaon Super Thermal Power Station • IT Department",
        font=("Arial", 11),
        fg=TEXT_GRAY,
        bg=WHITE
    )

    subtitle_label.pack(
        anchor="w"
    )

    user_frame = tk.Frame(
        header,
        bg=WHITE,
        width=250
    )

    user_frame.pack(
        side="right",
        fill="y",
        padx=25
    )

    user_frame.pack_propagate(
        False
    )

    welcome_label = tk.Label(
        user_frame,
        text=f"Welcome, {admin_name}",
        font=("Arial", 12, "bold"),
        fg=TEXT,
        bg=WHITE
    )

    welcome_label.pack(
        anchor="e",
        pady=(30, 2)
    )

    role_label = tk.Label(
        user_frame,
        text="Administrator",
        font=("Arial", 10),
        fg=PRIMARY,
        bg=WHITE
    )

    role_label.pack(
        anchor="e"
    )

    blue_line = tk.Frame(
        dashboard,
        bg=PRIMARY,
        height=4
    )

    blue_line.pack(
        fill="x"
    )

    content = tk.Frame(
        dashboard,
        bg=BG_COLOR
    )

    content.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=25
    )

    page_title = tk.Label(
        content,
        text="Dashboard",
        font=("Arial", 24, "bold"),
        fg=TEXT,
        bg=BG_COLOR
    )

    page_title.pack(
        pady=(0, 20)
    )

    statistics_frame = tk.Frame(
        content,
        bg=BG_COLOR
    )

    statistics_frame.pack(
        fill="x",
        pady=(0, 25)
    )

    total_value = tk.StringVar(
        value="0"
    )

    available_value = tk.StringVar(
        value="0"
    )

    assigned_value = tk.StringVar(
        value="0"
    )

    maintenance_value = tk.StringVar(
        value="0"
    )

    def create_stat_card(
        parent,
        title,
        variable,
        accent
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            bd=1,
            relief="solid",
            width=240,
            height=125
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        card.pack_propagate(
            False
        )

        top_bar = tk.Frame(
            card,
            bg=accent,
            height=5
        )

        top_bar.pack(
            fill="x"
        )

        title_label = tk.Label(
            card,
            text=title,
            font=("Arial", 11, "bold"),
            fg=TEXT_GRAY,
            bg=WHITE
        )

        title_label.pack(
            pady=(18, 5)
        )

        value_label = tk.Label(
            card,
            textvariable=variable,
            font=("Arial", 28, "bold"),
            fg=accent,
            bg=WHITE
        )

        value_label.pack()

    create_stat_card(
        statistics_frame,
        "TOTAL ASSETS",
        total_value,
        PRIMARY
    )

    create_stat_card(
        statistics_frame,
        "AVAILABLE",
        available_value,
        SUCCESS
    )

    create_stat_card(
        statistics_frame,
        "ASSIGNED",
        assigned_value,
        WARNING
    )

    create_stat_card(
        statistics_frame,
        "MAINTENANCE",
        maintenance_value,
        DANGER
    )

    actions_container = tk.Frame(
        content,
        bg=WHITE,
        bd=1,
        relief="solid"
    )

    actions_container.pack(
        fill="x",
        padx=60,
        pady=10
    )

    section_title = tk.Label(
        actions_container,
        text="Asset Management",
        font=("Arial", 15, "bold"),
        fg=PRIMARY_DARK,
        bg=WHITE
    )

    section_title.grid(
        row=0,
        column=0,
        columnspan=3,
        sticky="w",
        padx=25,
        pady=(20, 15)
    )

    def style_button(
        parent,
        text,
        command,
        bg_color=PRIMARY
    ):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 11, "bold"),
            fg=WHITE,
            bg=bg_color,
            activeforeground=WHITE,
            activebackground=PRIMARY_DARK,
            relief="flat",
            bd=0,
            cursor="hand2",
            height=2
        )

        return button

    def refresh_statistics():

        try:
            total, available, assigned, maintenance = get_asset_statistics()

            total_value.set(
                str(total)
            )

            available_value.set(
                str(available)
            )

            assigned_value.set(
                str(assigned)
            )

            maintenance_value.set(
                str(maintenance)
            )

        except Exception as error:

            print(
                "Statistics Error:",
                error
            )

    def format_date(date_text):

        date_text = date_text.strip()

        if not date_text:
            return None

        formats = [
            "%Y-%m-%d",
            "%Y%m%d",
            "%d-%m-%Y",
            "%d/%m/%Y"
        ]

        for date_format in formats:

            try:

                date_object = datetime.strptime(
                    date_text,
                    date_format
                )

                return date_object.strftime(
                    "%Y-%m-%d"
                )

            except ValueError:
                continue

        raise ValueError(
            "Invalid date.\n\n"
            "Use one of these formats:\n"
            "YYYY-MM-DD\n"
            "YYYYMMDD\n"
            "DD-MM-YYYY\n"
            "DD/MM/YYYY"
        )

    def add_asset_window():

        window = tk.Toplevel(
            dashboard
        )

        window.title(
            "NTPC IT Asset Management - Add Asset"
        )

        window.geometry(
            "720x760"
        )

        window.configure(
            bg=BG_COLOR
        )

        window.resizable(
            False,
            False
        )

        title = tk.Label(
            window,
            text="Add New IT Asset",
            font=("Arial", 22, "bold"),
            fg=PRIMARY_DARK,
            bg=BG_COLOR
        )

        title.pack(
            pady=(25, 5)
        )

        subtitle = tk.Label(
            window,
            text="Register a new IT asset in the system",
            font=("Arial", 10),
            fg=TEXT_GRAY,
            bg=BG_COLOR
        )

        subtitle.pack(
            pady=(0, 20)
        )

        form_container = tk.Frame(
            window,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        form_container.pack(
            padx=35,
            fill="both",
            expand=True
        )

        form_frame = tk.Frame(
            form_container,
            bg=WHITE
        )

        form_frame.pack(
            padx=30,
            pady=20
        )

        entries = {}

        fields = [
            "Asset Code",
            "Asset Name",
            "Asset Type",
            "Manufacturer",
            "Model",
            "Serial Number",
            "Department",
            "Location",
            "Assigned To",
            "Purchase Date",
            "Warranty Expiry",
            "Status",
            "Remarks"
        ]

        required_fields = {
            "Asset Code",
            "Asset Name",
            "Asset Type",
            "Status"
        }

        asset_types = [
            "Desktop",
            "Laptop",
            "Monitor",
            "Printer",
            "Scanner",
            "Server",
            "Router",
            "Switch",
            "UPS",
            "Projector",
            "Network Device",
            "Storage Device",
            "Other"
        ]

        departments = [
            "IT Department",
            "Electrical Department",
            "Mechanical Department",
            "C&I Department",
            "Civil Department",
            "HR Department",
            "Finance Department",
            "Administration",
            "Operations",
            "Maintenance",
            "Other"
        ]

        locations = [
            "IT Office",
            "Administrative Building",
            "Control Room",
            "Server Room",
            "Main Plant",
            "Workshop",
            "Store",
            "Training Centre",
            "Other"
        ]

        statuses = [
            "Available",
            "Assigned",
            "Maintenance",
            "Retired"
        ]

        for row, field in enumerate(fields):

            display_name = field

            if field == "Purchase Date":
                display_name = "Purchase Date (YYYY-MM-DD)"

            if field == "Warranty Expiry":
                display_name = "Warranty Expiry (YYYY-MM-DD)"

            if field in required_fields:
                display_name += " *"

            label = tk.Label(
                form_frame,
                text=display_name,
                font=("Arial", 10, "bold" if field in required_fields else "normal"),
                fg=TEXT,
                bg=WHITE,
                width=27,
                anchor="w"
            )

            label.grid(
                row=row,
                column=0,
                sticky="w",
                padx=(0, 15),
                pady=5
            )

            if field == "Asset Type":

                widget = ttk.Combobox(
                    form_frame,
                    values=asset_types,
                    width=38
                )

            elif field == "Department":

                widget = ttk.Combobox(
                    form_frame,
                    values=departments,
                    width=38
                )

            elif field == "Location":

                widget = ttk.Combobox(
                    form_frame,
                    values=locations,
                    width=38
                )

            elif field == "Status":

                widget = ttk.Combobox(
                    form_frame,
                    values=statuses,
                    width=38,
                    state="readonly"
                )

                widget.set(
                    "Available"
                )

            elif field == "Remarks":

                widget = tk.Text(
                    form_frame,
                    width=40,
                    height=3,
                    font=("Arial", 10)
                )

            else:

                widget = tk.Entry(
                    form_frame,
                    width=40,
                    font=("Arial", 10)
                )

            widget.grid(
                row=row,
                column=1,
                sticky="w",
                padx=0,
                pady=5
            )

            entries[field] = widget

        def get_value(field):

            widget = entries[field]

            if isinstance(
                widget,
                tk.Text
            ):

                return widget.get(
                    "1.0",
                    tk.END
                ).strip()

            return widget.get().strip()

        def save_asset():

            asset_code = get_value(
                "Asset Code"
            )

            asset_name = get_value(
                "Asset Name"
            )

            asset_type = get_value(
                "Asset Type"
            )

            manufacturer = get_value(
                "Manufacturer"
            )

            model = get_value(
                "Model"
            )

            serial_number = get_value(
                "Serial Number"
            )

            department = get_value(
                "Department"
            )

            location = get_value(
                "Location"
            )

            assigned_to = get_value(
                "Assigned To"
            )

            purchase_date_text = get_value(
                "Purchase Date"
            )

            warranty_expiry_text = get_value(
                "Warranty Expiry"
            )

            status = get_value(
                "Status"
            )

            remarks = get_value(
                "Remarks"
            )

            if not asset_code:

                messagebox.showwarning(
                    "Required Field",
                    "Please enter Asset Code.",
                    parent=window
                )

                entries["Asset Code"].focus_set()

                return

            if not asset_name:

                messagebox.showwarning(
                    "Required Field",
                    "Please enter Asset Name.",
                    parent=window
                )

                entries["Asset Name"].focus_set()

                return

            if not asset_type:

                messagebox.showwarning(
                    "Required Field",
                    "Please select Asset Type.",
                    parent=window
                )

                entries["Asset Type"].focus_set()

                return

            if not status:

                messagebox.showwarning(
                    "Required Field",
                    "Please select Asset Status.",
                    parent=window
                )

                entries["Status"].focus_set()

                return

            try:

                purchase_date = format_date(
                    purchase_date_text
                )

            except ValueError as error:

                messagebox.showerror(
                    "Invalid Purchase Date",
                    str(error),
                    parent=window
                )

                entries["Purchase Date"].focus_set()

                return

            try:

                warranty_expiry = format_date(
                    warranty_expiry_text
                )

            except ValueError as error:

                messagebox.showerror(
                    "Invalid Warranty Expiry",
                    str(error),
                    parent=window
                )

                entries["Warranty Expiry"].focus_set()

                return

            if purchase_date and warranty_expiry:

                purchase_object = datetime.strptime(
                    purchase_date,
                    "%Y-%m-%d"
                )

                warranty_object = datetime.strptime(
                    warranty_expiry,
                    "%Y-%m-%d"
                )

                if warranty_object < purchase_object:

                    messagebox.showerror(
                        "Invalid Date",
                        "Warranty Expiry cannot be before Purchase Date.",
                        parent=window
                    )

                    entries["Warranty Expiry"].focus_set()

                    return

            if not serial_number:
                serial_number = None

            if not assigned_to:
                assigned_to = None

            try:

                add_asset(
                    asset_code,
                    asset_name,
                    asset_type,
                    manufacturer,
                    model,
                    serial_number,
                    department,
                    location,
                    assigned_to,
                    purchase_date,
                    warranty_expiry,
                    status,
                    remarks
                )

                messagebox.showinfo(
                    "Success",
                    "Asset Added Successfully!",
                    parent=window
                )

                refresh_statistics()

                window.destroy()

            except Exception as error:

                error_message = str(
                    error
                )

                if "Duplicate entry" in error_message:

                    messagebox.showerror(
                        "Duplicate Asset",
                        "Asset Code or Serial Number already exists.",
                        parent=window
                    )

                else:

                    messagebox.showerror(
                        "Unable to Add Asset",
                        error_message,
                        parent=window
                    )

        button = style_button(
            window,
            "Add Asset",
            save_asset,
            SUCCESS
        )

        button.pack(
            pady=20,
            ipadx=35
        )

    def create_asset_table(
        parent,
        columns,
        widths
    ):

        table_frame = tk.Frame(
            parent,
            bg=WHITE
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        vertical_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )

        horizontal_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=tree.xview
        )

        tree.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                width=widths.get(
                    column,
                    120
                ),
                anchor="center",
                minwidth=70
            )

        tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        vertical_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        horizontal_scrollbar.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        table_frame.grid_rowconfigure(
            0,
            weight=1
        )

        table_frame.grid_columnconfigure(
            0,
            weight=1
        )

        return tree

    def insert_records(
        tree,
        records
    ):

        for item in tree.get_children():

            tree.delete(
                item
            )

        for record in records:

            tree.insert(
                "",
                "end",
                values=record
            )

    def view_assets_window():

        window = tk.Toplevel(
            dashboard
        )

        window.title(
            "NTPC IT Asset Management - View Assets"
        )

        window.geometry(
            "1450x650"
        )

        window.configure(
            bg=BG_COLOR
        )

        title = tk.Label(
            window,
            text="IT Asset Records",
            font=("Arial", 22, "bold"),
            fg=PRIMARY_DARK,
            bg=BG_COLOR
        )

        title.pack(
            pady=(20, 5)
        )

        subtitle = tk.Label(
            window,
            text="Complete list of registered IT assets",
            font=("Arial", 10),
            fg=TEXT_GRAY,
            bg=BG_COLOR
        )

        subtitle.pack(
            pady=(0, 10)
        )

        table_container = tk.Frame(
            window,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        table_container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        columns = (
            "ID",
            "Asset Code",
            "Asset Name",
            "Type",
            "Manufacturer",
            "Model",
            "Serial Number",
            "Department",
            "Location",
            "Assigned To",
            "Purchase Date",
            "Warranty",
            "Status",
            "Remarks",
            "Created At"
        )

        widths = {
            "ID": 55,
            "Asset Code": 100,
            "Asset Name": 150,
            "Type": 100,
            "Manufacturer": 120,
            "Model": 110,
            "Serial Number": 140,
            "Department": 160,
            "Location": 130,
            "Assigned To": 130,
            "Purchase Date": 110,
            "Warranty": 110,
            "Status": 100,
            "Remarks": 180,
            "Created At": 140
        }

        tree = create_asset_table(
            table_container,
            columns,
            widths
        )

        try:

            records = get_all_assets()

            insert_records(
                tree,
                records
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error),
                parent=window
            )

    def search_asset_window():

        window = tk.Toplevel(
            dashboard
        )

        window.title(
            "NTPC IT Asset Management - Search Asset"
        )

        window.geometry(
            "1450x650"
        )

        window.configure(
            bg=BG_COLOR
        )

        title = tk.Label(
            window,
            text="Search IT Asset",
            font=("Arial", 22, "bold"),
            fg=PRIMARY_DARK,
            bg=BG_COLOR
        )

        title.pack(
            pady=(20, 5)
        )

        subtitle = tk.Label(
            window,
            text="Search using Asset Code, Name, Type, Serial Number, Department or Location",
            font=("Arial", 10),
            fg=TEXT_GRAY,
            bg=BG_COLOR
        )

        subtitle.pack(
            pady=(0, 10)
        )

        search_frame = tk.Frame(
            window,
            bg=BG_COLOR
        )

        search_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        search_entry = tk.Entry(
            search_frame,
            width=45,
            font=("Arial", 11),
            bd=1,
            relief="solid"
        )

        search_entry.pack(
            side="left",
            padx=(0, 10)
        )

        table_container = tk.Frame(
            window,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        table_container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        columns = (
            "ID",
            "Asset Code",
            "Asset Name",
            "Type",
            "Manufacturer",
            "Model",
            "Serial Number",
            "Department",
            "Location",
            "Assigned To",
            "Purchase Date",
            "Warranty",
            "Status",
            "Remarks",
            "Created At"
        )

        widths = {
            "ID": 55,
            "Asset Code": 100,
            "Asset Name": 150,
            "Type": 100,
            "Manufacturer": 120,
            "Model": 110,
            "Serial Number": 140,
            "Department": 160,
            "Location": 130,
            "Assigned To": 130,
            "Purchase Date": 110,
            "Warranty": 110,
            "Status": 100,
            "Remarks": 180,
            "Created At": 140
        }

        tree = create_asset_table(
            table_container,
            columns,
            widths
        )

        def perform_search():

            text = search_entry.get().strip()

            if not text:

                messagebox.showwarning(
                    "Search",
                    "Please enter something to search.",
                    parent=window
                )

                search_entry.focus_set()

                return

            try:

                records = search_assets(
                    text
                )

                insert_records(
                    tree,
                    records
                )

                if not records:

                    messagebox.showinfo(
                        "Search",
                        "No matching asset found.",
                        parent=window
                    )

            except Exception as error:

                messagebox.showerror(
                    "Search Error",
                    str(error),
                    parent=window
                )

        def clear_search():

            search_entry.delete(
                0,
                tk.END
            )

            insert_records(
                tree,
                []
            )

            search_entry.focus_set()

        search_button = style_button(
            search_frame,
            "Search",
            perform_search,
            PRIMARY
        )

        search_button.pack(
            side="left",
            padx=5,
            ipadx=15
        )

        clear_button = tk.Button(
            search_frame,
            text="Clear",
            command=clear_search,
            font=("Arial", 10, "bold"),
            fg=WHITE,
            bg=PRIMARY_DARK,
            activeforeground=WHITE,
            activebackground="#002A52",
            relief="flat",
            cursor="hand2",
            height=2
        )

        clear_button.pack(
            side="left",
            padx=5,
            ipadx=15
        )

        search_entry.bind(
            "<Return>",
            lambda event: perform_search()
        )

        search_entry.focus_set()

    def update_asset_window():

        window = tk.Toplevel(
            dashboard
        )

        window.title(
            "NTPC IT Asset Management - Update Asset"
        )

        window.geometry(
            "700x720"
        )

        window.configure(
            bg=BG_COLOR
        )

        window.resizable(
            False,
            False
        )

        title = tk.Label(
            window,
            text="Update IT Asset",
            font=("Arial", 22, "bold"),
            fg=PRIMARY_DARK,
            bg=BG_COLOR
        )

        title.pack(
            pady=(20, 5)
        )

        code_frame = tk.Frame(
            window,
            bg=BG_COLOR
        )

        code_frame.pack(
            pady=10
        )

        tk.Label(
            code_frame,
            text="Asset Code",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=BG_COLOR
        ).pack(
            side="left",
            padx=10
        )

        asset_code_entry = tk.Entry(
            code_frame,
            width=30,
            font=("Arial", 10)
        )

        asset_code_entry.pack(
            side="left",
            padx=5
        )

        form_container = tk.Frame(
            window,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        form_container.pack(
            padx=30,
            fill="both",
            expand=True
        )

        form_frame = tk.Frame(
            form_container,
            bg=WHITE
        )

        form_frame.pack(
            padx=25,
            pady=15
        )

        fields = [
            "Asset Name",
            "Asset Type",
            "Manufacturer",
            "Model",
            "Serial Number",
            "Department",
            "Location",
            "Purchase Date",
            "Warranty Expiry",
            "Status",
            "Remarks"
        ]

        entries = {}

        asset_types = [
            "Desktop",
            "Laptop",
            "Monitor",
            "Printer",
            "Scanner",
            "Server",
            "Router",
            "Switch",
            "UPS",
            "Projector",
            "Network Device",
            "Storage Device",
            "Other"
        ]

        departments = [
            "IT Department",
            "Electrical Department",
            "Mechanical Department",
            "C&I Department",
            "Civil Department",
            "HR Department",
            "Finance Department",
            "Administration",
            "Operations",
            "Maintenance",
            "Other"
        ]

        locations = [
            "IT Office",
            "Administrative Building",
            "Control Room",
            "Server Room",
            "Main Plant",
            "Workshop",
            "Store",
            "Training Centre",
            "Other"
        ]

        statuses = [
            "Available",
            "Assigned",
            "Maintenance",
            "Retired"
        ]

        for row, field in enumerate(fields):

            label_text = field

            if field == "Purchase Date":
                label_text = "Purchase Date (YYYY-MM-DD)"

            elif field == "Warranty Expiry":
                label_text = "Warranty Expiry (YYYY-MM-DD)"

            tk.Label(
                form_frame,
                text=label_text,
                font=("Arial", 10),
                fg=TEXT,
                bg=WHITE,
                width=25,
                anchor="w"
            ).grid(
                row=row,
                column=0,
                sticky="w",
                padx=5,
                pady=5
            )

            if field == "Asset Type":

                widget = ttk.Combobox(
                    form_frame,
                    values=asset_types,
                    width=38
                )

            elif field == "Department":

                widget = ttk.Combobox(
                    form_frame,
                    values=departments,
                    width=38
                )

            elif field == "Location":

                widget = ttk.Combobox(
                    form_frame,
                    values=locations,
                    width=38
                )

            elif field == "Status":

                widget = ttk.Combobox(
                    form_frame,
                    values=statuses,
                    width=38
                )

            elif field == "Remarks":

                widget = tk.Text(
                    form_frame,
                    width=40,
                    height=3,
                    font=("Arial", 10)
                )

            else:

                widget = tk.Entry(
                    form_frame,
                    width=40,
                    font=("Arial", 10)
                )

            widget.grid(
                row=row,
                column=1,
                sticky="w",
                padx=5,
                pady=5
            )

            entries[field] = widget

        def get_widget_value(
            field
        ):

            widget = entries[field]

            if isinstance(
                widget,
                tk.Text
            ):

                return widget.get(
                    "1.0",
                    tk.END
                ).strip()

            return widget.get().strip()

        def load_asset():

            code = asset_code_entry.get().strip()

            if not code:

                messagebox.showwarning(
                    "Required",
                    "Please enter Asset Code.",
                    parent=window
                )

                asset_code_entry.focus_set()

                return

            try:

                record = get_asset_by_code(
                    code
                )

                if not record:

                    messagebox.showerror(
                        "Not Found",
                        "Asset not found.",
                        parent=window
                    )

                    return

                values = {
                    "Asset Name": record[2],
                    "Asset Type": record[3],
                    "Manufacturer": record[4],
                    "Model": record[5],
                    "Serial Number": record[6],
                    "Department": record[7],
                    "Location": record[8],
                    "Purchase Date": record[10],
                    "Warranty Expiry": record[11],
                    "Status": record[12],
                    "Remarks": record[13]
                }

                for field in fields:

                    widget = entries[field]

                    if isinstance(
                        widget,
                        tk.Text
                    ):

                        widget.delete(
                            "1.0",
                            tk.END
                        )

                        if values[field] is not None:

                            widget.insert(
                                "1.0",
                                str(values[field])
                            )

                    else:

                        widget.delete(
                            0,
                            tk.END
                        )

                        if values[field] is not None:

                            widget.insert(
                                0,
                                str(values[field])
                            )

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=window
                )

        def save_update():

            code = asset_code_entry.get().strip()

            if not code:

                messagebox.showwarning(
                    "Required",
                    "Please enter Asset Code.",
                    parent=window
                )

                return

            try:

                purchase_date = format_date(
                    get_widget_value(
                        "Purchase Date"
                    )
                )

                warranty_expiry = format_date(
                    get_widget_value(
                        "Warranty Expiry"
                    )
                )

            except ValueError as error:

                messagebox.showerror(
                    "Invalid Date",
                    str(error),
                    parent=window
                )

                return

            if purchase_date and warranty_expiry:

                purchase_object = datetime.strptime(
                    purchase_date,
                    "%Y-%m-%d"
                )

                warranty_object = datetime.strptime(
                    warranty_expiry,
                    "%Y-%m-%d"
                )

                if warranty_object < purchase_object:

                    messagebox.showerror(
                        "Invalid Date",
                        "Warranty Expiry cannot be before Purchase Date.",
                        parent=window
                    )

                    return

            try:

                result = update_asset(
                    code,
                    get_widget_value("Asset Name"),
                    get_widget_value("Asset Type"),
                    get_widget_value("Manufacturer"),
                    get_widget_value("Model"),
                    get_widget_value("Serial Number"),
                    get_widget_value("Department"),
                    get_widget_value("Location"),
                    purchase_date,
                    warranty_expiry,
                    get_widget_value("Status"),
                    get_widget_value("Remarks")
                )

                if result:

                    messagebox.showinfo(
                        "Success",
                        "Asset Updated Successfully!",
                        parent=window
                    )

                    refresh_statistics()

                    window.destroy()

                else:

                    messagebox.showwarning(
                        "Update",
                        "No asset was updated.",
                        parent=window
                    )

            except Exception as error:

                messagebox.showerror(
                    "Update Error",
                    str(error),
                    parent=window
                )

        button_frame = tk.Frame(
            window,
            bg=BG_COLOR
        )

        button_frame.pack(
            pady=15
        )

        load_button = style_button(
            button_frame,
            "Load Asset",
            load_asset,
            PRIMARY
        )

        load_button.pack(
            side="left",
            padx=8,
            ipadx=10
        )

        update_button = style_button(
            button_frame,
            "Update Asset",
            save_update,
            SUCCESS
        )

        update_button.pack(
            side="left",
            padx=8,
            ipadx=10
        )

    def assign_asset_window():

        window = tk.Toplevel(
            dashboard
        )

        window.title(
            "NTPC IT Asset Management - Assign Asset"
        )

        window.geometry(
            "600x470"
        )

        window.configure(
            bg=BG_COLOR
        )

        window.resizable(
            False,
            False
        )

        title = tk.Label(
            window,
            text="Assign IT Asset",
            font=("Arial", 22, "bold"),
            fg=PRIMARY_DARK,
            bg=BG_COLOR
        )

        title.pack(
            pady=(25, 5)
        )

        subtitle = tk.Label(
            window,
            text="Assign an available asset to an employee or department",
            font=("Arial", 10),
            fg=TEXT_GRAY,
            bg=BG_COLOR
        )

        subtitle.pack(
            pady=(0, 20)
        )

        form = tk.Frame(
            window,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        form.pack(
            padx=40,
            fill="both",
            expand=True
        )

        fields = [
            "Asset Code",
            "Assign To",
            "Department",
            "Location"
        ]

        entries = {}

        for row, field in enumerate(fields):

            tk.Label(
                form,
                text=field,
                font=("Arial", 10, "bold"),
                fg=TEXT,
                bg=WHITE,
                width=18,
                anchor="w"
            ).grid(
                row=row,
                column=0,
                padx=(25, 10),
                pady=15,
                sticky="w"
            )

            if field == "Department":

                widget = ttk.Combobox(
                    form,
                    values=[
                        "IT Department",
                        "Electrical Department",
                        "Mechanical Department",
                        "C&I Department",
                        "Civil Department",
                        "HR Department",
                        "Finance Department",
                        "Administration",
                        "Operations",
                        "Maintenance",
                        "Other"
                    ],
                    width=30
                )

            elif field == "Location":

                widget = ttk.Combobox(
                    form,
                    values=[
                        "IT Office",
                        "Administrative Building",
                        "Control Room",
                        "Server Room",
                        "Main Plant",
                        "Workshop",
                        "Store",
                        "Training Centre",
                        "Other"
                    ],
                    width=30
                )

            else:

                widget = tk.Entry(
                    form,
                    width=33,
                    font=("Arial", 10)
                )

            widget.grid(
                row=row,
                column=1,
                padx=(0, 25),
                pady=15
            )

            entries[field] = widget

        def assign():

            code = entries["Asset Code"].get().strip()

            assigned_to = entries["Assign To"].get().strip()

            department = entries["Department"].get().strip()

            location = entries["Location"].get().strip()

            if not code:

                messagebox.showwarning(
                    "Required",
                    "Please enter Asset Code.",
                    parent=window
                )

                return

            if not assigned_to:

                messagebox.showwarning(
                    "Required",
                    "Please enter the employee or person to whom the asset is assigned.",
                    parent=window
                )

                return

            try:

                asset = get_asset_by_code(
                    code
                )

                if not asset:

                    messagebox.showerror(
                        "Not Found",
                        "Asset Code not found.",
                        parent=window
                    )

                    return

                result = assign_asset(
                    code,
                    assigned_to,
                    department,
                    location
                )

                if result:

                    messagebox.showinfo(
                        "Success",
                        "Asset Assigned Successfully!",
                        parent=window
                    )

                    refresh_statistics()

                    window.destroy()

                else:

                    messagebox.showerror(
                        "Assignment Failed",
                        "Asset could not be assigned.",
                        parent=window
                    )

            except Exception as error:

                messagebox.showerror(
                    "Assignment Error",
                    str(error),
                    parent=window
                )

        button = style_button(
            window,
            "Assign Asset",
            assign,
            WARNING
        )

        button.pack(
            pady=20,
            ipadx=35
        )

    def delete_asset_window():

        window = tk.Toplevel(
            dashboard
        )

        window.title(
            "NTPC IT Asset Management - Delete Asset"
        )

        window.geometry(
            "1250x680"
        )

        window.configure(
            bg=BG_COLOR
        )

        title = tk.Label(
            window,
            text="Delete IT Asset",
            font=("Arial", 22, "bold"),
            fg=DANGER,
            bg=BG_COLOR
        )

        title.pack(
            pady=(20, 5)
        )

        subtitle = tk.Label(
            window,
            text="Search, select and permanently remove an asset",
            font=("Arial", 10),
            fg=TEXT_GRAY,
            bg=BG_COLOR
        )

        subtitle.pack(
            pady=(0, 10)
        )

        search_frame = tk.Frame(
            window,
            bg=BG_COLOR
        )

        search_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        tk.Label(
            search_frame,
            text="Search",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=BG_COLOR
        ).pack(
            side="left",
            padx=(0, 10)
        )

        search_entry = tk.Entry(
            search_frame,
            width=42,
            font=("Arial", 10)
        )

        search_entry.pack(
            side="left",
            padx=5
        )

        table_container = tk.Frame(
            window,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        table_container.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=5
        )

        columns = (
            "ID",
            "Asset Code",
            "Asset Name",
            "Type",
            "Serial Number",
            "Department",
            "Location",
            "Assigned To",
            "Status"
        )

        widths = {
            "ID": 60,
            "Asset Code": 120,
            "Asset Name": 160,
            "Type": 110,
            "Serial Number": 150,
            "Department": 170,
            "Location": 140,
            "Assigned To": 150,
            "Status": 100
        }

        tree = create_asset_table(
            table_container,
            columns,
            widths
        )

        def load_delete_records(
            records
        ):

            for item in tree.get_children():

                tree.delete(
                    item
                )

            for record in records:

                values = (
                    record[0],
                    record[1],
                    record[2],
                    record[3],
                    record[6] or "Not Available",
                    record[7] or "Not Available",
                    record[8] or "Not Available",
                    record[9] or "Not Assigned",
                    record[12] or "Not Available"
                )

                tree.insert(
                    "",
                    "end",
                    values=values
                )

        def show_all_assets():

            try:

                load_delete_records(
                    get_all_assets()
                )

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=window
                )

        def perform_search():

            text = search_entry.get().strip()

            if not text:

                show_all_assets()

                return

            try:

                records = search_assets(
                    text
                )

                load_delete_records(
                    records
                )

                if not records:

                    messagebox.showinfo(
                        "Search",
                        "No matching asset found.",
                        parent=window
                    )

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=window
                )

        def clear_search():

            search_entry.delete(
                0,
                tk.END
            )

            show_all_assets()

            search_entry.focus_set()

        search_button = style_button(
            search_frame,
            "Search",
            perform_search,
            PRIMARY
        )

        search_button.pack(
            side="left",
            padx=5,
            ipadx=10
        )

        show_button = style_button(
            search_frame,
            "Show All",
            show_all_assets,
            SUCCESS
        )

        show_button.pack(
            side="left",
            padx=5,
            ipadx=10
        )

        clear_button = style_button(
            search_frame,
            "Clear",
            clear_search,
            PRIMARY_DARK
        )

        clear_button.pack(
            side="left",
            padx=5,
            ipadx=10
        )

        selected_frame = tk.Frame(
            window,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        selected_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        selected_code = tk.StringVar(
            value="None selected"
        )

        selected_name = tk.StringVar(
            value="-"
        )

        selected_status = tk.StringVar(
            value="-"
        )

        tk.Label(
            selected_frame,
            text="Selected Asset:",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            side="left",
            padx=(20, 8),
            pady=12
        )

        tk.Label(
            selected_frame,
            textvariable=selected_code,
            font=("Arial", 10, "bold"),
            fg=DANGER,
            bg=WHITE
        ).pack(
            side="left",
            padx=8
        )

        tk.Label(
            selected_frame,
            text="Name:",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            side="left",
            padx=(25, 5)
        )

        tk.Label(
            selected_frame,
            textvariable=selected_name,
            font=("Arial", 10),
            fg=TEXT_GRAY,
            bg=WHITE
        ).pack(
            side="left",
            padx=5
        )

        tk.Label(
            selected_frame,
            text="Status:",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            side="left",
            padx=(25, 5)
        )

        tk.Label(
            selected_frame,
            textvariable=selected_status,
            font=("Arial", 10),
            fg=TEXT_GRAY,
            bg=WHITE
        ).pack(
            side="left",
            padx=5
        )

        def update_selection(
            event=None
        ):

            selection = tree.selection()

            if not selection:

                selected_code.set(
                    "None selected"
                )

                selected_name.set(
                    "-"
                )

                selected_status.set(
                    "-"
                )

                return

            values = tree.item(
                selection[0],
                "values"
            )

            selected_code.set(
                values[1]
            )

            selected_name.set(
                values[2]
            )

            selected_status.set(
                values[8]
            )

        tree.bind(
            "<<TreeviewSelect>>",
            update_selection
        )

        def begin_delete():

            selection = tree.selection()

            if not selection:

                messagebox.showwarning(
                    "Select Asset",
                    "Please select an asset to delete.",
                    parent=window
                )

                return

            values = tree.item(
                selection[0],
                "values"
            )

            code = values[1]

            try:

                record = get_asset_by_code(
                    code
                )

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=window
                )

                return

            if not record:

                messagebox.showerror(
                    "Not Found",
                    "The selected asset no longer exists.",
                    parent=window
                )

                show_all_assets()

                return

            confirmation_window = tk.Toplevel(
                window
            )

            confirmation_window.title(
                "Confirm Delete"
            )

            confirmation_window.geometry(
                "600x620"
            )

            confirmation_window.configure(
                bg=BG_COLOR
            )

            confirmation_window.resizable(
                False,
                False
            )

            confirmation_window.transient(
                window
            )

            confirmation_window.grab_set()

            tk.Label(
                confirmation_window,
                text="Confirm Asset Deletion",
                font=("Arial", 22, "bold"),
                fg=DANGER,
                bg=BG_COLOR
            ).pack(
                pady=(25, 5)
            )

            tk.Label(
                confirmation_window,
                text="This action cannot be undone.",
                font=("Arial", 11, "bold"),
                fg=DANGER,
                bg=BG_COLOR
            ).pack(
                pady=(0, 20)
            )

            asset_frame = tk.Frame(
                confirmation_window,
                bg=WHITE,
                bd=1,
                relief="solid"
            )

            asset_frame.pack(
                fill="x",
                padx=35,
                pady=5
            )

            asset_details = [
                ("Asset Code", record[1]),
                ("Asset Name", record[2]),
                ("Asset Type", record[3]),
                ("Serial Number", record[6] or "Not Available"),
                ("Department", record[7] or "Not Available"),
                ("Location", record[8] or "Not Available")
            ]

            for row, (
                label,
                value
            ) in enumerate(asset_details):

                tk.Label(
                    asset_frame,
                    text=label + ":",
                    font=("Arial", 10, "bold"),
                    fg=TEXT,
                    bg=WHITE,
                    width=18,
                    anchor="w"
                ).grid(
                    row=row,
                    column=0,
                    padx=(20, 10),
                    pady=7,
                    sticky="w"
                )

                tk.Label(
                    asset_frame,
                    text=str(value),
                    font=("Arial", 10),
                    fg=TEXT_GRAY,
                    bg=WHITE,
                    anchor="w"
                ).grid(
                    row=row,
                    column=1,
                    padx=10,
                    pady=7,
                    sticky="w"
                )

            admin_frame = tk.Frame(
                confirmation_window,
                bg=WHITE,
                bd=1,
                relief="solid"
            )

            admin_frame.pack(
                fill="x",
                padx=35,
                pady=15
            )

            tk.Label(
                admin_frame,
                text="Deletion Authorized By",
                font=("Arial", 11, "bold"),
                fg=PRIMARY_DARK,
                bg=WHITE
            ).grid(
                row=0,
                column=0,
                columnspan=2,
                padx=20,
                pady=(12, 8),
                sticky="w"
            )

            admin_details = [
                ("Admin Name", admin_name),
                ("User ID", admin_user_id if admin_user_id is not None else "Not Available"),
                ("Username", admin_username if admin_username else "Not Available")
            ]

            for row, (
                label,
                value
            ) in enumerate(
                admin_details,
                start=1
            ):

                tk.Label(
                    admin_frame,
                    text=label + ":",
                    font=("Arial", 10, "bold"),
                    fg=TEXT,
                    bg=WHITE,
                    width=18,
                    anchor="w"
                ).grid(
                    row=row,
                    column=0,
                    padx=(20, 10),
                    pady=5,
                    sticky="w"
                )

                tk.Label(
                    admin_frame,
                    text=str(value),
                    font=("Arial", 10),
                    fg=TEXT_GRAY,
                    bg=WHITE
                ).grid(
                    row=row,
                    column=1,
                    padx=10,
                    pady=5,
                    sticky="w"
                )

            password_frame = tk.Frame(
                confirmation_window,
                bg=BG_COLOR
            )

            password_frame.pack(
                pady=5
            )

            tk.Label(
                password_frame,
                text="Admin Password:",
                font=("Arial", 10, "bold"),
                fg=TEXT,
                bg=BG_COLOR
            ).grid(
                row=0,
                column=0,
                padx=10,
                pady=8
            )

            password_entry = tk.Entry(
                password_frame,
                width=28,
                show="*",
                font=("Arial", 11)
            )

            password_entry.grid(
                row=0,
                column=1,
                padx=10,
                pady=8
            )

            button_frame = tk.Frame(
                confirmation_window,
                bg=BG_COLOR
            )

            button_frame.pack(
                pady=15
            )

            def verify_and_delete():

                password = password_entry.get()

                if not password:

                    messagebox.showwarning(
                        "Password Required",
                        "Please enter the admin password.",
                        parent=confirmation_window
                    )

                    password_entry.focus_set()

                    return

                if not admin_username:

                    messagebox.showerror(
                        "Authentication Error",
                        "Admin username is not available. Please logout and login again.",
                        parent=confirmation_window
                    )

                    return

                connection = None
                cursor = None

                try:

                    connection = connect_database()

                    if connection is None:

                        messagebox.showerror(
                            "Database Error",
                            "Unable to connect to the database.",
                            parent=confirmation_window
                        )

                        return

                    cursor = connection.cursor(
                        dictionary=True
                    )

                    cursor.execute(
                        """
                        SELECT User_Id, Username, Password, Full_Name, Role
                        FROM Users
                        WHERE Username = %s
                        """,
                        (
                            admin_username,
                        )
                    )

                    user = cursor.fetchone()

                    if not user:

                        messagebox.showerror(
                            "Authentication Error",
                            "Admin account could not be found.",
                            parent=confirmation_window
                        )

                        return

                    if str(
                        user.get(
                            "Role",
                            ""
                        )
                    ).lower() != "admin":

                        messagebox.showerror(
                            "Authorization Error",
                            "Only an administrator can delete assets.",
                            parent=confirmation_window
                        )

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
                        password.encode(
                            "utf-8"
                        ),
                        stored_password
                    ):

                        messagebox.showerror(
                            "Incorrect Password",
                            "Incorrect admin password.\n\nThe asset has NOT been deleted.",
                            parent=confirmation_window
                        )

                        password_entry.delete(
                            0,
                            tk.END
                        )

                        password_entry.focus_set()

                        return

                except Exception as error:

                    messagebox.showerror(
                        "Authentication Error",
                        str(error),
                        parent=confirmation_window
                    )

                    return

                finally:

                    if cursor is not None:

                        try:
                            cursor.close()
                        except:
                            pass

                    if connection is not None:

                        try:
                            connection.close()
                        except:
                            pass

                try:

                    result = delete_asset(
                        code
                    )

                    if result:

                        messagebox.showinfo(
                            "Asset Deleted",
                            f"Asset '{code}' was deleted successfully.",
                            parent=confirmation_window
                        )

                        confirmation_window.destroy()

                        show_all_assets()

                        update_selection()

                        refresh_statistics()

                    else:

                        messagebox.showerror(
                            "Not Found",
                            "The asset could not be deleted because it no longer exists.",
                            parent=confirmation_window
                        )

                        confirmation_window.destroy()

                        show_all_assets()

                except Exception as error:

                    messagebox.showerror(
                        "Delete Error",
                        str(error),
                        parent=confirmation_window
                    )

            cancel_button = tk.Button(
                button_frame,
                text="Cancel",
                command=confirmation_window.destroy,
                font=("Arial", 10, "bold"),
                bg=PRIMARY_DARK,
                fg=WHITE,
                activebackground="#002A52",
                activeforeground=WHITE,
                relief="flat",
                cursor="hand2",
                width=14,
                height=2
            )

            cancel_button.pack(
                side="left",
                padx=8
            )

            delete_button = tk.Button(
                button_frame,
                text="Confirm Delete",
                command=verify_and_delete,
                font=("Arial", 10, "bold"),
                bg=DANGER,
                fg=WHITE,
                activebackground="#A91F1F",
                activeforeground=WHITE,
                relief="flat",
                cursor="hand2",
                width=16,
                height=2
            )

            delete_button.pack(
                side="left",
                padx=8
            )

            password_entry.focus_set()

        delete_button = style_button(
            window,
            "Delete Selected Asset",
            begin_delete,
            DANGER
        )

        delete_button.pack(
            pady=12,
            ipadx=30
        )

        tree.bind(
            "<Double-1>",
            lambda event: begin_delete()
        )

        show_all_assets()

        search_entry.focus_set()

    buttons = [
        (
            "Add Asset",
            add_asset_window,
            PRIMARY
        ),
        (
            "View Assets",
            view_assets_window,
            PRIMARY
        ),
        (
            "Search Asset",
            search_asset_window,
            PRIMARY
        ),
        (
            "Update Asset",
            update_asset_window,
            PRIMARY
        ),
        (
            "Assign Asset",
            assign_asset_window,
            WARNING
        ),
        (
            "Delete Asset",
            delete_asset_window,
            DANGER
        )
    ]

    for index, (
        text,
        command,
        color
    ) in enumerate(buttons):

        row = (
            index // 3
        ) + 1

        column = index % 3

        button = style_button(
            actions_container,
            text,
            command,
            color
        )

        button.grid(
            row=row,
            column=column,
            sticky="ew",
            padx=20,
            pady=10
        )

    for column in range(3):

        actions_container.grid_columnconfigure(
            column,
            weight=1
        )

    bottom_frame = tk.Frame(
        content,
        bg=BG_COLOR
    )

    bottom_frame.pack(
        fill="x",
        padx=60,
        pady=(20, 0)
    )

    refresh_button = tk.Button(
        bottom_frame,
        text="Refresh Dashboard",
        command=refresh_statistics,
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=PRIMARY_DARK,
        activebackground="#E8F1FF",
        activeforeground=PRIMARY_DARK,
        relief="solid",
        bd=1,
        cursor="hand2",
        width=20,
        height=2
    )

    refresh_button.pack(
        side="left"
    )

    def logout():

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?",
            parent=dashboard
        )

        if not answer:
            return

        dashboard.destroy()

        try:

            from login import open_login

            open_login()

        except Exception as error:

            print(
                "Logout Error:",
                error
            )

    logout_button = tk.Button(
        bottom_frame,
        text="Logout",
        command=logout,
        font=("Arial", 10, "bold"),
        bg=PRIMARY_DARK,
        fg=WHITE,
        activebackground="#002A52",
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2",
        width=14,
        height=2
    )

    logout_button.pack(
        side="right"
    )

    footer = tk.Label(
        content,
        text="NTPC IT Asset Management System • Kahalgaon Super Thermal Power Station",
        font=("Arial", 9),
        fg=TEXT_GRAY,
        bg=BG_COLOR
    )

    footer.pack(
        pady=(20, 0)
    )

    refresh_statistics()

    dashboard.mainloop()


if __name__ == "__main__":
    open_dashboard()