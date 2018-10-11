from collections import defaultdict
import json


class RestAPI(object):
    def __init__(self, database=None):
        """Our constructor class to create API objects."""

        self.database = database
        self.balance = {}

    def get(self, url, payload=None):
        """The GET method of our API"""
        if url == '/users':
            return self.database

    def post(self, url, payload=None):
        """The POST method of our API"""

        payload = json.loads(payload)

        if url == '/add':
            response = self.post_add(**payload)
        if url == '/iou':
            response = self.post_iou(**payload)

        return json.dumps(response)
