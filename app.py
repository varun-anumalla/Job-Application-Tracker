from flask import Flask, render_template, request, redirect, url_for, Response
from database import get_connection, initialize_database
import csv
import io

app = Flask(__name__)

# Create database if it doesn't exist
initialize_database()

# Available statuses
STATUSES = [
    "Wishlist",
    "Applied",
    "Interview",
    "Offer",
    "Rejected"
]


# =========================
# Dashboard
# =========================
@app.route("/")
def home():

    search = request.args.get("q", "").strip()
    status_filter = request.args.get("status", "All")

    conn = get_connection()

    query = """
    SELECT *
    FROM applications
    WHERE 1=1
    """

    params = []

    # Search functionality
    if search:
        query += """
        AND (
            company_name LIKE ?
            OR job_role LIKE ?
            OR location LIKE ?
        )
        """

        term = f"%{search}%"

        params.extend([
            term,
            term,
            term
        ])

    # Status filter
    if status_filter != "All":
        query += """
        AND status = ?
        """

        params.append(status_filter)

    query += """
    ORDER BY id DESC
    """

    applications = conn.execute(
        query,
        params
    ).fetchall()

    # Total applications
    total = conn.execute(
        """
        SELECT COUNT(*) AS total
        FROM applications
        """
    ).fetchone()["total"]

    # Status counts
    stats = {}

    for status in STATUSES:

        stats[status] = conn.execute(
            """
            SELECT COUNT(*) AS count
            FROM applications
            WHERE status = ?
            """,
            (status,)
        ).fetchone()["count"]

    conn.close()

    return render_template(
        "index.html",
        applications=applications,
        total=total,
        stats=stats,
        statuses=STATUSES,
        search=search,
        status_filter=status_filter
    )


# =========================
# Add Application
# =========================
@app.route("/add", methods=["GET", "POST"])
def add_application():

    if request.method == "POST":

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO applications
            (
                company_name,
                job_role,
                location,
                salary,
                applied_date,
                status,
                job_url,
                notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                request.form.get("company_name", ""),
                request.form.get("job_role", ""),
                request.form.get("location", ""),
                request.form.get("salary", ""),
                request.form.get("applied_date", ""),
                request.form.get("status", "Wishlist"),
                request.form.get("job_url", ""),
                request.form.get("notes", "")
            )
        )

        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    return render_template(
        "add.html",
        statuses=STATUSES
    )


# =========================
# Edit Application
# =========================
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_application(id):

    conn = get_connection()

    if request.method == "POST":

        conn.execute(
            """
            UPDATE applications
            SET
                company_name = ?,
                job_role = ?,
                location = ?,
                salary = ?,
                applied_date = ?,
                status = ?,
                job_url = ?,
                notes = ?
            WHERE id = ?
            """,
            (
                request.form.get("company_name", ""),
                request.form.get("job_role", ""),
                request.form.get("location", ""),
                request.form.get("salary", ""),
                request.form.get("applied_date", ""),
                request.form.get("status", "Wishlist"),
                request.form.get("job_url", ""),
                request.form.get("notes", ""),
                id
            )
        )

        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    application = conn.execute(
        """
        SELECT *
        FROM applications
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    conn.close()

    return render_template(
        "edit.html",
        application=application,
        statuses=STATUSES
    )


# =========================
# Delete Application
# =========================
@app.route("/delete/<int:id>")
def delete_application(id):

    conn = get_connection()

    conn.execute(
        """
        DELETE FROM applications
        WHERE id = ?
        """,
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


# =========================
# Update Status Dropdown
# =========================
@app.route("/update_status/<int:id>", methods=["POST"])
def update_status(id):

    status = request.form.get("status")

    conn = get_connection()

    conn.execute(
        """
        UPDATE applications
        SET status = ?
        WHERE id = ?
        """,
        (
            status,
            id
        )
    )

    conn.commit()
    conn.close()

    return redirect(request.referrer or url_for("home"))


# =========================
# Export CSV
# =========================
@app.route("/export")
def export_csv():

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT *
        FROM applications
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "Company",
        "Role",
        "Location",
        "Salary",
        "Applied Date",
        "Status",
        "Job URL",
        "Notes"
    ])

    for row in rows:

        writer.writerow([
            row["company_name"],
            row["job_role"],
            row["location"],
            row["salary"],
            row["applied_date"],
            row["status"],
            row["job_url"],
            row["notes"]
        ])

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=applications.csv"
        }
    )


# =========================
# Run App
# =========================
if __name__ == "__main__":
    app.run(debug=True)