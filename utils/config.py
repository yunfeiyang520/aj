
import redis
import os

from utils.settings import DATABASE, BASE_DIR
from utils.funtions import get_db_uri


class Config():

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'secret_key'

    SESSION_TYPE = 'redis'

    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')

    SESSION_KEY_PREFIX = 'aj_'

    # 上传图片地址
    UPLOAD_FOLDER = os.path.join(os.path.join(BASE_DIR, 'static'), 'upload')

