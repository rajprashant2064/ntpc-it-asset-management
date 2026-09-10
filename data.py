import random
from datetime import date, timedelta
from database import connect_database as get_connection

random.seed(20260830)

DEPARTMENTS = [
    "IT Department", "HR Department", "Finance Department", "Administration",
    "Operations", "Electrical", "Mechanical", "C&I", "Civil", "Stores",
    "Procurement", "Safety", "Security", "Training Centre", "Medical",
    "Commercial", "Legal", "Vigilance"
]

LOCATIONS = [
    "IT Department", "Admin Building", "Main Plant", "Control Room",
    "Training Centre", "CISF Office", "HR Building", "Finance Building",
    "Main Store", "Electrical Department", "Mechanical Department",
    "C&I Department", "Guest House", "Workshop", "Medical Centre",
    "Security Office"
]

EMPLOYEES = [
    ("EMP-CLG-1001", "Amit Kumar"), ("EMP-CLG-1002", "Rahul Singh"),
    ("EMP-CLG-1003", "Priya Sharma"), ("EMP-CLG-1004", "Ravi Kumar"),
    ("EMP-CLG-1005", "Neha Kumari"), ("EMP-CLG-1006", "Vikash Singh"),
    ("EMP-CLG-1007", "Ankit Raj"), ("EMP-CLG-1008", "Pooja Kumari"),
    ("EMP-CLG-1009", "Sandeep Kumar"), ("EMP-CLG-1010", "Karan Singh"),
    ("EMP-CLG-1011", "Sneha Sharma"), ("EMP-CLG-1012", "Manish Kumar"),
    ("EMP-CLG-1013", "Rohit Raj"), ("EMP-CLG-1014", "Anjali Singh"),
    ("EMP-CLG-1015", "Deepak Kumar"), ("EMP-CLG-1016", "Nisha Kumari"),
    ("EMP-CLG-1017", "Arjun Singh"), ("EMP-CLG-1018", "Kavita Sharma"),
    ("EMP-CLG-1019", "Vivek Kumar"), ("EMP-CLG-1020", "Shweta Singh")
]

ASSET_TYPES = [
    ("Laptop", [("Dell", "Latitude 5420"), ("Dell", "Latitude 5520"), ("HP", "ProBook 440 G9"), ("HP", "ProBook 450 G9"), ("Lenovo", "ThinkPad E14 Gen 4"), ("Lenovo", "ThinkPad L14 Gen 3")]),
    ("Desktop", [("Dell", "OptiPlex 3080"), ("Dell", "OptiPlex 5090"), ("HP", "ProDesk 400 G7"), ("HP", "ProDesk 600 G6"), ("Lenovo", "ThinkCentre M70s")]),
    ("Monitor", [("Dell", "P2422H"), ("Dell", "E2422H"), ("HP", "P24v G4"), ("Lenovo", "ThinkVision T24i")]),
    ("Printer", [("HP", "LaserJet Pro M404dn"), ("HP", "LaserJet Enterprise M507dn"), ("Canon", "imageCLASS LBP226dw"), ("Brother", "HL-L6200DW")]),
    ("Scanner", [("Canon", "imageFORMULA DR-C240"), ("Epson", "DS-530 II"), ("HP", "ScanJet Pro 3500")]),
    ("Network Switch", [("Cisco", "Catalyst 2960X"), ("Cisco", "Catalyst 9200"), ("HPE", "Aruba 2530"), ("HPE", "Aruba 2930F")]),
    ("Router", [("Cisco", "ISR 4331"), ("Cisco", "ISR 4321"), ("MikroTik", "CCR2004")]),
    ("Firewall", [("Fortinet", "FortiGate 60F"), ("Fortinet", "FortiGate 100F"), ("Sophos", "XGS 116")]),
    ("Server", [("Dell", "PowerEdge R740"), ("Dell", "PowerEdge R750"), ("HPE", "ProLiant DL380 Gen10"), ("HPE", "ProLiant DL380 Gen11")]),
    ("UPS", [("APC", "Smart-UPS 1500"), ("APC", "Smart-UPS 3000"), ("Numeric", "Keor 3KVA"), ("Eaton", "9E 3000i")]),
    ("Projector", [("Epson", "EB-X06"), ("BenQ", "MH733"), ("ViewSonic", "PA503W")]),
    ("IP Phone", [("Cisco", "IP Phone 8841"), ("Cisco", "IP Phone 7821"), ("Yealink", "T46U")]),
    ("Storage Device", [("Synology", "DS920+"), ("QNAP", "TS-464"), ("Dell", "PowerVault ME4024")]),
    ("Tablet", [("Samsung", "Galaxy Tab S8"), ("Lenovo", "Tab P11"), ("Apple", "iPad 10th Gen")])
]

STATUS_WEIGHTS = [("Assigned", 55), ("Available", 25), ("Maintenance", 10), ("Retired", 10)]

REMARKS = {
    "Assigned": ["In active use", "Assigned to department employee", "Operational", "In regular use"],
    "Available": ["Available in IT Store", "Ready for allocation", "Spare equipment", "Available for deployment"],
    "Maintenance": ["Under maintenance", "Service request raised", "Awaiting repair", "Preventive maintenance"],
    "Retired": ["Retired from service", "Awaiting disposal", "End of useful life", "Decommissioned"]
}

CODES = {
    "Laptop": "LT", "Desktop": "DT", "Monitor": "MN", "Printer": "PR",
    "Scanner": "SC", "Network Switch": "SW", "Router": "RT", "Firewall": "FW",
    "Server": "SV", "UPS": "UPS", "Projector": "PJ", "IP Phone": "IP",
    "Storage Device": "ST", "Tablet": "TB"
}

def random_date():
    start = date(2019, 1, 1)
    end = date(2026, 8, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

def weighted_status():
    return random.choices(
        [x[0] for x in STATUS_WEIGHTS],
        weights=[x[1] for x in STATUS_WEIGHTS],
        k=1
    )[0]

def build_assets(total):
    records = []
    for number in range(1, total + 1):
        asset_type, models = random.choice(ASSET_TYPES)
        manufacturer, model = random.choice(models)
        status = weighted_status()
        department = random.choice(DEPARTMENTS)
        location = random.choice(LOCATIONS)

        if status == "Assigned":
            employee_id, employee_name = random.choice(EMPLOYEES)
            assigned_to = f"{employee_name} ({employee_id})"
        else:
            assigned_to = None

        purchase_date = random_date()
        warranty_expiry = purchase_date + timedelta(days=365 * random.choice([1, 2, 3, 3, 4, 5]))
        asset_code = f"NTPC-CLG-{CODES[asset_type]}-{number:05d}"
        serial_number = f"{manufacturer[:4].upper()}-CLG-{number:07d}"

        records.append((
            asset_code,
            f"{manufacturer} {model}",
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
            random.choice(REMARKS[status])
        ))
    return records

def insert_assets(total=10000):
    connection = get_connection()
    if connection is None:
        raise RuntimeError("Unable to connect to the database.")

    cursor = connection.cursor()
    query = '''
    INSERT INTO Assets
    (Asset_Code, Asset_Name, Asset_Type, Manufacturer, Model, Serial_Number,
     Department, Location, Assigned_To, Purchase_Date, Warranty_Expiry, Status, Remarks)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    try:
        records = build_assets(total)
        for start in range(0, total, 500):
            cursor.executemany(query, records[start:start + 500])
            connection.commit()
            print(f"Inserted {min(start + 500, total)} / {total}")
        print(f"Successfully inserted {total} synthetic NTPC-CLG assets.")
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    insert_assets(10000)
