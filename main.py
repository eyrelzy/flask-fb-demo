from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
import os

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_object('conf.Config')

# Get constants
FACEBOOK_APP_ID = app.config.get('FACEBOOK_APP_ID')
FACEBOOK_SECRET = app.config.get('FACEBOOK_SECRET')
app.debug = app.config.get('DEBUG')
app.secret_key = os.environ.get('SECRET_KEY')

# oauth to facebook
oauth = OAuth()
facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_SECRET,
    request_token_params={'scope': 'email'}
)


@app.route('/')
def index():
  if 'logged_in' not in session:
    return "<a href='" + url_for('login') + "'>Log in with Facebook.</a>"
  else:
    return redirect(url_for('show_info'))

@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))

@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['facebook_token'] = (resp['access_token'], '')
    session['logged_in'] = True

    return redirect(url_for('show_info'))

@facebook.tokengetter
def get_facebook_oauth_token():
    """ Return the access token. """
    return session.get('facebook_token')

@app.route("/logout")
def logout():
    """ Log out the user. """
    session.pop('logged_in', None)
    session.pop('facebook_token', None)
    return redirect(url_for('index'))

@app.route('/info')
def show_info():
    """ Print info about the facebook user. """
    me = facebook.get('/me')
    friends = facebook.get('/me/friends')
    return 'Logged in as id=%s name=%s redirect=%s' % \
       (me.data['id'], me.data['name'], request.args.get('next'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    if FACEBOOK_APP_ID and FACEBOOK_SECRET:
        app.run(host='0.0.0.0', port=port)
    else:
        print 'Cannot start application without Facebook App Id and Secret set'
