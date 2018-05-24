
from flask_script import Manager

from utils.app import create_app
from utils.config import Config

# 创建flask对象app
app = create_app(Config)
# 使用Manger去管理falsk对象app
manage = Manager(app=app)

if __name__ == '__main__':

    manage.run()
