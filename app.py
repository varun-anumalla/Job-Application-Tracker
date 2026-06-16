from flask import Flask, render_template, request, redirect, url_for
from database import get_connection, initialize_database

app = Flask(__name__)

initialize_database()


@app.route("/")
def home():

    conn = get_connection()

    applications = conn.execute("""
    SELECT *
    FROM applications
    ORDER BY id DESC
    """).fetchall()

    total = conn.execute("""
    SELECT COUNT(*) as total
    FROM applications
    """).fetchone()["total"]

    conn.close()

    return render_template(
        "index.html",
        applications=applications,
        total=total
    )


@app.route("/add", methods=["GET", "POST"])
def add_application():

    if request.method == "POST":

        company = request.form["company_name"]
        role = request.form["job_role"]
        location = request.form["location"]
        salary = request.form["salary"]
        date = request.form["applied_date"]
        status = request.form["status"]
        notes = request.form["notes"]

        conn = get_connection()

        conn.execute("""
        INSERT INTO applications
        (
            company_name,
            job_role,
            location,
            salary,
            applied_date,
            status,
            notes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            company,
            role,
            location,
            salary,
            date,
            status,
            notes
        ))

        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/delete/<int:id>")
def delete_application(id):

    conn = get_connection()

    conn.execute(
        "DELETE FROM applications WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_application(id):

    conn = get_connection()

    if request.method == "POST":

        status = request.form["status"]
        notes = request.form["notes"]

        conn.execute("""
        UPDATE applications
        SET status=?, notes=?
        WHERE id=?
        """,
        (status, notes, id))

        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    application = conn.execute(
        "SELECT * FROM applications WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template(
        "edit.html",
        application=application
    )


if __name__ == "__main__":
    app.run(debug=True)