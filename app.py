from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# DATABASE CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library_management"
)

cursor = db.cursor(dictionary=True)

# ---------------- HOME ----------------
@app.route("/")
def index():
    return render_template("index.html")

# ---------------- BOOKS ----------------
@app.route("/books")
def books():
    cursor.execute("SELECT * FROM Book")
    books = cursor.fetchall()
    return render_template("books.html", books=books)

@app.route("/add_book", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    date = request.form["published_date"]

    cursor.execute(
        "INSERT INTO Book(title, author, published_date) VALUES(%s,%s,%s)",
        (title, author, date),
    )
    db.commit()
    return redirect("/books")


# ---------------- MEMBERS ----------------
@app.route("/members")
def members():
    cursor.execute("SELECT * FROM Member")
    members = cursor.fetchall()
    return render_template("members.html", members=members)

@app.route("/add_member", methods=["POST"])
def add_member():
    first = request.form["first_name"]
    last = request.form["last_name"]
    email = request.form["email"]

    cursor.execute(
        "INSERT INTO Member(first_name,last_name,email) VALUES(%s,%s,%s)",
        (first, last, email),
    )
    db.commit()
    return redirect("/members")


# ---------------- LOANS (READ) ----------------
@app.route("/loans")
def loans():
    cursor.execute("""
        SELECT L.loan_id,
               B.title,
               CONCAT(M.first_name,' ',M.last_name) AS member,
               L.issue_date,
               L.due_date,
               L.return_date,
               L.status
        FROM Loan L
        JOIN Book B ON L.book_id=B.book_id
        JOIN Member M ON L.member_id=M.member_id
    """)
    loans = cursor.fetchall()
    return render_template("loans.html", loans=loans)


# ---------------- ISSUE BOOK (CREATE) ----------------
@app.route("/issue", methods=["GET","POST"])
def issue():
    if request.method == "POST":
        book_id = request.form["book_id"]
        member_id = request.form["member_id"]

        cursor.execute("""
            INSERT INTO Loan(book_id,member_id,issue_date,due_date,status)
            VALUES(%s,%s,CURDATE(),
            DATE_ADD(CURDATE(),INTERVAL 14 DAY),'Issued')
        """,(book_id,member_id))

        db.commit()
        return redirect("/loans")

    cursor.execute("SELECT * FROM Book")
    books = cursor.fetchall()

    cursor.execute("SELECT * FROM Member")
    members = cursor.fetchall()

    return render_template("issue.html",books=books,members=members)


# ---------------- RETURN BOOK (UPDATE) ----------------
@app.route("/return/<int:id>")
def return_book(id):
    cursor.execute("""
        UPDATE Loan
        SET return_date = CURDATE(),
            status='Returned'
        WHERE loan_id=%s
    """,(id,))
    db.commit()
    return redirect("/loans")


# ---------------- DELETE LOAN ----------------
@app.route("/delete/<int:id>")
def delete_loan(id):
    cursor.execute("DELETE FROM Loan WHERE loan_id=%s",(id,))
    db.commit()
    return redirect("/loans")


if __name__ == "__main__":
    app.run(debug=True)