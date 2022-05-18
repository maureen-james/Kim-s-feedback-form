from . import main
from flask import render_template,abort,redirect,url_for,request,flash
from flask_login import login_required
from ..models import User,Feedback,Comment,Upvote,Downvote
from .. import db,photos
# from .forms import UpdateProfile, FeedbackForm, CommentForm
# from ..requests import get_quote

#Application views
@main.route('/dashboard')
def dashboard():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Kim-s-feedback-form'
    user = User.query.all()
    quotes = get_quote()
    feedback = Feedback.query.all()

    return render_template ('dashboard.html',title=title,feedback=feedback,quotes=quotes,user=user)

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    return render_template ('index.html')


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()

    if user is None:
        abort(404)
    else:
        return render_template('profile/profile.html', user = user)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.avatar = path
        db.session.commit()
    return redirect(url_for('main.profile',name = name))

@main.route('/user/<name>/update',methods = ['GET','POST'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username = name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',name = user.username))

    return render_template('profile/update.html',form =form)

@main.route('/create_new',methods = ['GET','POST'])
@login_required
def new_feedback():
    form = FeedbackForm()

    if form.validate_on_submit():
        company = form.company.data
        context = form.context.data
        new_feedback = Feedback(company=company,context=context)
        
        db.session.add(new_feedback)
        db.session.commit()
        return redirect(url_for('main.index'))
    else:
        all_feedback = Feedback.query.order_by(Feedback.posted)

    return render_template('new_feedback.html',feedback_form = form,feedback=all_feedback)

@main.route('/comment/<int:feedback_id>', methods = ['POST','GET'])
def comment(feedback_id):
    form = CommentForm()
    feedback = Feedback.query.get(feedback_id)
    all_comments = Comment.query.filter_by(feedback_id = feedback_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        feedback_id = feedback_id
        new_comment = Comment(comment=comment,feedback_id = feedback_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.comment', feedback_id = feedback_id))
    return render_template('comment.html',comment_form =form, feedback = feedback,all_comments=all_comments)

@main.route('/like/<int:id>', methods=['GET', 'POST'])
def like(id):
    feedback = Feedback.query.get(id)
    if feedback is None:
        abort(404)
    like = Upvote.query.filter_by(feedback_id=id).first()
    if like is not None:
        db.session.add(like)
        db.session.commit()
    new_like = Upvote(feedback_id=id)
    db.session.add(new_like)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/dislike/<int:id>', methods=['GET', 'POST'])
def dislike(id):
    feedback = Feedback.query.get(id)
    if feedback is None:
        abort(404)
    
    dislike = Downvote.query.filter_by(feedback_id=id).first()
    
    if dislike is not None:   
        db.session.add(dislike)
        db.session.commit()

    new_dislike = Downvote(feedback_id=id)
    db.session.add(new_dislike)
    db.session.commit()
    
    return redirect(url_for('main.index'))

@main.route('/delete_feedback/<int:id>',methods = ['GET','POST'])
@login_required
def delete(id):
    feedback= Feedback.query.get(id)
    db.session.delete(feedback)
    db.session.commit()

    return redirect(url_for('main.index'))

@main.route("/delete_comment/<int:id>")
@login_required
def delete_comment(id):
    comment = Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for('main.index'))