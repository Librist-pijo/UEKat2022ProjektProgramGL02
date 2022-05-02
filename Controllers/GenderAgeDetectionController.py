import os
from flask import jsonify, request
import Schemas.ApiSchema as schema
from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from werkzeug.utils import secure_filename
#  Restful way of creating APIs through Flask Restful

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class GenderAgeDetectionPhotoApi(MethodResource, Resource):
    @doc(description='Photo GET Endpoint', tags=['Photo'])
    @marshal_with(schema.ResponseSchema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        return {'message': 'Test GET'}

    @doc(description='Photo POST Endpoint', tags=['Photo'])
    @use_kwargs(schema.FileUploadSchema, location=('files'))
    @marshal_with(schema.ResponseSchema)  # marshalling
    def post(self, **kwargs):
        '''
        POST method represents a POST API method
        '''
        # check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message' : 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message' : 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resp = jsonify({'message' : 'File successfully uploaded'})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
            resp.status_code = 400
            return resp
        return {'message': 'Test POST'}

# TODO - Additional controller for video
# class GenderAgeDetectionVideoApi(MethodResource, Resource):
#     @doc(description='Video GET Endpoint', tags=['Video'])
#     @marshal_with(schema.ResponseSchema)  # marshalling
#     def get(self):
#         '''
#         Get method represents a GET API method
#         '''
#         return {'message': 'Test GET'}

#     @doc(description='Video POST Endpoint', tags=['Video'])
#     @use_kwargs(schema.RequestSchema, location=('json'))
#     @marshal_with(schema.ResponseSchema)  # marshalling
#     def post(self, **kwargs):
#         '''
#         POST method represents a POST API method
#         '''
#         return {'message': 'Test POST'}
