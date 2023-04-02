POSTS_AMAUNT = 100
COMMENTS_AMAUNT = 500
ALBUMS_AMAUNT = 100
PHOTOS_AMAUNT = 5000
TODOS_AMAUNT = 200
USERS_AMAUNT = 10

RESOURCES_LIST = {
    "posts": "posts/",
    "comments": "comments/",
    "albums": "albums/",
    "photos": "photos/",
    "todos": "todos/",
    "users": "users/"
}

schema_posts = {
    'type': 'array',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'}
    }
}
schema_comments = {
    'type': 'array',
    'properties': {
        'postId': {'type': 'number'},
        'id': {'type': 'number'},
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'body': {'type': 'string'}
    }
}
schema_albums = {
    'type': 'array',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'}
    }
}
schema_photos = {
    'type': 'array',
    'properties': {
        'albumId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'url': {'type': 'string'},
        'thumbnailUrl': {'type': 'string'}
    }
}
schema_todos = {
    'type': 'array',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'completed': {'type': 'boolean'}
    }
}
schema_users = {
    'type': 'array',
    'properties': {
        'id': {'type': 'number'},
        'name': {'type': 'string'},
        'username': {'type': 'string'},
        'email': {'type': 'string'},
        'address': {
            'type': 'array',
            'properties': {
                'street': {'type': 'string'},
                'suite': {'type': 'string'},
                'city': {'type': 'string'},
                'zipcode': {'type': 'string'},
            }
        }
    }
}
