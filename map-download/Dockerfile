FROM nginx:1.14.1-alpine

## Copy our default nginx config
COPY nginx/*.conf /etc/nginx/conf.d/

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

## From ‘builder’ stage copy over the artifacts in dist folder to default nginx public folder
COPY maps/*.pk3 /home/q3a/baseq3/

EXPOSE 9090

CMD ["nginx", "-g", "daemon off;"]
