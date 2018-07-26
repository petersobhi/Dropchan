# DropChan
An anonymous board created by Django and Dropbox without any use of databases.

### External Documentation:

* [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)
* [Dropbox API](http://dropbox-sdk-python.readthedocs.io/en/latest/)

### Requirements to run locally:

* Linux-based system
* [Python 3.6](https://www.python.org/)

### Installation:
##### System Dependencies:
1. Install pip and vitualenv:  
`sudo apt-get install -y virtualenv`  
`sudo apt-get install -y python3-pip`
2. Create a virtual environment:  
`virtualenv -p python3 ~/.virtualenvs/dropchan`
3. Activate `dropchan` virtual environment:  
`source ~/.virtualenvs/dropchan/bin/activate`
4. Install requirements in the virtual environment:  
`pip3 install -r requirements.txt`

### Dropbox structure:
The system contains of 2 main models: `Thread` and `Comment`.
Thread JSON model:

```
{id}: {
    "title": {title},
    "description": {description},
    "timestamp": {timestamp}
}
```
* The threads info saved as a JSON file in: `/threads.json`.
* If a thread has a cover image, it is saved on: `/threads/{thread_id}/cover.png`

Comment JSON model:

```
{id}: {
    "body": {body},
    "timestamp": {timestamp}
}
```
* The threads info saved as a JSON file in: `/threads/{thread_id}/comments.json`.
* If a thread has a cover image, it is saved on: `/threads/{thread_id}/images/{comment_id}.png`

### Configuration
Available settings:
**DROPBOX_TOKEN**
Dropbox App token that will be used.
You will need to register a new app in the [Dropbox App Console](https://www.dropbox.com/developers/apps) to get a token.

**THREADS_JSON_PATH (='/threads.json')**
Specifies the JSON file path that store the threads information.

**THREAD_IMAGE_PATH (='/threads/{thread_id}/cover.png')**
Specifies the path of the thread cover images.
`{thread_id}` replacement string must be a part of the provided string.

**COMMENTS_JSON_PATH (='/threads/{thread_id}/comments.json')**
Specifies the JSON file path that store the comments information.
`{thread_id}` replacement string must be a part of the provided string.

**COMMENT_IMAGE_PATH (='/threads/{thread_id}/images/{comment_id}.png')**
Specifies the path of the comment cover images.
`{thread_id}` and `{comment_id}` replacement strings must be a part of the provided string.

### Authors
* [Peter Bassem Sobhi](https://github.com/petersobhi)

