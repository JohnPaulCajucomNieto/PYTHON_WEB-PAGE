from app import mycursor

mycursor.execute("CREATE DATABASE IF NOT EXISTS customer")
mycursor.execute("USE customer")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customerorders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Firstname VARCHAR(255),
        Lastname VARCHAR(255),
        FullAddress VARCHAR(255),
        EmailAddress VARCHAR(255),
        PhoneNumber VARCHAR(15),
        Instrument VARCHAR(255),
        Qty INT,
        Brand VARCHAR(255)
    )
""")
