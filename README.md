# python-teaching

This is a python learning route teaching project

# python开发

## 开发环境选择

目前最新稳定本版为python3.10
具体版本的 Python 环境可以在[官网](https://www.python.org/)下载。

## 开发工具

推荐使用 [pycharm](https://www.jetbrains.com/pycharm/)，可以选择免费的社区版本。
[Visual Studio Code](https://code.visualstudio.com/) 是微软开发的一款免费轻量级文本编辑器，通过安装插件可以自定义成一款功能强大的
IDE 开发工具。目前支持 Python 的插件体系已经较为完善，此方案也可以作为备用。

## 交互式python命令行工具 [ipython](https://ipython.org/)

在本地开启 python shell 时会受到无法自动联想补全的困扰，因此在交互调试等情况下，可以使用 `ipython` 命令行工具。

* 安装命令

```base
pip install -U ipython
```

* 进入 ipython shell
  在命令行执行 `ipython` 即可。

# 注意事项

## pycharm 使用

无论什么语言在编写过程中都要遵循一定的代码风格规范，在pycharm中可以使用快捷键 `ctrl + alt + L` 可以快速格式化代码。

## 基础

### 基本数据类型

### 变量

* 局部变量
* 全局变量

### 简单函数

### 输入输出函数

## [python标准库](https://docs.python.org/zh-cn/3/library/index.html)

### `except Exception as exc `捕获的异常太广泛了这种操作可以用在如下情况：

* 当你不确定它会出现什么异常，单又不希望程序挂掉的时候。但捕获后，应该使用 `logging.exception(ex)` 将异常堆栈显示出来，方便以后根据堆栈调试信息。

* 在逻辑最外层捕获顶级异常，但需要使用 `traceback.print_exc()` 将异常堆栈打印到控制台。这种在命令行程序的最外层可以使用。

* 其他情况应避免直接捕获 Exception 异常，而是捕获具体需要处理的异常。至于没有捕获到，那程序出错后，再进行问题修复即可

