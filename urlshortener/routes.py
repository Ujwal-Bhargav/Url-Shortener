from flask import Blueprint,request,render_template,redirect

from urlshortener.models import Link
from urlshortener import extensions
short=Blueprint("short",__name__)



@short.route('/')
def index():
    return render_template('index.html')

@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    link.visits+=1
    extensions.db.session.commit()
    return redirect(link.original_url)



@short.route('/add_link',methods=["POST"])
def add_link():
    original_url=request.form["original_url"]
    link=Link(original_url=original_url)
    extensions.db.session.add(link)
    extensions.db.session.commit()
    return render_template('link_added.html',original_url=link.original_url,new_link=link.short_url)

@short.route('/stats')
def stats():
    links=Link.query.all()
    return  render_template('stats.html',links=links)

@short.errorhandler(404)
def page_not_found(e):
    return '<h1> 404 Page not found</h1>',404