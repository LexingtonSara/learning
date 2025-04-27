零、前言
Web开发早期,开发者需要手动编写每个页面.后来使用程序为Web服务器动态生成内容,这项技术称为CGI(Common Gateway Interface)公共网关接口.CGI程序运行在服务器上,接收HTTP请求,生成HTTP响应,并把响应发送给客户端.

Web应用的工作流程及术语:
1.URL/URI：Uniform Resource Locator/Identifier，统一资源定位符/标识符，用来标识互联网上资源的地址
2.IP地址：Internet Protocol Address，互联网协议地址，用来标识互联网上计算机的位置
3.域名：Domain Name，域名，用来标识互联网上计算机的名称(ip地址的别名)
4.DNS：Domain Name System，域名系统，用来将域名转换为IP地址
5.HTTP协议：Hypertext Transfer Protocol，超文本传输协议，构建在TCP之上的应用层协议，用于从Web服务器传输超文本到客户端的请求
6.Web服务器：Web Server，网络服务器，运行HTTP协议的软件，负责响应HTTP请求并返回HTTP响应
7.反向代理:代理客户端向服务器发出请求,然后将服务器返回的资源返回客户端
8.Nginx：高性能的Web服务器，支持异步非阻塞I/O模型，支持热部署，支持负载均衡，支持动静分离，支持缓存，支持多线程

HTTP协议:构建与TCP(Transmission Control Protocol传输控制协议)之上的应用层协议,利用TCP提供的可靠的服务传输实现了Web应用中的数据交换.
HTTP请求(请求行+请求头+空行+[消息体]):
1.请求行：GET /index.html HTTP/1.1，请求方法(GET/POST/PUT/DELETE)、请求路径、HTTP版本
2.请求头：Host:www.example.com，请求域名
3.空行：表示请求头和消息体的分隔符
4.消息体：GET请求没有消息体,POST请求有消息体,消息体可以是表单数据,JSON数据,XML数据等.

HTTP响应(响应行+响应头+空行+消息体):
1.响应行：HTTP/1.1 200 OK，HTTP版本、响应状态码、响应状态描述
2.响应头：Content-Type:text/html;charset=utf-8，响应内容类型、字符编码
3.空行：表示响应头和消息体的分隔符
4.消息体：响应消息体可以是HTML页面,JSON数据,XML数据等.

