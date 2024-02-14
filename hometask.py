"""
Создать страницу, на которой будет форма для ввода имени и электронной почты,
при отправке которой будет создан cookie-файл с данными пользователя,
а также будет произведено перенаправление на страницу приветствия,
где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», 
при нажатии на которую будет удалён cookie-файл с данными пользователя 
и произведено перенаправление на страницу ввода имени и электронной почты.
"""

from flask import Flask, render_template, url_for, make_response, request, redirect


app = Flask(__name__)
@app.route("/delete_cookie")
def delete_():
    delete_cookies()
    return redirect(url_for("main_page_"))

def delete_cookies():
    resp = make_response("cookies delted")
    for i in request.cookies:
        resp.delete_cookie(i)
    return resp


@app.route("/")
def main_page_():
    resp = make_response(render_template("main.html"))
    resp.set_cookie('user_cookie', 'cookie_value')
    return resp


@app.route("/sign_up", methods=["POST", "GET"])
def sign_up_():
    if request.method == "POST":
        name = request.form["name"]
        return redirect(url_for("cheers_"))
    return render_template("sign_up.html")

@app.route("/cheers", methods = ["POST", "GET"])
def cheers_():
    name = request.args.get("name")
    return render_template("cheers.html", name= name)




    """
    echo "# flask_hometask_2" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Maarulove/flask_hometask_2.git
git push -u origin main
    """