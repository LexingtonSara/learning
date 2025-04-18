    零、css简介
CSS(Cascading Style Sheets)是一种用于表现HTML(Hypertext Markup Language)的样式语言。CSS描述了HTML文档中元素的外观和版式,包括字体、颜色、大小、边框、背景、透明度、对齐方式等.

    CSS 网页布局
网页布局有很多种方式，一般分为以下几个部分：头部区域、菜单导航区域、内容区域、底部区域.
头部区域:位于整个网页的顶部,通常包含logo、标题、搜索框等.
菜单导航区域:包含了一些链接,可以引导用户浏览其他页面.
内容区域:一般有三种形式,1列:一般用于移动端、2列:一般用于平板设备、3列:一般用于PC桌面设备.
底部区域:包含版权信息、联系方式、网站地图等.
响应式网页布局:响应式网页布局是指网页可以根据不同设备的屏幕大小和分辨率调整布局,以适应不同设备的访问.
响应式网页设计的原理是通过CSS3的媒体查询(media query)来实现的.

    CSS 语法
CSS规则由两个主要的部分构成,选择器以及一条或者多条声明.
选择器用于指定一个需要改变样式的HTML元素;声明用于设置HTML元素的样式,每条声明由一个属性和一个值组成,本质是用分号分隔的键值对.

    CSS 选择器和组合选择符
CSS选择器用于指定HTML元素,可以是标签名、类名、ID、属性、伪类等.
id选择器:为标有特定id的HTML元素指定特定的样式,HTML元素中用id属性来设置id选择器,CSS中id选择器以"#"来定义.id属性不能以数字开头,数字开头的id在Mozilla/Firefox浏览器中会被忽略.
class选择器:用于描述一组元素的样式,class可以在多个元素中使用,HTML元素中class属性来设置class选择器,CSS中class选择器以"."来定义.
标签选择器:用于选择特定的HTML标签,如div,p,span等.
通配符选择器:用于选择所有元素,如*{}
后代选择器:用于选择特定元素的后代元素,如div span{}#以空格隔开,div标签下的所有span标签都会被选中.
子元素选择器:用于选择特定元素的直接子元素,如div > span{}#以>隔开,div标签下的所有一级子span标签都会被选中.
相邻兄弟选择器:用于选择特定元素的相邻兄弟元素,如div + p{}#以+隔开,div标签紧跟着的第一个p标签会被选中.
后续兄弟选择器:用于选择特定元素的后续兄弟元素,如div ~ p{}#以~隔开,div标签后面的所有p标签都会被选中.
伪类和伪元素:伪类和伪元素是CSS3中新增的概念,用于描述特殊的状态和选择器.伪类用于向某些选择器添加特殊的效果,如:hover、:active、:focus等.伪元素用于创建一些特殊的元素,如::before、::after等.

    CSS 创建
当读到一个样式表时,浏览器会根据它来格式化HTML文档.
外部样式表、内部样式表、内联样式:
外部样式表:在HTML文档的head部分通过link标签引入外部样式表,通过href属性指定样式表的路径.
内部样式表:在HTML文档的head部分通过style标签定义内部样式表,通过style标签定义的样式会覆盖外部样式表.
内联样式:在HTML元素的style属性中定义样式,通过style属性定义的样式会覆盖外部样式表和内部样式表.
多重样式:当两个或多个样式规则应用于同一个元素时,属性值将从更具体的样式表中被继承过来,后面的样式会覆盖前面的样式.
样式表优先级:内联样式>内部样式表>外部样式表>浏览器默认样式.
!important 规则例外当 !important 规则被应用在一个样式声明中时,该样式声明会覆盖CSS中任何其他的声明, 无论它处在声明列表中的哪里. 
使用 !important 不是一个好习惯，因为它改变了你样式表本来的级联规则，从而使其难以调试.


    CSS背景:
background-color:设置背景颜色;在body选择器中,颜色值可以用十六进制、RGB、颜色名来表示.
background-image:设置背景图片;默认情况下,背景图片进行平铺重复显示,覆盖整个元素实体.
background-repeat:设置背景图片的重复方式;默认情况下,背景图片进行平铺重复显示,repeat-x水平重复,repeat-y垂直重复,no-repeat不重复.
background-attachment:设置背景图片是否固定或者随着页面的其余部分滚动;
background-position:设置背景图片的位置;
简写属性:简化这些属性代码,将这些属性合并在同一个属性中,body{background:color url repeat attachment position;}

    CSS文本text:
