from flask import Flask, request, render_template
import re


app = Flask(__name__)

####################################################
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string')
    regex = request.form.get('regex')
    matches = re.findall(regex, test_string)
    return render_template('index.html', matches=matches, test_string=test_string, regex=regex)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form.get('email')
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid = bool(re.match(regex, email))
    return render_template('index.html', email=email, is_valid=is_valid)













####################################################
if __name__ == "__main__":
    app.run(debug= True)