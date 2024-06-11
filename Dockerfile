# 使用官方的 Node.js 镜像
FROM node:16

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 package-lock.json
COPY package*.json ./

# 安装前端依赖
RUN npm install

# 复制前端项目所有文件到工作目录
COPY . .

# 构建前端项目
RUN npm run build

# 使用 Nginx 作为前端服务器
FROM nginx:1.21
COPY --from=0 /app/dist /usr/share/nginx/html

# 暴露 Nginx 默认的运行端口
EXPOSE 80

# 运行 Nginx
CMD ["nginx", "-g", "daemon off;"]
