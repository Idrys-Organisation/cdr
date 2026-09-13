FROM nginx:alpine
COPY --chmod=644 index.html favicon.svg robots.txt /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/templates/default.conf.template
