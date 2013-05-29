import os

class Config(object):
    DEBUG = True
    TESTING = False
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
    FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
    FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET')
    FACEBOOK_SCOPE = ['user_likes', 'user_photos', 'user_photo_video_tags']
