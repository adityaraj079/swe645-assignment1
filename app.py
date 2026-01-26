from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        # Access form data if needed
        # data = request.form.to_dict()
        return render_template("survey.html", success=True)
    return render_template("survey.html", success=False)

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    
    app.run(debug=True)
