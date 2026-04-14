FROM nginx:alpine
COPY --chmod=644 index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/templates/default.conf.template