一、Flask简介
Flask是一个轻量级的Web应用框架,它使用Python语言编写.
```python
from flask import Flask#导入Flask类,Flask类是Flask框架的核心类,用于创建Web应用程序实例
app = Flask(__name__)#创建Flask应用实例,参数__name__表示当前模块的名称,在模块中运行时是__main__,在其他模块中导入时是模块的名称

@app.route('/')#装饰器,告诉Flask哪个URL能够触发下面的函数
def index():#当用户访问根URL时,执行该函数
    return 'Hello, World!'#返回响应消息体

if __name__ == '__main__':
    app.run(debug=True)#启动Flask应用,debug=True表示调试模式,可以看到错误信息
```
二、HTML简介
HTML(Hypertext Markup Language)是一种用于创建网页的标记语言,它是一种基于XML的标记语言,是一种标准通用标记语言.HTML使用标记标签来描述网页的内容,如文本、图片、表格、链接等.HTML标签由尖括号包围,如<html>、<body>、<h1>、<p>等.
```html
<!DOCTYPE html>#设置文档类型为HTML
<html>#创建HTML文档
<meta charset="utf-8">#设置网页编码
<head>
    <title>Hello, World!</title>#设置网页标题
</head>
<body> <!--块级标签,独占一行,-->
    <h1>Hello, World!</h1> <!--创建标题,显示Hello, World!;标题一共有6级,从h1到h6,h1是最重要的标题,h6是最低级的标题-->
    <div>第一个html网页</div><!--创建div元素,并添加内容;可以容纳其他HTML元素,如图片、文本、表格等-->
    <p>这是我的第一个网页</p><!--创建p元素,并添加内容;p标签是段落标签,用来显示文本内容,可以包含多个<span>、<div>等标签-->   
    <!--行内标签,不独占一行,可以连接起来-->
    <span style="color:red;">这是我的第一个网页</span><!--创建span元素,并添加内容;span标签是行内标签,不独占一行,可以嵌入到其他标签中,如<p>标签中-->    <br><!--创建换行符-->
    
    <!--标签内可以添加属性信息-->
    <a href="https://www.baidu.com" target="_blank">百度</a><!--创建超链接,并添加链接地址;a标签是超链接标签,可以将用户从当前页面转到其他页面,或者下载文件等-->    <br><!--创建换行符-->
    <img style ="width:100px;height:100px;" src="https://www.baidu.com/img/bd_logo1.png" alt="百度logo"><!--创建图片,并添加图片地址和替代文字;img标签是图片标签,可以显示图片,可以用本地文件路径或网络地址来指定图片源.自闭合标签,没有内容,无需结束标签-->    <br><!--创建换行符-->
    <ul> <!--创建无序列表-->
        <li>列表1</li> <!--创建列表项,并添加内容-->
        <li>列表2</li> <!--创建列表项,并添加内容-->
        <li>列表3</li> <!--创建列表项,并添加内容-->
    </ul> <!--结束无序列表-->
    <ol> <!--创建有序列表-->
        <li>列表1</li> <!--创建列表项,并添加内容-->
        <li>列表2</li> <!--创建列表项,并添加内容-->
        <li>列表3</li> <!--创建列表项,并添加内容-->
    </ol> <!--结束有序列表-->
    <hr><!--创建水平线，用于分隔内容--> 
    <table border="1"> <!--创建表格，border属性设置表格边框宽度-->
        <thead> <!--创建表格头-->
            <tr> <!--创建表格行-->
                <th>表头1</th> <!--创建表头单元格,并添加内容-->
                <th>表头2</th> <!--创建表头单元格,并添加内容-->
                <th>表头3</th> <!--创建表头单元格,并添加内容-->
            </tr>
        </thead>
        <tbody> <!--创建表格体-->
            <tr> <!--创建表格行-->
                <td>文本内容</td> <!--创建单元格,并添加内容-->
                <td>
                    <img style ="width:50px;height:50px;"  src="https://www.baidu.com/img/bd_logo1.png" alt="百度logo">  <!--创建图片作为单元格内容-->
                </td> <!--创建单元格,并添加内容-->
                <td>
                <a href="https://www.baidu.com" target="_blank">详情请点击搜索</a> <!--创建超链接作为单元格内容-->
                </td> <!--创建单元格,并添加内容-->   
            </tr>
        </tbody>
    </table> <!--结束表格-->
    <input type="text" /> <!--创建输入框,用于输入文本--><br><!--行内标签,需手动创建换行符-->
    <input type="password" /> <!--创建密码输入框,用于输入密码,不会显示输入内容--><br><!--行内标签,需手动创建换行符-->
    <input type="file" /> <!--创建文件上传框,用于上传文件--><br><!--行内标签,需手动创建换行符-->
    <input type="radio" name="gender" />男 <!--创建单选框-->
    <input type="radio" name="gender" />女<!--名字一致,表示同一组单选框-->
    <input type="checkbox" />蓝球 <!--创建蓝球复选框-->
    <input type="checkbox" />足球 <!--足球复选框-->
    <hr>
    <input type="button" value="提交" /> <!--创建按钮,用于提交-->
    <input type="submit" value="提交" /> <!--创建提交按钮,用于提交表单-->
    <hr>
    <!--下拉框-->
    <select multiple><!--multiple属性表示可以选择多个选项,无multiple属性表示只能选择一个选项-->
        <option value="1">选项1</option>
        <option value="2">选项2</option>
        <option value="3">选项3</option>
    </select>
    <!--结束下拉框-->
    <!--多行文本-->
    <textarea rows="5" cols="30"></textarea><!--创建多行文本框,rows属性设置行数,cols属性设置列数-->
    <form action="http://www.baidu.com" method="post"> <!--创建表单,action属性设置提交地址,method属性设置提交方式-->
        <input type="text" name="username" /> <!--创建输入框,用于输入用户名-->
        <input type="password" name="password" /> <!--创建密码输入框,用于输入密码-->
        <input type="submit" value="提交" /> <!--创建提交按钮,用于提交表单-->
    </form> <!--结束表单-->
</body>
</html>
```

