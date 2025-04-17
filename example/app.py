from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/register', methods=['GET'])#限制访问方式为GET
# def register():
#     return render_template('register.html')#返回注册页面register.html,用flask的render_template函数渲染

# # @app.route('/do/register', methods=['GET'])#限制访问方式为GET
# # def do_register():
# #     # 注册页面,用<form>标签实现收集用户输入的信息
# #     print(request.args)
# #     return '注册成功'

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    # 注册页面,用<form>标签实现收集用户输入的信息
    else:
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            return '两次输入的密码不一致'
        email = request.form.get('email')
        gender = request.form.get('gender')
        hobbies = request.form.getlist('hobby')
        city = request.form.get('city') 
        tags = request.form.getlist('tags')
        introduction = request.form.get('introduction')
        print(username, password, email, gender, hobbies, city, tags, introduction)
        return '注册成功'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        return '登录成功'
        

if __name__ == '__main__':
    app.run(debug=True)