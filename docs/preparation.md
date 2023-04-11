# 技术准备

## 开发环境搭建

本项目使用 python3.10/3.11。具体版本的python环境可以在 [官网](https://www.python.org/downloads/) 自行下载。

## IDE使用

推荐使用 [Pycharm](https://www.jetbrains.com/pycharm/) 开发工具，初学者页可以选择免费的社区版本 (Professional)。

## 虚拟环境使用

> 在Python开发中使用虚拟环境（Virtual Environment）可以帮助开发者更好地管理项目依赖和避免冲突。
>
> 当我们在本地安装了多个Python库和依赖时，这些库可能会相互冲突，导致程序无法正常工作。
>
> 使用虚拟环境可以解决这个问题，因为每个虚拟环境都有自己独立的Python解释器和依赖，不会干扰其他虚拟环境或本地Python环境。

本项目中推荐使用 `poetry`，该工具既包含虚拟环境管理也支持打包发布等功能。

在安装好 Python 环境后，在全局环境中安装 poetry

```bash
# 安装最新版本的pip工具
python -m pip install -U pip
# 安装 poetry 
pip install -U poetry 
```

poetry 的详细命令可以到其 [官方](https://python-poetry.org/) 查看

## git 使用

> Git是一个开源的项目管理平台，它可以帮助团队协作开发，管理代码版本和跟踪代码变化。
> 在软件开发中，Git被广泛使用，特别是在开源项目和大型项目中。

为了方便大家理解，建议在使用命令行来操作 git

- gitbash 安装 （git 命令行工具）


