from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for payroll
employees = [
    {"id": 1, "name": "John Doe", "position": "Developer", "salary": 50000},
    {"id": 2, "name": "Jane Smith", "position": "Designer", "salary": 45000},
]

@app.route("/")
def index():
    return render_template("index.html", employees=employees)

@app.route("/add", methods=["POST"])
def add_employee():
    new_employee = {
        "id": len(employees) + 1,
        "name": request.form["name"],
        "position": request.form["position"],
        "salary": int(request.form["salary"]),
    }
    employees.append(new_employee)
    return jsonify({"message": "Employee added successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
