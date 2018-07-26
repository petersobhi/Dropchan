import io
import json
from PIL import Image
from collections import OrderedDict
import dropbox

from django.utils.crypto import get_random_string
from django.conf import settings

dbx = dropbox.Dropbox(settings.DROPBOX_TOKEN)


def generate_unique_id():
    """
    Return an 8-digit ID
    In production UUID should be used instead.
    """
    return get_random_string(length=8, allowed_chars='0123456789')


def read_json_file_as_dict(path):
    """Take a path that contains json file and return an OrderedDict object"""
    try:
        metadata, threads_file = dbx.files_download(path)
        all_objects = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(threads_file.content.decode())
    except dropbox.exceptions.ApiError:
        all_objects = OrderedDict()
    return all_objects


def append_dict_to_json_file(id, dict, path):
    """
    Try to open the a json file and append the a new json object to it.
    Creates a new one if its the first object to be added.
    """
    all_objects = read_json_file_as_dict(path)
    all_objects[id] = dict
    threads_file = io.BytesIO(json.dumps(all_objects).encode())
    dbx.files_upload(threads_file.getvalue(), path, mode=dropbox.files.WriteMode('overwrite'))


def upload_image(image, path):
    """Reformat an image and convert it to PNG then upload it to a Dropbox path."""
    resized_image = Image.open(image)
    resized_image.thumbnail(size=(360, 360))

    image_bytes = io.BytesIO()
    resized_image.save(image_bytes, format('PNG'))
    dbx.files_upload(image_bytes.getvalue(), path)


def get_image_url(path):
    """Return a shareable image url from Dropbox that is valid for 4 hours."""
    try:
        image_link = dbx.files_get_temporary_link(path)
        url = image_link.link
    except dropbox.exceptions.ApiError:
        url = None
    return url
