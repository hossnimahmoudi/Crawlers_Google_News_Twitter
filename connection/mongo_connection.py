from mongoengine import connect


class mongoConnection:
    def __init__(self, config):
        self.config = config

    def __enter__(self):
        self.connection = connect(db='collectionName', host='mongodb://system:@:22018/?authSource=')

        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
