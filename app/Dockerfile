# 使用官方的 Python 基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到工作目录中
COPY . /app

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 默认的运行端口
EXPOSE 5000

# 运行 Flask 应用
CMD ["flask", "run", "--host=0.0.0.0"]
