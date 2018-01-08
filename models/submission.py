import os
from utils.fs import remove_ext

class Submission:
    def __init__(self, path):
        self.path = path
        self.filename = remove_ext(os.path.basename(path))
        self.comments = ""

    def append_comment(self, content):
        self.comments += content
