from flask import render_template, url_for, flash, redirect
from f5InterviewProject import app, db
from f5InterviewProject.forms import FamilyAdd
from f5InterviewProject.models import Post





@app.route("/", methods=['GET'])
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)





@app.route("/add", methods=['GET','POST'])
def add():
    form = FamilyAdd()
    if form.validate_on_submit():
        post=Post(firstName=form.firstName.data, lastName=form.lastName.data)
        db.session.add(post)
        db.session.commit()
        flash('Success!', 'success') 
        return redirect(url_for('home'))  
    return render_template('add.html', title='Add', form=form)