# 日常记录

## 开发总结

### opencv在docker环境下安装异常问题

* 构建docker后，运行报错：`ImportError: libGL.so.1: cannot open shared object file: No such file or directory`

  opencv在docker环境下使用无需 GUI 库依赖项，
  所以使用 `pip install opencv-python-headless`  [无头主模块包](https://pypi.org/project/opencv-python-headless/)
  或 `opencv-contrib-python-headless`Headless 完整包 安装

### 开启MySQL容器

```bash
docker run -e MYSQL_ROOT_PASSWORD=[password] -e MYSQL_DATABASE=[database] -p 3307:3306 --network db --name mysql mysql:debian
```

### docker-compose

```bash
docker compose build
docker compose up
```

### tox测试中，使用 `pytest cov` 语句实现返回覆盖率

```bash
poetry run pytest tests -ra -q --cov=src --cov-report=term-missing --cov-report=html
```

### 基于本地项目目录开启docker容器

```bash
docker run -it --rm -v %cd%:/app --name demo python:3.10 bash 
```
