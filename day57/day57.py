from flask import Flask, render_template
import random, datetime, requests

app = Flask(__name__)

@app.route("/")
def main_page():
    random_number = random.randint(0,9)
    return render_template("index.html", num=random_number, this_year=datetime.datetime.today().year)

# This api route is not run in BH laptop as it is stopped by firewall
@app.route("/name/<user_name>")
def api_prediction(user_name):
    age_params = {"name": user_name}
    age_response = requests.get("https://api.agify.io", params=age_params, verify=False)

    gender_params = {"name": user_name}
    gender_response = requests.get("https://api.genderize.io", params=gender_params, verify=False)

    return render_template("api_prediction.html", person_name=user_name, age=age_response.json(), gender=gender_response.json())

@app.route("/python_operation/<num>")
def py_operation(num):
    return render_template("py_operation.html", my_number=int(num))

if __name__ == "__main__":
    app.run(debug=True)