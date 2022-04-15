import Schemas.ApiSchema as schema
from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
#  Restful way of creating APIs through Flask Restful


class GenderAgeDetectionPhotoApi(MethodResource, Resource):
    @doc(description='Photo GET Endpoint', tags=['Photo'])
    @marshal_with(schema.ResponseSchema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        return {'message': 'Test GET'}

    @doc(description='Photo POST Endpoint', tags=['Photo'])
    @use_kwargs(schema.RequestSchema, location=('json'))
    @marshal_with(schema.ResponseSchema)  # marshalling
    def post(self, **kwargs):
        '''
        POST method represents a POST API method
        '''
        return {'message': 'Test POST'}


class GenderAgeDetectionVideoApi(MethodResource, Resource):
    @doc(description='Video GET Endpoint', tags=['Video'])
    @marshal_with(schema.ResponseSchema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        return {'message': 'Test GET'}

    @doc(description='Video POST Endpoint', tags=['Video'])
    @use_kwargs(schema.RequestSchema, location=('json'))
    @marshal_with(schema.ResponseSchema)  # marshalling
    def post(self, **kwargs):
        '''
        POST method represents a POST API method
        '''
        return {'message': 'Test POST'}
