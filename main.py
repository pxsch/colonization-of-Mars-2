from flask import Flask, render_template

app = (Flask(__name__))


@app.route('/training/<prof>')
def index(prof):
    param = {}
    param['prof'] = prof
    return render_template('trainings.html', **param)


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    param = {}
    param['list'] = list
    param["professions"] = professions
    return render_template('professions.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')