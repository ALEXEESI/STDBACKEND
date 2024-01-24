from flask import request,Flask,jsonify

app = Flask(__name__) 


student=[
    {"id":6530300660,"name":"Apiwit Nares","major":"T12","GPA":"2.93"},
    {"id":6530300259,"name":"Somchai jaidee","major":"T12","GPA":"3.3"},
    {"id":6530300257,"name":"Sommai jaidee","major":"T22","GPA":"1.5"},
    {"id":6530300662,"name":"Twipa Nares","major":"T16","GPA":"3.8"}
    
]
@app.route("/")
def Greet():
    return "<p>Welcome to Student Management Systems</p>"

@app.route("/student",methods=["GET"])
def get_all_student():
    return jsonify({"Student":student})

@app.route("/student/<int:student_id>",methods=["GET"])
def get_student(student_id):
    std =  next(( b for b in student if b["id"]==student_id),None)
    if std:
        return jsonify(std)
    else:
        return jsonify({"error":"Student Not Found"}),404

@app.route("/student",methods=["POST"])
def create_student():
    data = request.get_json()
    new_student={
        "id":data["id"],
        "name":data["name"],
        "major":data["major"],
        "gpa":data["gpa"]
    }
    if any(student["id"] == new_student["id"] for student in student):
          return jsonify({"error": "Cannot Create New Student"}),500
    else:
          student.append(new_student)
          return jsonify(new_student),200

@app.route("/student/<int:student_id>",methods=["PUT"])
def update_student(student_id):
    std = next((b for b in student if b["id"]==student_id),None)
    if std:
        data = request.get_json()
        std.update(data)
        return jsonify(std)
    else:
        return jsonify({"error":"Student Not Found"}),404

@app.route("/student/<int:student_id>",methods=["DELETE"])
def delete_student(student_id):
    std = next((b for b in student if b["id"]==student_id),None)
    if std:
        student.remove(std)
        return jsonify({"message":"Student Deleted Successfully"}),200
    else:
        return jsonify({"error":"Student Not Found"}),404
    


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)