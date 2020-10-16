from flask import abort
from flask import render_template,request
from flask import Blueprint
import pyshorteners
from datetime import date

url_shortener = Blueprint('url_shortener', __name__)

@url_shortener.route('/')
@url_shortener.route('/home')
def home():
	return render_template('home.html')


@url_shortener.route('/shortened_url', methods=['POST'])
def shorten_url():
	link = request.form['link']
	shortner = pyshorteners.Shortener()
	res = shortner.tinyurl.short(link)
	#print(res)
	res = {'short_url_res': res}
	return render_template('result.html', result=res)


@url_shortener.route('/shortened_url_via_api', methods=['POST'])
def shorten_url_via_api():
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    link = request.args.get('link','')
    shortner = pyshorteners.Shortener()
    res = shortner.tinyurl.short(link)
    #print(res)
    res = { 'result':'Success',
    		'status_code':201,
    		'time':d2,
    		'shortened_url': res}
    return res