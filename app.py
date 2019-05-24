from member.controller import MemberController
from blood.model import BloodModel
from ai_calc.controller import CalculatorController
from gradient_descent.controller import GradientDescentController
from iris.controller import IrisController
from chatbot.controller import ChatbotController
from cabbage.controller import CabbageController
import re

from flask import Flask, jsonify, render_template, request

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('home.html', name='')

@app.route('/login', methods=['POST'])
def login():
    print('로그인 들어옴')
    userid = request.form['userid']
    password = request.form['password']
    print("컨트롤러 아이디 {}, 비번 {}".format(userid, password))
    ctrl = MemberController()
    view = ctrl.login(userid, password)
    return render_template(view)

@app.route('/move/<path>',methods=['GET'])
def move(path):
    print('{} 로 이동 '.format(path))
    return render_template('{}.html'.format(path))

@app.route('/blood',methods=['POST'])
def blood():
    weight = request.form['weight']
    age = request.form['age']
    print("컨트롤러 아이디 {}, 비번 {}".format(weight, age))
    model = BloodModel('blood/data/data.txt')
    raw_data = model.create_raw_data()
    render_params = {}
    val = model.make_session(raw_data, weight, age)
    render_params['result'] = val
    return render_template('blood.html', **render_params)


@app.route('/ai_calc', methods=['GET','POST'])
def ai_calc():
    print("계산기 진입 ")
    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']
    print("{} {} {} = ".format(num1, num2, opcode))
    c = CalculatorController(num1, num2, opcode)

    val = c.calc()
    render_params = {}
    render_params['result'] = val
    return render_template('ai_calc.html', **render_params)


@app.route('/iris', methods=['GET','POST'])
def predict_iris():

    ctrl = IrisController()
    result = ctrl.service_model()
    render_params = {}
    render_params['result'] = result
    return render_template('iris.html', **render_params)

@app.route('/cabbage', methods=['GET','POST'])
def predict_cabbage():

    ctrl = CabbageController()
    result = ctrl.service_model()
    render_params = {}
    render_params['result'] = result
    return render_template('cabbage.html', **render_params)



@app.route('/ui_calc')
def ui_calc():
    stmt = request.args.get('stmt','NONE')
    if (stmt == 'NONE'):
        print('넘어온 값이 없음')
    else :
        print('넘어온 식: {}'.format(stmt))
        patt = '[0-9]+'
        op = re.sub(patt, '', stmt)
        print('넘어온 연산자: {}'.format(op))
        nums = stmt.split(op)

        if op == '+':
            result = int(nums[0]) + int(nums[1])
        elif op == '-':
            result = int(nums[0]) - int(nums[1])
        elif op == '*':
            result = int(nums[0]) * int(nums[1])
        elif op == '/':
            result = int(nums[0]) / int(nums[1])

    # 연산
    return jsonify(result = result)


@app.route("/gradient_descent")
def gradient_descent():
    ctrl = GradientDescentController()
    name = ctrl.draw_chart()
    return render_template('gradient_descent.html', name=name)

@app.route("/chatbot", methods=['GET','POST'])
def chatbot():
    pass



if __name__ == '__main__':
    app.run()













