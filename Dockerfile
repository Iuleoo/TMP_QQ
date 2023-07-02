# 使用Python 3作为基础镜像
FROM python:3

# 将main.py复制到容器中的/app目录
COPY main.py /app/main.py

# 设置工作目录为/app
WORKDIR /app

# 安装所需的依赖项
RUN pip install requests flask

# 指定容器启动时运行的命令
CMD ["python", "main.py"]
