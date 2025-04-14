from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        return render_template("contact.html", submitted=True, name=name, message=message)
    return render_template("contact.html")

@app.route('/interests', methods=["GET", "POST"])
def interests():
    interests = None
    if request.method == "POST":
        interests = request.form["interests"]
    return render_template("interests.html", interests=interests)

if __name__ == '__main__':
    app.run(debug=True)
