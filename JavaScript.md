JavaScript是Web的编程语言,所有现代的HTML页面都可以使用JavaScript.
HTML定义了网页的内容,CSS定义了网页的样式和布局,JavaScript则是用来实现网页的动态效果的脚本语言.
JavaScript是一种轻量级的编程语言,是可插入到HTML页面中的编程代码,由现代浏览器代为执行.

    JavaScript 用法:
HTML中的JavaScript脚本代码必须位于<script>和</script>标签之间,可以被放置在<head>或<body>中.
JavaScript代码可以直接写在HTML页面中,也可以单独写在一个.js文件中,然后在HTML页面中通过<script>标签引入.在<script>标签的src属性中指定.js文件的路径.外部脚本不能包含<script>标签.

    JavaScript 输出:
JavaScript没有任何打印或者输出的函数,可以通过不同的方式来输出数据.
1. 使用console.log()函数: console.log()函数可以打印到浏览器的控制台,可以输出任意数据类型.
2. 使用innerHTML属性: 可以将数据直接写入到HTML元素的innerHTML属性中,可以输出字符串,也可以输出HTML代码.
3. 使用document.write()函数: document.write()函数可以将数据直接写入到HTML页面的<body>部分,可以输出字符串,也可以输出HTML代码.
4. 使用弹出框: 可以使用window.alert()函数来弹出一个对话框,可以输出字符串.  
注意：如果文档已完成加载后再执行document.write()函数,则会覆盖整个页面.console.log()主要是用于调试和测试,不会影响页面的正常显示.而window.alert()会弹出一个对话框,页面会被暂停,用户无法进行任何操作.document.getElementById()可以获取HTML元素,document.getElementById(xx).innerHTML可以获取或插入元素内容.

    JavaScript 语言:
固定值称之为字面量,可以直接使用,如数字、字符串、布尔值等.
变量是存储数据的容器,可以用来保存和操作数据.
语句用分号;分隔,用分号来结束语句是可选的.使用驼峰命名法来命名变量.
代码块的作用是一并执行语句序列,使用花括号{}来定义代码块.
使用关键字var、let、const来定义变量,分别具有函数作用域、块作用域和块级作用域的常量.使用等号=来赋值.

    JavaScript 事件:
HTML事件时发生在HTML元素上的事情,当在HTML中使用JavaScript时,JavaScript可以出发这些事件.
HTML事件可以是浏览器行为,也可以是用户行为,JavaScript可以监听这些事件,并作出相应的响应.
常见的HTML事件有:
1. onclick: 当用户点击某个HTML元素时触发.
2. onmouseover: 当鼠标指针悬停在某个HTML元素上时触发.
3. onmouseout: 当鼠标指针移开某个HTML元素时触发.
4. onkeydown: 当用户按下某个键盘按键时触发.
5. onload: 当页面加载完成时触发.
6. onchange: 当HTML元素的内容发生变化时触发.
7. onsubmit: 当用户提交表单时触发.

    JavaScript 字符串模板:
JavaScript的字符串模板是一种特殊的字符串,``模板字符串``或者`模板字面量`,可以包含变量,可以使用${}语法来表示变量.(性质同python中的格式化字符串)

    javascript 错误处理:
原理同python的try-except-finally-raise语句.
try-catch-finally-throw语句,用于捕获并处理JavaScript代码中的错误.throw语句用于创建自定义错误.

    JavaScript 声明提升:
JavaScript的声明提升是指JavaScript在执行代码之前,会将变量和函数的声明提升到当前作用域的最前面.
JavaScript的声明提升的原因是JavaScript的作用域是函数作用域,而函数的声明应该在函数体之前.
通常在每个作用域开始前声明这些变量,这是正常的JavaScript解析步骤.
在严格模式下,JavaScript的声明提升会导致一些错误,因为在严格模式下,变量的声明必须出现在作用域的最前面.
use strict; //启用严格模式  
严格模式下,不允许使用未声明的变量;不允许删除变量或对象;不允许删除函数;不允许变量重名;不允许使用with语句;不允许使用eval()函数等.

    JavaScript 表单:
HTML表单是用来收集用户输入的元素,JavaScript可以用来操作表单.
HTML表单的属性:
1. name: 表单元素的名称,用于在服务器端进行数据处理.
2. value: 表单元素的初始值.
3. type: 表单元素的类型,如text、password、checkbox、radio、submit、button、image、reset、file等.
4. checked: 用于checkbox和radio类型的表单元素,表示是否被选中.
5. disabled: 用于禁用表单元素.
6. readonly: 用于只读的表单元素.
7. required: 用于必填的表单元素.
8. placeholder: 用于提示用户输入的内容.
9. maxlength: 用于限制用户输入的字符长度.
10. pattern: 用于限制用户输入的字符格式.
11. title: 用于提示用户输入的详细信息.

JavaScript操作表单:
一个HTML表单可能存在多个<form>标记,JS会为每个<form>元素创建一个Form对象,并存储到一个forms数组中.
访问表单的三种方式:
1. 通过表单的编号: document.forms[0]
2. 通过表单的名称: document.fname
3. 在支持DOM的浏览器中: document.getElementsByID("fID")或者document.getElementsByID("fname")

每个表单都是一个表单元素的集合,访问表单元素也是三种方式:
1. 通过元素的编号: document.form1.elements[0]
2. 通过name属性: document.form1.text1
3. 在支持DOM的浏览器中: document.getElementsByID("elementID")