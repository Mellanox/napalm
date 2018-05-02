import re

class MissingData(Exception):

    def __init__(self, request):
        self.request = request
        self.request_id = re.sub(r'[\[\]\*\^\+\s\|]', '_', request)

    def __str__(self):
        return self.request
