# 勘误网开发日志

## 初衷
出版物中难免会出现一些勘误，而当我发现它们的时候，

- 我发现根本无处核实它们。
- 即使有，也只是部分书籍提供了类似帖子性质的勘误表。没有一个专门收集勘误的地方，让你可以报告自己发现的勘误。
所以，我希望能够建设这样一个网站，使用类似维基模式的方式来收集勘误。

## v0.0.1
### 需求

1. 可以新建勘误本
1. 可以浏览勘误本标题
1. 可以查看勘误本内容
1. 可以修改勘误本内容

暂时不需要实现的需求：

1. 无账号，无权限
2. 勘误内容纯文本，无格式
3. 无历史
4. 不检查编辑冲突
5. 无导航、无搜索、无翻页
6. 无CSS美化

### 实现
**需要：**

1. Python2.7.9
2. django1.8.0
3. sqlite3

**注意：**
仅在开发阶段使用sqlite数据库，我是真的想实现一个勘误网站，而不是作为一个练习，所以任何与建设一个勘误网站无关的内容我都不想涉及，例如：

1. wsgi服务器
2. 数据库
3. url分发
4. 数据库访问

**url设计：**
``` Python
url(r'^$', views.index, name='index'),
url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
url(r'^(?P<pk>[0-9]+)/edit_form/$', views.edit_form, name='edit_form'),
url(r'^save', views.save, name='save'),
url(r'^add_form/$', views.add_form, name='add_form'),
url(r'^add/$', views.add),
```

**模型设计：**
``` Python
class Corrigendum:
    title = models.CharField(max_length=200)
    text = models.TextField()
```