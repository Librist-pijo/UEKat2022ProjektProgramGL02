from marshmallow import Schema, fields
# import datetime as dt
# from dataclasses import dataclass

# @dataclass
# class Album:
#             title: str
#             release_date: dt.date

# class AlbumSchema(Schema):
#             title = fields.Str(); release_date = fields.Date()

# album = Album("Beggars Banquet", dt.date(1968, 12, 6))
# schema = AlbumSchema()
# data = schema.dump(album)
# data # {'release_date': '1968-12-06', 'title': 'Beggars Banquet'}


class ResponseSchema(Schema):
    message = fields.Str(default='Success')


class RequestSchema(Schema):
    api_type = fields.String(required=True, description="Post API")
