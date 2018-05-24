
from flask import Flask
from utils.settings import template_dir, static_dir
from utils.funtions import init_ext

from App.user_views import user_blueprint
from App.house_views import house_blueprint
from App.order_views import order_blueprint

# 定义函数，创建flask对象app
def create_app(Config):
    app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
    app.register_blueprint(blueprint=house_blueprint, url_prefix='/house')
    app.register_blueprint(blueprint=order_blueprint, url_prefix='/order')

    app.config.from_object(Config)
    # 初始化对象
    init_ext(app)

    return app