color:设置文本颜色; 
text-align:设置文本的对齐方式;center居中,left左对齐,right右对齐，justify两端对齐.
text-decoration:设置文本的装饰,主要用于删除链接的下划线,如删除线line-through、下划线underline、上划线overline等.
text-transform:设置文本的大小写,如大写uppercase、小写lowercase、首字母大写capitalize.
text-indent:设置文本第一行的缩进.

    CSS字体font:
通用字体系列:拥有相似外观的字体组合系统,如Serif、Sans-Serif、Monospace等.
特定字体系列:如Times或Courier,这些字体系列有着独特的风格和感觉.
font-family:设置字体系列,可以设置多个字体,浏览器会按照顺序查找字体,如果第一个字体不存在或不支持,则会尝试下一个字体.多个字的名称必须用引号括起来,字体名称之间用逗号隔开.
font-style:字体样式,如正常normal、斜体italic、粗体bold、倾斜oblique.
font-size:字体大小,可以用px、em、pt等单位,px是像素单位,em是相对于父元素的字体大小,pt是磅值.
绝对大小、相对大小:如果不指定一个字体的大小,默认大小和普通文本段落一样16px=1em.
相对大小em可以和百分比配合使用,如font-size:1.2em;

    CSS链接:
链接的样式可以使用任何CSS属性,如颜色、背景、边框、字体等.
下面四个伪类用于设置链接的不同状态:
    a:link:默认样式,未访问的链接.
    a:visited:已访问的链接.
    a:hover:鼠标悬停在链接上时的样式.
    a:active:链接被点击时的样式.
删除超链接的下划线:text-decoration:none
设置背景颜色:background-color:blue;

    CSS 盒子模型
Box Model是CSS的核心,它定义了网页中的元素的大小、位置、边框、内边距、外边距等属性.
width:设置元素的宽度,可以用px、em、%等单位,百分比是相对于父元素的宽度.
height:设置元素的高度,
Margin:外边距,设置元素与元素之间的距离,没有背景,完全透明,四个方向可以单独设置.
border:边框,设置元素的边框.
padding:内边距,设置元素内容与元素边框之间的距离,当填充/内边距被清除时,所释放的区域将受到元素背景颜色的填充.
content:设置元素的内容,可以是文本、图像、视频等.

    CSS Border边框
Border用于定义元素边框的样式,border-width:边框宽度,border-style:边框样式,border-color:边框颜色.
border-style 有以下几种样式:none:无边框、solid:实线边框、dotted:点线边框、dashed:虚线边框...
border-width:边框宽度,可以用px、em、%等单位,百分比是相对于父元素的宽度.
border-color:边框颜色,可以用十六进制、RGB、颜色名来表示.
border-radius:设置元素的圆角半径,如果设置一个参数,则四个方向的圆角半径都相同,如果设置四个参数,则分别为左上、右上、右下、左下四个方向的圆角半径.
border:简写属性,用于把所有边框属性设置在一个声明中.边框可以单独设置各边,从上边框开始,顺时针方向为:top、right、bottom、left.


    CSS 填充padding
Padding用于设置元素内容与元素边框之间的距离,当填充/内边距被清除时,所释放的区域将受到元素背景颜色的填充.
padding:设置元素的内边距,可以用px、em、%等单位,百分比是相对于父元素的宽度.

    CSS 轮廓
轮廓（outline）是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用。
outline-width:轮廓宽度,outline-style:轮廓样式,outline-color:轮廓颜色.outline不占用空间,仅是视觉效果.

    CSS 定位position
元素可以使用的顶部，底部，左侧和右侧属性定位.这些属性无法工作,除非事先设定position属性.
static:默认值,元素按照正常文档流进行排列,top、bottom、left、right属性无效.
relative:相对定位,相对于元素本身的位置进行定位,top、bottom、left、right属性有效.配合使用top、bottom、left、right可以设置元素的位置.
absolute:绝对定位,相对于最近的已定位的祖先元素进行定位,如果祖先元素不存在,相对于body进行定位.
fixed:固定定位,相对于浏览器窗口进行定位,不随页面滚动而变化. Fixed定位的元素和其他元素重叠.不占用空间,仅是视觉效果.
sticky:粘性定位,相对于相对定位和固定定位的元素,当元素在屏幕范围内时,它的位置与相对定位和固定定位的元素相同,当元素滚出屏幕范围时,它的位置固定.
粘性定位的元素是依赖于用户的滚动,在 position:relative 与 position:fixed 定位之间切换.

    CSS 列表
