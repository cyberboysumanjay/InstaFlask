from flask import Flask, render_template,request,jsonify,json
import instagram

app = Flask(__name__)
app.secret_key = 'iknowyoucanseethis'

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
   return render_template("index.html")

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'POST':
        result = request.form
        username=(result['userid'])
    id=''
    user=''
    try:
        id=instagram.getID(username)
        if id=='invalid_username':
            return '<h1>Invalid Username</h1><br><h2>Please go back and enter a valid username to continue</p>'
    except Exception as e:
        print(e)
    try:
        user_data=instagram.userDetails(id)
    except Exception as e:
        print(e)
    dp_url=user_data['user']['hd_profile_pic_versions'][0]['url']
    hd_dp_url=user_data['user']['hd_profile_pic_url_info']['url']
    username=user_data['user']['username']
    fullname=user_data['user']['full_name']
    private_profile=user_data['user']['is_private']
    is_verified=user_data['user']['is_verified']
    anonymous_profile_pic=user_data['user']['has_anonymous_profile_picture']
    total_posts=user_data['user']['media_count']
    followers=user_data['user']['follower_count']
    following=user_data['user']['following_count']
    bio=user_data['user']['biography']
    if len(bio)==0:
        bio='None'
    report_fraud=user_data['user']['can_be_reported_as_fraud']
    try:
        external_url=user_data['user']['external_url']
    except:
        external_url='None'
    finally:
        if len(external_url)==0:
            external_url='None'


    return render_template("display.html",dp_url=dp_url,username=username,fullname=fullname,private_profile=private_profile,is_verified=is_verified,anonymous_profile_pic=anonymous_profile_pic,total_posts=total_posts,followers=followers,following=following,bio=bio,external_url=external_url,report_fraud=report_fraud,hd_dp_url=hd_dp_url)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
