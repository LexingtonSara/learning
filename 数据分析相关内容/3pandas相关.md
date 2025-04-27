Pandas的应用:
pandas可以从各种文件格式比如CSV、Excel、SQL、JSON等读取数据,也可以将数据写入到各种文件格式.
pandas可以对各种数据进行运算操作,比如排序、过滤、聚合等.广泛应用在学术、金融、统计学、数据科学等领域.
Pandas是数据分析的利器,不仅提供了高效、灵活的数据结构,还能以极低的成本完成复杂的数据操作和分析任务.
- 数据清洗与预处理:处理缺失值、异常值、重复值、空值等,进行数据类型转换、字符串操作等.
- 数据操作与分析:支持高效的数据选择、筛选、切片、按条件提取数据、合并、连接多个数据集、数据分组、汇总统计等操作.进行复杂的数据变换如数据透视表、交叉表、时间序列分析等.
- 数据读取与导出:支持多种文件格式的读取,包括CSV、Excel、SQL、JSON等,还支持将数据写入到各种文件格式.
- 数据可视化:通过matplotlib和其他可视化工具的集成,可以快速生成折线图、柱状图、散点图等常见图表.
- 时间序列分析:支持强大的时间序列处理功能,包括日期的解析、重采样、时区转换等.

数据结构:主要有Series、DataFrame、Panel三种数据结构.
Series:一种类似于一维数组的对象,由一组数据(数值、字符串、布尔值、各种numpy数据类型)以及与之相关的索引组成.
DataFrame:二维的表格型数据结构,含有一组有序的列,每列可以是不同的值类型(数值、字符串、布尔值),可以看成由Series组成的字典.既有行索引也有列索引.
Panel:三维数据结构,可以理解为由DataFrame组成的字典.

DataFrame由index、key、value三种数据结构组成.
index:行索引,用于标识DataFrame中的行,可以是数字、字符串、日期等.
key:列索引,用于标识DataFrame中的列,可以是数字、字符串、日期等.
value:数据值,可以是数值、字符串、布尔值等.

series在使用字典创建时,key作为index,value作为value.
dataframe在使用字典创建时,key作为列名,value作为Series.

CSV文件(逗号分隔值文件comma-separated values file):一种常见的文本文件,由纯文本形式存储表格数据,以纯文本形式存储数据,以逗号分隔值(CSV)格式存储.
- 读取CSV文件:使用pandas.read_csv()函数读取CSV文件.
pd.read_csv(filepath_or_buffer,sep,header,names,dtype,index_col)
- filepath_or_buffer:文件路径或文件对象.
- sep:分隔符,默认是逗号.
- header:行索引所在行的位置,默认是0.
- names:列名列表,默认是文件第一行的列名.可以用该参数指定列名.
- dtype:数据类型字典,用于指定列的类型.
- index_col:列索引,默认是None.
直接读取CSV文件,默认会将第一行作为列名,第一列作为行索引.直接用print()函数打印只会显示前5行和后5行.其他数据以省略号表示.要想显示全部数据,可以使用print(df.to_string())函数.

- 写入CSV文件:使用pandas.DataFrame.to_csv()函数写入CSV文件.
DataFrame.to_csv(path_or_buf,sep,index,columns,header,encoding,mode)
- path_or_buf:文件路径或文件对象.
- sep:分隔符,默认是逗号.
- index:是否写入行索引,默认是True.
- columns:指定列名列表,默认是None.
- header:是否写入列名,默认是True.
- encoding:编码格式,默认是utf-8.
- mode:写入模式,默认是w.

Excel文件:一种常见的表格文件,由微软公司开发,支持多种数据类型,包括数字、文本、日期、布尔值等.
- 读取Excel文件:使用pandas.read_excel()函数读取Excel文件.
pd.read_excel(io,sheet_name,header,names,index_col,usecols,dtype)
- io:文件路径或文件对象.
- sheet_name:工作表名称,默认是0.即第一个工作表.
- header:指定用做列名的行,默认是0.即第一行.
- names:列名列表,默认是文件第一行的列名.可以用该参数指定列名.
- index_col:指定用做行索引的列,默认是None.
- usecols:指定读取的列名或列索引,默认是None.
- dtype:数据类型字典,用于指定列的类型.

- 写入Excel文件:使用pandas.DataFrame.to_excel()函数写入Excel文件.
DataFrame.to_excel(excel_writer,sheet_name,startrow,startcol,header,index,index_label)
- excel_writer:文件路径或文件对象.
- sheet_name:工作表名称,默认是'Sheet1'.
- startrow:写入起始行,默认是0.
- startcol:写入起始列,默认是0.
- header:是否写入列名,默认是True.
- index:是否写入行索引,默认是True.
- index_label:行索引标签,默认是None.

如果将一个DataFrame写入Excel文件的多个工作表,可以用ExcelWriter()函数来实现.
ExcelWriter()是pandas提供的写入Excel文件的类,可以将多个DataFrame或者Series写入同一个Excel文件.
```python
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')
```
这样可以将df1写入Sheet1,df2写入Sheet2.

加载excel文件:ExcelFile()是pandas提供的读取Excel文件的类,可以处理多个表单,并在不重新打开文件的情况下访问其中的数据.
```python
excel_file = pd.ExcelFile('example.xlsx')
print(excel_file.sheet_names)  # 输出所有表单的名称
df1 = excel_file.parse('Sheet1')  # 读取表单1的数据
excel_file.close()  # 关闭文件
```

