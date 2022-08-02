from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
    'Id': 1,
    'Title': 'Data Analyst',
    'Location': 'Garden Grove, CA',
    'Salary': '$50,000'
}, {
    'Id': 2,
    'Title': 'Data Scientist',
    'Location': 'Irvine, CA',
    'Salary': '$70,000'
}, {
    'Id': 3,
    'Title': 'Chemical Engineer',
    'Location': 'Bakerfield, CA',
    'Salary': '$90,000'
}, {
    'Id': 4,
    'Title': 'Electric Engineer',
    'Location': 'Los Angeles, CA',
    'Salary': '$80,000'
}, {
    'Id': 5,
    'Title': 'Mechanic Engineer',
    'Location': 'Westminster, CA',
}]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
