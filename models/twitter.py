from mongoengine import *
import marshmallow_mongoengine as ma


class EntitiesModel(EmbeddedDocument):
    hashtags                     = ListField(StringField(required=False))
    symbols                      = ListField(StringField(required=False))
    user_mentions                = ListField(StringField(required=False))
    urls                         = DictField()

class TwitterModel(Document):
    created_at                      = StringField(required=False)
    full_text                       = StringField(required=False)
    place                           = StringField(required=False)
    username                        = StringField(required=False)
    user_followers                  = IntField(required=False)
    user_id_str                     = StringField(required=False)
    user_location                   = StringField(required=False)
    description                     = StringField(required=False)


class TwitterSchema(ma.ModelSchema):
    class Meta:
        model = TwitterModel