from flask import render_template,redirect,url_for,abort,request,flash
from app.models import User
from .forms import UpdateProfile
from .. import db
from flask_login import login_required,current_user
from app.main import main