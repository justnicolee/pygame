
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calculate", methods=["GET", "POST"])
def calculate():

    result = None

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2

    return render_template('base.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)