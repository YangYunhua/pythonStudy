# 更新日志

### 2016.09.27
- 尝试为api接口增加加密模式
- 重构请求的方法装饰器的构成方式，添加put和delete装饰器

### 2016.09.22
- 添加谷歌验证页

### 2016.08.31
- 添加请求生命周期流程图

### 2016.08.28
- 更改bootstrap模板的样式

### 2016.08.27
- 修正bootstrp首页的html的代码结构

### 2016.08.10
- 封装重构User类方法`signin`、`signout`、`verify_password`
- 封装重构`check_xxx`函数

### 2016.07.26
- 实现首页文章的摘要显示

### 2016.07.23
- 在网站右下角添加回到页顶的图标（只有滚动超过一个屏幕高度才是可见的）

### 2016.07.22
- uikit导航栏固定顶部
- markdown实现GFM式的换行（标准md语法是末尾加两个空格再回车才是换行，GFM是直接回车就是换行了）
- 修复管理页面分页导航的bug

### 2016.07.14
- 更换markdown渲染库为mistune
- php语言可以自动识别高亮，要以`<?php`开头
- **基本所有编程语言都可以高亮显示**，只要<kbd>\`\`\`(lang)\n(code)\n\`\`\`</kbd>包裹的话

### 2016.07.03
- 点击图标跳转到另一个模板的同页面，而不再是跳转到另一个模板的首页

### 2016.07.02
- 修得管理页面表格文字溢出的问题
- 修复了在搜狗浏览器无法给导航栏添加高亮样式的问题

### 2016.07.01
- 修复uikit登陆页面表单在移动端溢出的问题
- uikit导航栏在移动端时用图标代替文字
- 完成uikit风格的管理页面
- 完成uikit风格的博客编辑页面
- 修正js的this变量，统一命名为self

### 2016.06.30
- 修复导航栏点击<kbd>manage</kbd>不会高亮的问题
- 重写uikit模板
- 完成uikit风格的主页
- 完成uikit风格的博客页面
- 完成uikit风格的注册页面
- 完成uikit风格的登陆页面
- **添加导航栏图标切换bootstrap模板和uikit模板的功能**