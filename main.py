from flask import Flask, render_template, request, redirect, url_for
import time
import logging 

app = Flask(__name__)

#Initials for demo
USERNAME = "admin"
PASSWORD = "password"

MAX_ATTEMPTS = 5 #Attempts before ban 
BLOCK_TIME = 30  # seconds

#Data
failed_attempts = {}
blocked_until = {}

#Logging info and storing
logging.basicConfig(filename="info.log",format='%(asctime)s %(message)s',filemode='a')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


@app.route("/", methods=["GET", "POST"])
def login():
    ip = request.remote_addr
    now = time.time()

    if ip in blocked_until and now < blocked_until[ip]:
        return "Too many attempts. Try later.", 429

    #Giving info of initials
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        #Comparing if username and password same
        if username == USERNAME and password == PASSWORD:
            failed_attempts.pop(ip, None) #If initials are right, attempts set to 0
            blocked_until.pop(ip, None)
            logger.info(f"Successful login for user: {username} from IP {ip}") #Logging
            return redirect(url_for("welcome"))

        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1 #If initials are wrong,attempts+1
        logger.warning(f"Failed login attempt for user: {username} from IP {ip}")#Logging
        if failed_attempts[ip] >= MAX_ATTEMPTS:
            blocked_until[ip] = now + BLOCK_TIME #Blocking for 30 sec
            failed_attempts[ip] = 0
            logger.warning(f"IP blocked due to brute-force: {ip}")#Logging
            return "IP blocked for 30 seconds", 429

        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@app.route("/welcome")
def welcome():
    return "Welcome!"


if __name__ == "__main__":
    app.run(debug=True)