CSS列表是HTML中用来组织内容的一种方式,包括有序列表、无序列表、自定义列表等.
ul:无序列表;列表项标记用特殊图形,如小黑点、小方框等
ol:有序列表;列表项的标记有数字或字母
li:列表项;
list-style-type:设置列表项标记的类型,如圆点disc、数字decimal、圆圈circle、方块square、自定义图片等.
list-style-image:设置列表项标记的图像.
list-style-position:设置列表项标记的位置
list-style-type:none 属性可以用于移除小标记.默认情况下列表 <ul> 或 <ol> 还设置了内边距和外边距，可使用 margin:0 和 padding:0 来移除

    CSS表格:
border:设置表格边框,border-width:边框宽度,border-style:边框样式,border-color:边框颜色.
border-collapse:设置表格边框是否合并,border-spacing:设置表格边框的间距.
text-align:设置表格内文本的水平对齐方式.center居中,left左对齐,right右对齐.
vertical-align:设置表格内单元格内容的垂直对齐方式.top顶端对齐,middle居中对齐,bottom底端对齐.

    CSS 尺寸Diomension
height:设置元素的高度,可以用px、em、%等单位,百分比是相对于父元素的高度.
width:设置元素的宽度
max-width:设置元素的最大宽度
min-width:设置元素的最小宽度
max-height:设置元素的最大高度
min-height:设置元素的最小高度

    CSS Display显示
块元素占用了全部宽度，在前后都是换行符.内边距、外边距、高度、宽度都可以设置.
行内元素/内联元素只占用它需要的宽度，不换行.高度、宽度、内边距的上下和外边距的上下都不可以设置.
display:设置元素的显示类型,如块级block、行内inline、表格table、列表list等.
display:none:隐藏元素,元素不会显示,会释放元素占用的空间.
visibility:设置元素的可见性,visible可见,hidden隐藏,collapse折叠.
visibility:hidden;不会释放元素占用的空间,但是元素仍然存在,只是看不见而已.
display:block;显示为块级元素.
display:inline;显示为行内元素.
display:inline-block;显示为行内块元素,同行显示并可修改宽高内外边距等属性.常将所有<li>元素加上display:inline-block样式，原本垂直的列表就可以水平显示了


    CSS Overflow溢出
overflow:设置元素内容溢出时是否显示滚动条,overflow 属性只工作于指定高度的块元素上.
visible默认值,,当内容溢出元素框时,会呈现在元素框之外.
hidden不显示滚动条,当内容溢出元素框时,内容会被裁切,溢出部分不会显示.
scroll显示滚动条,当内容溢出元素框时,会出现滚动条.
auto显示滚动条,当内容溢出元素框时,会自动出现滚动条.
inherit:继承父元素的overflow属性.


    CSS Float浮动
float:设置元素的水平方向的移动,left、right、none.
一个浮动元素会尽量向左或向右移动，直到它的外边缘碰到包含框或另一个浮动框的边框为止.浮动元素之后的元素将围绕它,浮动元素之前的元素将不会受到影响.
clear:设置元素的两侧不允许有浮动元素,left、right、both.
clear:both;可以防止元素的左右两侧有浮动元素,但是不能阻止中间的元素被浮动元素覆盖.

    CSS 对齐
text-align:设置元素内文本的水平对齐方式.center居中,left左对齐,right右对齐.
vertical-align:设置元素内文本的垂直对齐方式.top顶端对齐,middle居中对齐,bottom底端对齐.
margin:auto;可以让块元素内的图片水平居中.
垂直对齐:通过设置padding实现垂直居中.

    CSS 导航栏
垂直导航栏





CSS分组和嵌套:
CSS允许将样式分组和嵌套,通过分组可以将相关的样式定义在一起,通过嵌套可以创建层次化的样式.
分组:通过选择器的组合,可以将多个样式定义在一起,如h1,h2,h3{color:red;}
嵌套:通过选择器的嵌套,可以创建层次化的样式,如ul li{color:red;}   ul{margin:0;padding:0;}   li{list-style:none;}

CSS Disaplay:
display:设置元素的显示类型,如块级block、行内inline、表格table、列表list等.
display:none:隐藏元素,元素不会显示,但仍占用空间.
CSS Visibility:
visibility:设置元素的可见性,visible可见,hidden隐藏,collapse折叠.
visibility:hidden;display:none;是隐藏元素的两种方式,区别在于display:none;会释放元素占用的空间,而visibility:hidden;不会释放元素占用的空间,但是元素仍然存在,只是看不见而已.