JSON文件相关操作:
- 读取JSON文件:使用pandas.read_json()函数读取JSON文件.
pd.read_json(path_or_buf,orient,dtype,convert_axes,convert_dates,keep_default_dates)
- path_or_buf:文件路径或文件对象,或者是URL.
- orient:JSON数据的格式,默认是'columns'.
- dtype:数据类型字典,用于指定列的类型.
- convert_axes:是否将轴转换为核实的数据类型,默认是True.
- convert_dates:是否将日期字符串转换为日期类型,默认是True.
- keep_default_dates:是否保留默认日期类型,默认是True.

JSON数据如果是嵌套的,可以用pd.json_normalize()函数将其转换为DataFrame.
pd.json_normalize(data,record_path,meta,meta_prefix,sep)
- data:JSON数据.
- record_path:JSON数据的记录路径,默认是None.在嵌套的情况下显示指定的路径下的JSON数据.
- meta:元数据,默认是None.meta参数以字典形式用于指定需读取的JSON数据,可以以列表的形式指定多个元数据,可以在列表内一层一层显示嵌套的层级,显示指定路径下的JSON数据.

将DataFrame写入JSON文件:使用pandas.DataFrame.to_json()函数写入JSON文件.
DataFrame.to_json(path_or_buf,orient,date_format,double_precision,force_ascii,date_unit,default_handler,lines)
- path_or_buf:文件路径或文件对象.默认是None,返回JSON字符串.
- orient:JSON数据的格式,默认是'columns'.
- date_format:日期格式,默认是None.
- default_handler:自定义处理非标准类型的处理函数,默认是None.
- lines:是否将每行数据作为一行输出,默认是False.



Pandas数据清洗:
数据清洗时对一些没有用的数据进行处理的过程,数据集可能存在数据缺失、数据格式错误、数据错误、数据重复等问题,需要对数据进行清洗,以便进行后续的分析和处理.

数据清洗的步骤:
1. 缺失值处理:识别并填补缺失值,或删除含缺失值的行或列.
2. 重复数据处理:检查并删除重复数据.确保每条数据唯一.
3. 异常值处理:识别并删除异常值,或将异常值替换为合理值.
4. 数据格式转换:转换数据类型或进行单位转换,如日期格式转换.
5. 标准化与归一化:对数值型数据进行标准化或归一化.
6. 类别数据编码:将类别变量转换为数值形式,如将性别、职业等转换为数值.
7. 文本处理:对文本数据进行清洗,如去除停用词、词干化、分词等.
8. 数据抽样:从数据集中抽取样本,或通过过采样或欠采样处理类别不平衡问题.
9. 特征工程:创建新特征、删除不相关的特征、选择重要特征等.

清洗空值:
- 使用dropna()函数删除含有缺失值的行或列.
DataFrame.dropna(axis=0,how='any',thresh=None,subset=None,inplace=False)
- axis:0表示行,1表示列.
- how:any表示只要含有缺失值,就删除该行或列.all表示全部缺失才删除该行或列.
- thresh:指定缺失值个数的阈值,超过该阈值才删除该行或列.
- subset:指定需要检查的列名列表,默认是None,表示检查所有列.
- inplace:是否在原数据上修改,默认是False.

- 使用fillna()函数填补缺失值.
DataFrame.fillna(value=None,method=None,axis=None,inplace=False,limit=None,downcast=None)
- value:指定填充值,默认是None,表示用0填充.
- method:指定填充方式,默认是None,表示用前一个值填充.
- axis:0表示行,1表示列.
- inplace:是否在原数据上修改,默认是False.
- limit:指定填充的最大次数,默认是None,表示填充所有缺失值.
- downcast:指定数据类型,默认是None,表示保持原数据类型.

替换空单元格的常用方法是计算列的均值、中位数、众数等,然后用该值填充空单元格.分别使用mean()、median()、mode()函数实现.

Pandas清洗重复数据:
pandas.DataFrame.duplicated()函数可以检查数据集中是否存在重复数据,返回布尔值Series,True表示重复,False表示不重复.
pandas.DataFrame.drop_duplicates()函数可以删除重复数据,默认保留第一次出现的行,可以设置keep='first'或'last'参数保留最后一次出现的行.

Pandas相关性分析:
相关性表示两个或多个变量之间的关系强度和方向,根据相关性的值,可以判断变量之间的关系.正相关、负相关、无相关性三种.
- 计算相关性:使用pandas.DataFrame.corr()函数计算相关性.
DataFrame.corr(method='pearson',min_periods=1)
- method:相关性计算方法,默认是'pearson',可选'kendall'、'spearman'.
- min_periods:计算相关系数时所需的最小观测值数量,默认是1.即只少有一个非空值才会计算相关系数.
df.corr()返回的是一个相关系数矩阵,矩阵的行和列对应数据框的列名,矩阵的元素为对应列之间的相关系数.
常见的相关系数：
- 皮尔逊相关系数(Pearson correlation coefficient):衡量两个变量之间的线性相关关系,取值范围[-1,1],值越接近1,表示两个变量正相关,值越接近-1,表示两个变量负相关,值接近0,表示无相关性.