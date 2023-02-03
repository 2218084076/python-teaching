# 日常记录

---

## 教学任务

python 应用

- [ ]  api、web 开发
- [ ]  自动化
- [X]  数据采集
- [ ]  数据分析

### 2023 02 11

- git 基本安装使用

    - 了解并完成 git `push` `commint` `pull`等基本操作 方便以后教学进行
    -
- 开发工具介绍

    - 开发中使用`poetry`虚拟环境
    - 项目中引用了`pylint` `isort` 代码规范
- python 基础梳理

---

## 开发总结

### opencv 在 docker 环境下安装异常问题

- 构建 docker 后，运行报错：`ImportError: libGL.so.1: cannot open shared object file: No such file or directory`

  opencv 在 docker 环境下使用无需 GUI 库依赖项，
  所以使用 `pip install opencv-python-headless` [无头主模块包](https://pypi.org/project/opencv-python-headless/)
  或 `opencv-contrib-python-headless`Headless 完整包 安装

### 开启 MySQL 容器

```bash
docker run -e MYSQL_ROOT_PASSWORD=[password] -e MYSQL_DATABASE=[database] -p 3307:3306 --network db --name mysql mysql:debian
```

### docker-compose

```bash
docker compose build
docker compose up
```

### tox 测试中，使用 `pytest cov` 语句实现返回覆盖率

```bash
poetry run pytest tests -ra -q --cov=src --cov-report=term-missing --cov-report=html
```

### 基于本地项目目录开启 docker 容器

```bash
docker run -it --rm -v %cd%:/app --name demo python:3.10 bash
```
