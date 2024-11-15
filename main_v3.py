from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)

    #The repr() function returns a printable representation of the given object.
    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes ={self.likes})"

db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name" , type = str, help = "Name of the video is required", required = True)
video_put_args.add_argument("views", type = int, help = "Views of the video is required", required = True)
video_put_args.add_argument("likes", type = int, help = "Likes on the video is required", required = True)

videos = {}
# 201 : Created
# 409 : Already exists
# 204 : Work delete
def abort_if_not_id(video_id):
    if video_id not in videos:
        abort(404, message = "Video id is not valid...")

def abort_if_exists(video_id):
    if video_id in videos:
        abort(409, message = "Video already exists with that ID...")
class Video(Resource):

    def get(self, video_id):
        abort_if_not_id(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        abort_if_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_not_id(video_id)
        del videos[video_id]
        return '', 204

api.add_resource(Video, "/video/<int:video_id>")# endpoint



if __name__ == "__main__":
    app.run(debug = True) #Not in production
