from flask import Flask
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
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



video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name" , type = str, help = "Name of the video is required", required = True)
video_put_args.add_argument("views", type = int, help = "Views of the video is required", required = True)
video_put_args.add_argument("likes", type = int, help = "Likes on the video is required", required = True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name" , type = str, help = "Name of the video is required")
video_update_args.add_argument("views", type = int, help = "Views of the video is required")
video_update_args.add_argument("likes", type = int, help = "Likes on the video is required")


resource_fields = {#Serialize a instance with this fields
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class Video(Resource):
    @marshal_with(resource_fields)#resource_fields
    def get(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, "Could not find video with that id")
        return result
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()

        if result:
            abort(409, message = "Video id taken...")

        video = VideoModel(id=video_id, name = args['name'], views = args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):#UPDATE
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message = "Video doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
         
        db.session.commit()

        return result, 200
    
    @marshal_with(resource_fields)
    def delete(self, video_id):
        # Buscar el video por ID
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video with that ID does not exist, cannot delete.")
        
        db.session.delete(result)
        db.session.commit()

api.add_resource(Video, "/video/<int:video_id>")# endpoint



if __name__ == "__main__":
    app.run(debug = True) #Not in production
