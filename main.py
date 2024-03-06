from flask import Flask, render_template

app = (Flask(__name__))


@app.route('/training/<prof>')
def index(prof):
    param = {}
    param['prof'] = prof
    return render_template('trainings.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')