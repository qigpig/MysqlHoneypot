import re,os
from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# 请自行更改密码
users = {
    "admin": generate_password_hash("gu+gugu")
}

def getHackerInfo():
    exp_path = os.path.abspath('.') + os.sep + "log"
    direxp = []
    for root,dirs,filenames in os.walk(exp_path):
        for filename in filenames:
            if 'config.data' in filename:
                direxp.append(os.path.join(root,filename))
    return direxp

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return True

@app.route('/')
@auth.login_required
def view_index():
    hackInfo = []
    infoList = []
    dataPath = getHackerInfo()
    for data in dataPath:
        ip = data.split(os.sep)[-2]
        infoList.append(ip)
        with open(data,'rb')as f:
            content = f.read().replace('\n','').replace('\r','').replace(' ','').replace('\t','').replace('\00','')
        f.close()
        wechatId = re.findall(r'WeChatFiles\\(.*)\\config', content)[0]
        infoList.append(wechatId)
        hackInfo.append(infoList)
        infoList = []
    return render_template('index.html',hackInfo=hackInfo)