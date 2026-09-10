from database import connect_database as get_connection


def add_asset(
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
):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO Assets
    (
        Asset_Code,
        Asset_Name,
        Asset_Type,
        Manufacturer,
        Model,
        Serial_Number,
        Department,
        Location,
        Assigned_To,
        Purchase_Date,
        Warranty_Expiry,
        Status,
        Remarks
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
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

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()


def get_all_assets():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Assets ORDER BY Asset_ID DESC"
    )

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records


def search_assets(search_text):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT * FROM Assets
    WHERE Asset_Code LIKE %s
       OR Asset_Name LIKE %s
       OR Asset_Type LIKE %s
       OR Manufacturer LIKE %s
       OR Model LIKE %s
       OR Serial_Number LIKE %s
       OR Department LIKE %s
       OR Location LIKE %s
       OR Assigned_To LIKE %s
       OR Status LIKE %s
    ORDER BY Asset_ID DESC
    """

    search_value = f"%{search_text}%"

    cursor.execute(
        query,
        (
            search_value,
            search_value,
            search_value,
            search_value,
            search_value,
            search_value,
            search_value,
            search_value,
            search_value,
            search_value
        )
    )

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records


def get_asset_by_code(asset_code):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Assets WHERE Asset_Code = %s",
        (asset_code,)
    )

    record = cursor.fetchone()

    cursor.close()
    connection.close()

    return record


def update_asset(
    asset_code,
    asset_name,
    asset_type,
    manufacturer,
    model,
    serial_number,
    department,
    location,
    purchase_date,
    warranty_expiry,
    status,
    remarks
):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE Assets
    SET Asset_Name = %s,
        Asset_Type = %s,
        Manufacturer = %s,
        Model = %s,
        Serial_Number = %s,
        Department = %s,
        Location = %s,
        Purchase_Date = %s,
        Warranty_Expiry = %s,
        Status = %s,
        Remarks = %s
    WHERE Asset_Code = %s
    """

    values = (
        asset_name,
        asset_type,
        manufacturer,
        model,
        serial_number,
        department,
        location,
        purchase_date,
        warranty_expiry,
        status,
        remarks,
        asset_code
    )

    cursor.execute(query, values)
    connection.commit()

    affected_rows = cursor.rowcount

    cursor.close()
    connection.close()

    return affected_rows


def assign_asset(
    asset_code,
    assigned_to,
    department,
    location
):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE Assets
    SET Assigned_To = %s,
        Department = %s,
        Location = %s,
        Status = 'Assigned'
    WHERE Asset_Code = %s
    """

    cursor.execute(
        query,
        (
            assigned_to,
            department,
            location,
            asset_code
        )
    )

    connection.commit()

    affected_rows = cursor.rowcount

    cursor.close()
    connection.close()

    return affected_rows


def delete_asset(asset_code):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM Assets WHERE Asset_Code = %s",
        (asset_code,)
    )

    connection.commit()

    affected_rows = cursor.rowcount

    cursor.close()
    connection.close()

    return affected_rows


def get_asset_statistics():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM Assets"
    )
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Assets WHERE Status = 'Available'"
    )
    available = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Assets WHERE Status = 'Assigned'"
    )
    assigned = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Assets WHERE Status = 'Maintenance'"
    )
    maintenance = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return (
        total,
        available,
        assigned,
        maintenance
    )