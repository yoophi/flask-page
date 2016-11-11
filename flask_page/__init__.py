from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from werkzeug.routing import BaseConverter
from werkzeug.utils import secure_filename

__version__ = '0.0.1'

page_bp = Blueprint('pages', __name__, template_folder='templates')


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


@page_bp.route('/', defaults={'page': 'index'})
@page_bp.route('/<regex("[a-zA-Z0-9_./-]+"):page>')
def show(page):
    page = secure_filename(page)

    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)


def init_app(app, **kwargs):
    kwargs.setdefault('url_prefix', '/pages')

    app.url_map.converters['regex'] = RegexConverter
    app.register_blueprint(page_bp, **kwargs)
