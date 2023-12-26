from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

JOBS = [
    {'id': 1,
     'title': 'Data Analyst',
     'location': 'Delhi, India',
     'salary': 'Rs. 10,000,000'},
    {'id': 1,
     'title': 'Data Analyst',
     'location': 'Delhi, India',
     'salary': 'Rs. 10,000,000'},
    {'id': 1,
     'title': 'Data Analyst',
     'location': 'Delhi, India',
     'salary': 'Rs. 10,000,000'},
         {'id': 1,
     'title': 'Cyber Security',
     'location': 'Remote'}
]

@app.route("/")

def hello_jovian():
    return render_template("home.html",
                            jobs = JOBS,
                            company_name='Jovian')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


