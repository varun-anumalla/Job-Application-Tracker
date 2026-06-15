from database import connect_db


class ApplicationTracker:

    def __init__(self):
        self.conn, self.cursor = connect_db()

    def add_application(self):

        company = input("Company Name: ")
        role = input("Job Role: ")
        location = input("Location: ")
        salary = input("Salary: ")
        date = input("Applied Date: ")
        status = input("Status: ")
        notes = input("Notes: ")

        self.cursor.execute("""
        INSERT INTO applications
        (company_name, job_role, location,
        salary, applied_date, status, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (company, role, location,
         salary, date, status, notes))

        self.conn.commit()

        print("\nApplication Added Successfully")

    def view_applications(self):

        self.cursor.execute("SELECT * FROM applications")

        rows = self.cursor.fetchall()

        if not rows:
            print("\nNo Applications Found")
            return

        print("\n" + "=" * 60)

        for row in rows:

            print(f"""
ID           : {row[0]}
Company      : {row[1]}
Role         : {row[2]}
Location     : {row[3]}
Salary       : {row[4]}
Applied Date : {row[5]}
Status       : {row[6]}
Notes        : {row[7]}
            """)

            print("-" * 60)

    def search_application(self):

        company = input("Enter Company Name: ")

        self.cursor.execute(
            "SELECT * FROM applications WHERE company_name LIKE ?",
            ('%' + company + '%',)
        )

        rows = self.cursor.fetchall()

        if not rows:
            print("\nNo Matching Records Found")
            return

        for row in rows:

            print(f"""
ID           : {row[0]}
Company      : {row[1]}
Role         : {row[2]}
Location     : {row[3]}
Salary       : {row[4]}
Applied Date : {row[5]}
Status       : {row[6]}
Notes        : {row[7]}
            """)

    def update_status(self):

        app_id = input("Enter Application ID: ")
        new_status = input("New Status: ")

        self.cursor.execute("""
        UPDATE applications
        SET status = ?
        WHERE id = ?
        """, (new_status, app_id))

        self.conn.commit()

        print("\nStatus Updated Successfully")

    def delete_application(self):

        app_id = input("Enter Application ID: ")

        self.cursor.execute(
            "DELETE FROM applications WHERE id = ?",
            (app_id,)
        )

        self.conn.commit()

        print("\nApplication Deleted Successfully")

    def total_applications(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM applications"
        )

        total = self.cursor.fetchone()[0]

        print(f"\nTotal Applications: {total}")