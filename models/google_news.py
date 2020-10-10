from  mongoengine import *
import marshmallow_mongoengine as ma


class GoogleNewsBrut(Document):
     """Class for defining structure of google news brut collection."""

     id                       = StringField(primary_key=True, autoincrement=True)
     content                  = StringField(required=False)
     created_at               = DateTimeField()

class OgModel(EmbeddedDocument):
    title                     = StringField(required=False)
    url                       = StringField(required=False)
    description               = StringField(required=False)
    site_name                 = StringField(required=False)
    image                     = StringField(required=False)
    type                      = StringField(required=False)
    pubdate                   = StringField(required=False)
    fb_appid                  = IntField(required=False)
    locale                    = StringField(required=False)

class FbModel(EmbeddedDocument):
    pages                     = IntField(required=False)
    app_id                    = StringField(required=False)

class TwitterModel(EmbeddedDocument):
    title                     = StringField(required=False)
    description               = StringField(required=False)
    card                      = StringField(required=False)
    site                      = StringField(required=False)
    creator                   = StringField(required=False)
    image                     = StringField(required=False)
    url                       = StringField(required=False)
    text                      = StringField(required=False)

class AdditionalDataModel(EmbeddedDocument):
     content = StringField(required=False)

class HeadlineModel(EmbeddedDocument):
    title                     = StringField(required=False)
    abstract                  = StringField(required=False)
    authors                   = ListField(StringField(required=False))
    publishdate              = ListField(StringField(required=False))

class GoogleNews(Document):

     """Class for defining structure of google news collection."""

     headline                 = DictField()
     article                  = StringField(required=False)
     subjects                 = ListField(StringField(required=False))
     source                   = StringField(required=False)
     url                      = StringField(required=False)
     type                     = StringField(required=False)
     meta                     = {'strict': False}


class GoogleNewsSchema(ma.ModelSchema):
    class Meta:
        model = GoogleNews

