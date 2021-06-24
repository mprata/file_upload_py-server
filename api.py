from flask import Flask
from flask_restx import Resource, Api, reqparse
from flask_cors import CORS
import werkzeug

app = Flask(__name__)
CORS(app, resources={r"/upload_image/*":{
  "origins": "*",
  "allow_headers": "*"
}})
api = Api(app)

@api.route('/hello')
class Hello(Resource):
   def get(self):
     return "hello"

@api.route('/upload_image')
class UploadImage(Resource):
   def post(self):
     parse = reqparse.RequestParser()
     parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
     args = parse.parse_args()
     image_file = args['file']
     image_file.save("uploaded_file.jpg")

if __name__ == '__main__':
    app.run(debug=True)