网络请求流程:
1.用户在浏览器输入网址,访问Web服务器
浏览器会发送数据到Web服务器的80端口,本质上发送的是字符串数据.
"GET / expore/ HTTP/1.1\r\nHost: ...\r\nuser-agent: ...\r\n\r\n"
GET请求[URL方法/表单提交]:get请求、跳转、向后台传入数据,数据会拼接在url后面,以?分割.
POST请求[表单提交]:post请求、提交表单、向后台传入数据,数据会拼接在请求体中.
2.Web服务器接收到请求,解析请求信息,生成HTTP请求报文


二、Django简介
Django是一个Python Web框架,是一个高级的Web应用开发框架,它可以快速开发出功能完善的Web应用.Django是用Python语言编写的,使用了MVC(Model-View-Controller)模式,MVC模式将应用程序分成三个层次:模型层、视图层、控制器层.Django项目中我们称之为MTV,MTV中的M跟MVC中的M没有区别,就是代表数据的模型,T代表了网页模板（显示数据的视图）,而V代表了视图函数,在Django框架中,视图函数和Django框架本身一起扮演了MVC中C的角色.

    Django 模版
django.http.HttpResponse():用于返回HTTP响应,可以返回文本、JSON数据、XML数据等.
django.shortcuts.render():用于渲染模板,第一个参数为request,第二个参数为模板名称,第三个参数为模板数据.
django.shortcuts.redirect():用于重定向,跳转新页面,参数为URL地址.
django.shortcuts.reverse():用于反向解析,根据URL名称获取URL地址.
Django 模版标签:在项目文件夹下创建名为templates的目录(可以按app名称进行细分),用于存放模板文件.
HTML模板文件:以.html为后缀,包含了HTML代码,可以包含Django模板标签.用{{HTML变量名}}包围的变量会在视图函数中进行替换.
在应用的views.py文件中,编写视图函数,用Views变量名来保存需要返回的数据,并用render函数渲染模板,最终返回render(request, '模版文件名称.html', {'HTML变量名': 'Views变量名'})的结果.
在应用的urls.py文件中,编写URL路由,将view.py中的视图函数与URL进行绑定,,并将URL路由包含进项目的URL路由中.
Django提供了过滤器,可以对模板变量进行过滤,如对字符串进行截取、格式化等.
模版语法:{{ 变量名 | 过滤器:可选参数 }},模版过滤器可以在变量被显示前修改它,过滤使用管道字符.
过滤器可以被套接,如{{ 变量名 | 过滤器1:参数1 | 过滤器2:参数2 }}.过滤器的参数跟随冒号之后且总是以双引号包含.
if/else标签:{% if 条件 %}...{% elif 条件 %}...{% else %}...{% endif %}
for/in标签:{% for 变量 in 序列 %}...{% endfor %},用法同python,在{% for%}标签中可以通过使用{{forloop}}变量获取循环序号.
forloop.counter: 顺序获取循环序号，从 1 开始计算
forloop.counter0: 顺序获取循环序号，从 0 开始计算
forloop.revcounter: 倒序获取循环序号，结尾序号为 1
forloop.revcounter0: 倒序获取循环序号，结尾序号为 0
forloop.first（一般配合if标签使用）: 第一条数据返回 True，其他数据返回 False
forloop.last（一般配合if标签使用）: 最后一条数据返回 True，其他数据返回 False

