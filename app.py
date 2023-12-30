from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

@app.route("/")

def hello_jovian():
    return render_template("home.html",
                            company_name='Los Niños Flash Transportation')
@app.route("/contact")
def form():
    return render_template("contact_us.html")
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


  