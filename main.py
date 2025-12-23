from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "password"

MAX_ATTEMPTS = 5
BLOCK_TIME = 30  # seconds

failed_attempts = {}
blocked_until = {}


@app.route("/", methods=["GET", "POST"])
def login():
    ip = request.remote_addr
    now = time.time()

    if ip in blocked_until and now < blocked_until[ip]:
        return "Too many attempts. Try later.", 429

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            failed_attempts.pop(ip, None)
            blocked_until.pop(ip, None)
            return redirect(url_for("welcome"))

        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

        if failed_attempts[ip] >= MAX_ATTEMPTS:
            blocked_until[ip] = now + BLOCK_TIME
            failed_attempts[ip] = 0
            return "IP blocked for 30 seconds", 429

        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@app.route("/welcome")
def welcome():
    return "Welcome!"


if __name__ == "__main__":
    app.run(debug=True)
