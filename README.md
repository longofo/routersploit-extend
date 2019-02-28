## 如何使用



1. `git clone https://github.com/threat9/routersploit.git`

   `git clone https://github.com/longofo/routersploit-extend.git`

2. 将`routersploit-extend`目录下的`extsploit`放到`routersploit/routersploit/`目录下

3. 将`routersploit-extend`目录下的`testexploits`放到`routersploit/routersploit/modules`目录下，`testexploits`放的是几个使用了该扩展的demo的例子

demo演示：

[![](https://asciinema.org/a/xa8r6PhxwtGw87Osyk52GFpZC)](https://asciinema.org/a/xa8r6PhxwtGw87Osyk52GFpZC)



## 说明



1. `extsploit/exploit/client`放的是`routersploit`编写`exploit`需要继承的父类，像`testexploits`中的例子一样

   可以自己编写其他`client`，需要继承`extsploit.exploit.client.BaseClient`，在编写`exploit`是导入自己编写的`client`然后继承

2. `extsploit/exploit/option`是`exploit`中附加的Option选项

   可以自己编写特有的Option选项

3. `extsploit/exploit/resuest`是对`requests`模块做了`patch`

4. `extsploit/exploit/save`是保存运行结果的模块，我写了一个`file.py`，表示保存到`file`

   可以自己编写特有的`Save`模块，比如要存到`mongodb`，

   可以建一个`mongodb.py`文件，可参照`file.py`编写

5. `extsploit/exploit/search`是搜索模块，用于加载多个目标

   可以自己编写特有的`Search`模块，比如要存到从`google`加载，

   可以建一个`google.py`文件，可参照`zoomeye.py`编写

6. 所有外部需要使用的东西在`extsploit/__init__.py`中导入就行了


**注:**

1. 如果在`exploit`编写时使用了`routersploit`提供的`multi`装饰器，那么就不要使用`extsploit`中的东西
2. 每个`exploit`的`run/check`方法需要返回一个`dict`,为空表示失败,如果返回有内容表示成功，可参照`testexploits`中的例子