模版继承:模版可以用集成的方式来实现复用,父模版放置可重复利用的内容,子模版继承父模版,并添加新的内容.
{% extends '父模版路径' %} <!--继承父模版-->
{% block 块名 %}...{% endblock %} <!--父模版中预留的块,留给自末班填充差异性内容,子模版可以重写父模版中的块内容-->


    Django 模型
Django对各种数据库提供了很好的支持,包括关系型数据库(如MySQL、PostgreSQL、SQLite、Oracle),为这些数据库提供了统一的调用API.
ORM(Object-Relational Mapping)用于实现面向对象编程语言里不同类型的数据之间的转换,ORM在业务逻辑层和数据库层之间充当了桥梁的作用.
Django的模型层提供了一种抽象的概念,可以将数据库中的数据映射到Python对象上,并提供对数据的CRUD(Create-Read-Update-Delete)操作.
    models类 每个模型类对应数据库中的一张表,模型类中定义了表的字段和约束条件.
    对象实例 每个对象实例对应数据库中的一行记录,对象实例中包含了表中的字段值.
    属性 每个属性对应数据库中的一个字段,属性中包含了字段的值.
ORM无法操作到数据库级别,只能操作到表级别,所以在使用mysql数据库时,需要提前创建好数据库.然后向项目的settings.py文件中添加数据库配置信息.并在__init__.py文件中导入pymysql模块,pymysql.install_as_MySQLdb()方法用于将pymysql模块替换为MySQLdb模块,以支持django的mysql数据库操作.
Django中药使用模型,必须药创建一个app,然后在models.py文件中定义模型,在admin.py文件中注册模型,在views.py文件中编写视图函数,在urls.py文件中定义URL路由,然后在项目的settings.py文件中注册app.


    Django 视图
Django的视图层是一个视图函数,是一个简单的python函数,它负责处理HTTP请求,并生成HTTP响应.可以返回HTML页面、JSON数据、XML数据等.
每个视图函数都负责返回一个HttpResponse对象,对象中包含生成的响应.视图层中有两个重要的对象:request和HttpResponse.
request对象的几个常用的属性:
    GET:数据类型是QueryDict,一个类似于字典的对象,包含了HTTP GET的所有参数.
    POST:数据类型是QueryDict,一个类似于字典的对象,包含了HTTP POST的所有参数.
    body:数据类型是bytes,是原生请求体里的参数内容,在HTTP中用于POST，因为GET请求没有请求体.
    path:获取URL中的路径部分,数据类型是字符串.
    method:获取HTTP请求的方法,数据类型是字符串.结果为大写字母.

响应对象:主要有三种形式,HttpResponse()、render()、redirect().
    HttpResponse()对象:返回文本,参数为字符串,字符串中写文本内容,如果桉树为字符串里含有html标签,也可以渲染.
    render():返回文本,第一个参数为request,第二个参数为字符串(页面名称),第三个参数为字典(可选参数,用于传递给模板的数据).
    redirect():重定向,跳转新页面,参数为字符串,字符串中写要跳转的URL地址.一般用于form表单提交后,重定向到指定页面.


创建Django项目的基本步骤: 
    按照官方文档进行第一个Django应用的编写,第一部分:
    1.使用命令来引导一个新的Django项目 ...\>django-admin startproject myproject 
创建Django项目时可以使用 django-admin startproject myproject 命令,如果后面不指定项目名称,则默认创建名为myproject的项目.如果指定项目名称,则需提前创建一个项目文件夹,然后运行命令.
此时会在项目文件夹下创建一个名为myproject的目录,该目录包含了Django项目的基本文件和目录结构.
    manage.py:Django项目的管理脚本,用于启动项目、创建应用、运行服务器等.
    myproject/
        __init__.py:空文件,用于标识当前目录为Python包.
        settings.py:Django项目的配置文件,包含了项目的配置信息,如数据库配置、静态文件配置、中间件配置等.
        urls.py:Django项目的URL配置文件,包含了项目的URL路由配置.
        wsgi.py:WSGI配置文件,用于部署Django项目到Web服务器.接受HTTP请求,并将请求交给Django项目处理.
        asgi.py:ASGI配置文件,用于部署Django项目到Web服务器.接受HTTP请求,并将请求交给Django项目处理.
        views.py:Django项目的视图文件,用于处理HTTP请求.
    
    2.验证Django项目是否创建成功
