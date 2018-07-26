from time import gmtime, strftime

from django.conf import settings

from .dropbox_helper import (generate_unique_id, append_dict_to_json_file,
                             upload_image, read_json_file_as_dict, get_image_url)


class Thread(object):

    @classmethod
    def get_all(cls):
        """Return all threads from Dropbox."""
        threads = []
        threads_dict = read_json_file_as_dict(settings.THREADS_JSON_PATH)

        # Reverse the objects to get the newer first
        for id, thread_dict in reversed(list(threads_dict.items())):
            image_path = get_image_url(settings.THREAD_IMAGE_PATH.format(thread_id=id))
            thread = Thread(id=id, image_path=image_path, **thread_dict)
            threads.append(thread)

        return threads

    @classmethod
    def get_object(cls, id):
        """Return a thread of a given ID."""
        threads_dict = read_json_file_as_dict(settings.THREADS_JSON_PATH)
        thread_dict = threads_dict.get(str(id), None)

        if not thread_dict:
            return None

        image_path = get_image_url(settings.THREAD_IMAGE_PATH.format(thread_id=id))
        return Thread(id=id, image_path=image_path, **thread_dict)

    def __init__(self, title, description, id=None, image=None, image_path=None, timestamp=None):
        self.title = title
        self.description = description
        self.id = id
        self.image = image
        self.image_path = image_path
        self.timestamp = timestamp

    def save(self):
        """Save current thread to Dropbox."""
        self.id = generate_unique_id()
        self.timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        thread_dict = {
            "title": self.title,
            "description": self.description,
            "timestamp": self.timestamp
        }

        append_dict_to_json_file(self.id, thread_dict, settings.THREADS_JSON_PATH)
        if self.image:
            upload_image(self.image, settings.THREAD_IMAGE_PATH.format(thread_id=self.id))


class Comment(object):

    @classmethod
    def get_all(cls, thread_id):
        """Return all comments of a thread from Dropbox."""
        comments = []
        comments_dict = read_json_file_as_dict(settings.COMMENTS_JSON_PATH.format(thread_id=thread_id))

        for id, comment_dict in comments_dict.items():
            image_path = get_image_url(settings.COMMENT_IMAGE_PATH.format(thread_id=thread_id, comment_id=id))
            comment = Comment(id=id, image_path=image_path, **comment_dict)
            comments.append(comment)

        return comments

    def __init__(self, body, id=None, image=None, image_path=None, timestamp=None):
        self.body = body
        self.id = id
        self.image = image
        self.image_path = image_path
        self.timestamp = timestamp

    def save(self, thread_id):
        """Save current comment to Dropbox."""
        self.id = generate_unique_id()
        self.timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        comment_dict = {
            'body': self.body,
            'timestamp': self.timestamp
        }

        append_dict_to_json_file(self.id, comment_dict, settings.COMMENTS_JSON_PATH.format(thread_id=thread_id))
        if self.image:
            upload_image(self.image, settings.COMMENT_IMAGE_PATH.format(thread_id=thread_id, comment_id=self.id))
