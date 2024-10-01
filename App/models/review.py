from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user = db.relationship('User', backref='reviews')

    def __init__(self, student_id, user_id, review_text, rating):
        self.student_id = student_id
        self.user_id = user_id
        self.review_text = review_text
        self.rating = rating

    def get_json(self):
        user_username = self.user.username
        return {
            'review_text': self.review_text,
            'rating': self.rating,
            'user_username': user_username
        }
		