先进入项目文件夹,运行命令 ...\>python manage.py runserver 

    3.创建Django应用
在Django项目中,每一个应用都是一个Python包,Django自带一个工具,可以帮助生成应用的基础文件和目录结构.
运行命令 ...\>python manage.py startapp myapp 
创建一个名为myapp的目录,该目录其布局如下:
    myapp/
        __init__.py:空文件,用于标识当前目录为Python包.
        admin.py:Django应用的管理文件,用于注册模型到Django的后台管理系统.
        apps.py:Django应用的配置文件,用于配置Django应用的基本信息.
        migrations/
            __init__.py:空文件,用于标识当前目录为Python包.
        models.py:Django应用的模型文件,用于定义数据模型.
        tests.py:Django应用的测试文件,用于编写测试用例.
        views.py:Django应用的视图文件,用于处理HTTP请求.

    4.编写第一个视图
打开myapp/views.py文件,编写第一个视图函数:
```python
# from django.http import HttpResponse #导入HttpResponse类,用于返回HTTP响应
from django.shortcuts import render #导入render函数,用于渲染模板

def index(request):#定义视图函数,参数request是Django封装好的请求对象,包含了请求信息
    # return HttpResponse("Hello, World!")#返回HTTP响应,内容为"Hello, World!"
    return render(request, 'index.html', {'name': 'Django'})#渲染模板,第一个参数为request,第二个参数为模板名称,第三个参数为模板数据

```

在myapp/urls.py文件中,将视图函数与URL进行绑定:
```python
from django.urls import path
from myapp import views #导入视图函数,注意导入的是myapp.views而不是views,也可以使用 from . import views 导入当前模块的视图函数

urlpatterns = [
    path('', views.index, name='index'),
]#定义URL路由,将URL映射到视图函数,name参数用于给视图函数命名,方便在模板中使用.
```
在myproject/urls.py文件中,将myapp的URL路由导入到项目的URL路由中:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),#path函数至少需要两个参数,route和view,分别表示URL和视图函数.
    path('myapp/', include('myapp.urls')),#include函数用于包含其他URL路由,每当Django遇到include函数时,它会阶段URL中匹配到该点的部分,并将剩余的字符串传递给包含的URL路由以进行进一步处理.
]#定义项目的URL路由,将myapp的URL路由包含进来.
```
验证项目是否正常运行:
1.运行命令 ...\>python manage.py runserver 
2.在浏览器中输入网址 http://127.0.0.1:8000/myapp/       

    第二部分:
    0.前置条件:
打开myproject/settings.py文件,先将TIME_ZONE和LANGUAGE_CODE配置项设置为合适的值:新项目模板中TIME_ZONE配置项默认值为UTC,LANGUAGE_CODE配置项默认值为en-us.在windows系统下,Django无法可靠的使用交替时区,TIME_ZONE必须设置与系统时区一致.

头部文件中有INSTALLED_APPS配置项,包含了会在项目中启用的所有Django应用.默认包括了:
    django.contrib.admin:管理员站点
    django.contrib.auth：用户认证系统
    django.contrib.contenttypes：内容类型框架
    django.contrib.sessions：会话框架
    django.contrib.messages：消息框架
    django.contrib.staticfiles：静态文件框架
默认开启的某些应用至少需要一个数据表,所以在使用他们之前需要在数据库中创建相应的数据表.使用命令创建数据表: ...\>python manage.py migrate 
    1.数据库配置
Django项目默认使用SQLite数据库,如果需要使用其他数据库,则需要进行数据库配置.
比如使用MySQL数据库,则需要在myproject/settings.py文件中配置DATABASES配置项:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
        'PORT': 'your_database_port',
    }
}
```
其中ENGINE配置项指定了数据库的引擎,NAME配置项指定了数据库的名称,USER配置项指定了数据库的用户名,PASSWORD配置项指定了数据库的密码,HOST配置项指定了数据库的主机地址,PORT配置项指定了数据库的端口号.
在配置完数据库后,运行命令 ...\>python manage.py makemigrations 


    2.创建模型
