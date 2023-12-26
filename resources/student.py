from flask import  request, make_response
from flask_smorest import  Blueprint,abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
import json
from models.student import StudentsModel , db

student_B= Blueprint("student", __name__ ,description="student Operations")

@student_B.route('/students')
class STUDENT(MethodView):
    def get(self):
        students = StudentsModel.query.all()
        results = [
            {
                "student_id":student.student_id,
                "name": student.name,
                "membership_start": student.membership_start,
                "email": student.email,
                
            } for student in students]

        return {"count": len(results), "students": results, "message": "success"}

    def post(self):
        if request.is_json:
            try:
                 data = json.loads(request.data, strict=False)
            except SQLAlchemyError:
                 return make_response({"error": "There are issue with the json content","code":415},415)
            try:
                 new_student = StudentsModel( name=data['name'], membership_start=data['membership_start'], email=data['email'])
            except SQLAlchemyError:
                 return make_response({"error": "There are issue with the json content, check the keys","code":422},422)
            try:
                db.session.add(new_student)    ### should check the the content to make sure keys and values are valid.
                db.session.commit()
            except SQLAlchemyError:
                return abort(make_response({'message':f'An Error Occured While Inserting The Book '},500))

            return make_response({"message": f"Student {new_student.name} has been added successfully."},201)
        else:
            return make_response({"error": "The request payload is not in JSON format"},415)
        
