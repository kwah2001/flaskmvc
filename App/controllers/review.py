from App.models import Review
from App.models import User
from App.models import Student
from App.database import db

#add review to a specific student
def add_review(student_id, user_id, review_text):
    student = Student.query.get(student_id)
    user = User.query.get(user_id)

    if not student:
        return {"message": "Student not found."}
    if not user:
        return {"message": "User not found."}

    new_review = Review(student_id=student_id, user_id=user_id, review_text=review_text)
    db.session.add(new_review)
    db.session.commit()
    return {"message": f"Review added successfully"}
    

#view reviews for a particular student
def view_student_reviews(student_id):
    student = Student.query.get(student_id)
    if not student:
        return {"message": "Student not found."}

    reviews = Review.query.filter_by(student_id=student_id).all()
    if not reviews:
        return {"message": "No reviews found for this student."}

    review_list = [review.get_json() for review in reviews]
    return {"reviews": review_list}
    
  