在Django里写一个数据库驱动的Web应用,首先需要定义数据模型,也就是数据库结构设计和附加的其它元数据.
Django使用ORM(Object-Relational Mapping)技术,将数据库表和Python对象进行映射,使得数据库操作和Python代码可以分离.
Django的模型定义文件是myapp/models.py,比如定义了一个名为Person的模型:
```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
```
Person模型包含三个字段:name、age、email,分别表示姓名、年龄、邮箱,其中name字段使用CharField类型,表示字符串类型,最大长度为100,age字段使用IntegerField类型,表示整数类型,email字段使用EmailField类型,表示邮箱类型.

Django的模型定义文件中还可以定义其它元数据,比如设置默认值、是否必填、是否唯一等.
在未指定PrimaryKey的情况下,Django会自动创建id字段作为主键.

    3.激活模型
在Django项目中,模型是需要激活的,才能在数据库中创建表.
在myproject/settings.py文件中,将myapp添加到INSTALLED_APPS配置项中:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig', #添加myapp应用
]
```
然后运行命令 ...\>python manage.py makemigrations myapp 
通过makemigrations命令,Django会检测模型文件的变化,并把修改的部分存储为一个迁移.迁移是Django用来跟踪模型变化的机制.也是磁盘上的文件,记录了模型的变更.它被储存在myapp/migrations目录下.
Django有一个自动执行数据库迁移并同步管理数据库结构的命令migrate,运行命令 ...\>python manage.py migrate 

编辑models.py文件,改变模型.
运行命令 ...\>python manage.py makemigrations myapp  为模型文件生成迁移文件.
运行命令 ...\>python manage.py migrate  执行数据库迁移,同步模型到数据库.

    4.初试API
API(Application Programming Interface)是应用程序编程接口,是一组协议,使得应用程序可以相互通信和交流.
API允许开发人员集成来自其他应用程序的数据、服务和功能,而不是从头开始开发,从而实现快速开发和迭代.无需了解这些应用程序的内部实现,只需调用API即可.
    API的主要形式:
出现在程序语言中:例如计算一个数的n次方,可以用函数pow(x,n)来实现,pow函数就是语言提供的API.
出现在安装的依赖中:例如Python的requests库,它提供的requests.get()函数就是API.
用了第三方服务以网络形式请求出现:例如使用百度搜索引擎API,可以用requests.get()函数向百度服务器发送请求,获取搜索结果.

    5.介绍Django的管理页面
Django Admin 管理工具是django.contrib 的一部分,它是一个基于Web的管理界面,用于管理Django项目中的数据.
激活管理工具:在myproject/myproject/urls.py文件中,添加以下代码:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
]#本代码会在创建项目时自动生成,不需要手动添加.
```
然后运行命令 ...\>python manage.py runserver 
在浏览器中输入网址 http://127.0.0.1:8000/admin/ 
就可以看到Django Admin 管理工具的登录页面.

使用管理工具:
通过运行命令 ...\>python manage.py createsuperuser 创建一个超级用户,用于登录管理工具.
登录成功后,就可以在管理工具中管理数据库中的数据了.

为了让admin界面管理某个数据模型,需要在admin.py文件中注册模型:
```python
from django.contrib import admin
from myapp.models import Person

admin.site.register(Person)
```
就可以在Django Admin 管理工具中管理Person模型了.    