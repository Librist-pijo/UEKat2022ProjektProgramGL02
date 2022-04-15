from flask import Flask
from flask_restful import Api
from apispec import APISpec
import Controllers.GenderAgeDetectionController as GADC
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

app = Flask(__name__)  # Flask app instance initiated
api = Api(app)  # Flask restful wraps Flask app around it.
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Gender Age Detection',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

api.add_resource(GADC.GenderAgeDetectionPhotoApi, '/GenderAgeDetectionPhoto')
api.add_resource(GADC.GenderAgeDetectionVideoApi, '/GenderAgeDetectionVideo')
docs.register(GADC.GenderAgeDetectionPhotoApi)
docs.register(GADC.GenderAgeDetectionVideoApi)

if __name__ == '__main__':
    app.run(debug=True)
