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
    <!--行内标签,不独占一行,可以连接起来-->
    <span style="color:red;">这是我的第一个网页</span><!--创建span元素,并添加内容;span标签是行内标签,不独占一行,可以嵌入到其他标签中,如<p>标签中-->    <br><!--创建换行符-->
    <p>这是我的第一个网页</p><!--创建p元素,并添加内容;p标签是段落标签,用来显示文本内容,可以包含多个<span>、<div>等标签-->   <br><!--创建换行符-->
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
</body>
</html>
```
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>用户注册</title>
</head>
<body>
    <h1>用户注册</h1>
    <p>欢迎注册，请填写以下信息：</p>
    <div>
        用户名：<input type="text" name="username"><br>
        密码：<input type="password" name="password"><br>
        确认密码：<input type="password" name="confirm_password"><br>
        邮箱：<input type="email" name="email"><br>
        性别：<input type="radio" name="gender" value="male">男
        <input type="radio" name="gender" value="female">女<br>
        爱好：
        <input type="checkbox" name="hobby[]" value="reading"> 阅读
        <input type="checkbox" name="hobby[]" value="swimming"> 游泳
        <input type="checkbox" name="hobby[]" value="running"> 跑步
        <input type="checkbox" name="hobby[]" value="basketball"> 篮球
        <input type="checkbox" name="hobby[]" value="football"> 足球
        <input type="checkbox" name="hobby[]" value="pingpang"> 乒乓球<br>
        城市：
        <select name="city">
            <option value="beijing">北京</option>
            <option value="shanghai">上海</option>
            <option value="guangzhou">广州</option>
            <option value="shenzhen">深圳</option>
        </select><br>
        个人标签：<br>
        <select name="tag[]" multiple> 
            <option value="student">学生</option>
            <option value="worker">社畜</option>
            <option value="playinggame">打游戏</option>
            <option value="sleeping">睡觉</option>
            <option value="eating">吃饭</option>
            <option value="havingfun">开心</option>
            <option value="friends">交朋友</option>
        </select><br>
        个人简介：<br>
        <textarea name="introduction" rows="5" cols="30"></textarea><br>
        <input type="submit" value="submit提交">
        <input type="button" value="button提交">
    </div>
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

创建Django项目:django-admin startproject myproject