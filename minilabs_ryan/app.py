from flask import Blueprint, render_template, request
minilabs_ryan_bp = Blueprint('ryan', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')