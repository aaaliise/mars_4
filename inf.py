from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/")
def mission():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    temp = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return "</br>".join(temp)


@app.route("/image_mars")
def image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="static/img/mars.png" alt="нет">
                      </body>
                    </html>'''


@app.route("/promotion_image")
def promotion_image():
    temp = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="static/img/mars.png" alt="нет">
                            <div class="alert alert-dark" role="alert">
                                {temp[0]}
                            </div>
                            <div class="alert alert-success" role="alert">
                                {temp[1]}
                            </div>
                            <div class="alert alert-secondary" role="alert">
                                {temp[2]}
                            </div>
                            <div class="alert alert-warning" role="alert">
                                {temp[3]}
                            </div>
                            <div class="alert alert-danger" role="alert">
                                {temp[4]}
                            </div>
                          </body>
                        </html>'''


@app.route('/form', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                        </select>
                                     </div>
                                     <br>
                                     <label for="form-group form-check">Какие у вас профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label><br />
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label><br />
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Пилот</label><br />
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Метеоролог</label><br />
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label><br />
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер по радиоционной защите</label><br />
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Врач</label><br />
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label><br />
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <br>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <br>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    temp = ["На ней много необходимых ресурсов;", "На ней есть вода и атмосфера;",
            "На ней есть небольшое магнитное поле;", "Наконец, она просто красива!"]
    return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <title>Варианты выбора</title>
                              </head>
                              <body>
                                <h1>Мое предложение: {planet_name}</h1>
                                <h1>Эта планета близка к Земле;</h1>
                                <div class="alert alert-success" role="alert">
                                    {temp[0]}
                                </div>
                                <div class="alert alert-secondary" role="alert">
                                    {temp[1]}
                                </div>
                                <div class="alert alert-warning" role="alert">
                                    {temp[2]}
                                </div>
                                <div class="alert alert-danger" role="alert">
                                    {temp[3]}
                                </div>
                              </body>
                            </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-light" role="alert">
                      составляет {rating}!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>'''


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
