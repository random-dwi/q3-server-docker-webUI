#STAGE 1: Build ###

# We label our stage as ‘builder’
FROM node:10-alpine

WORKDIR /var/

RUN apk --no-cache add git && \
    git clone https://github.com/random-dwi/q3-server-docker-rest-api  && \
    cd ./q3-server-docker-rest-api/ && \
    npm ci && \
    npm run build

WORKDIR /var/q3-server-docker-rest-api/

ENV Q3SERV_HOST quake3
ENV Q3SERV_PASS secret
ENV Q3LOG_FILE logs/server.log

EXPOSE 9009
CMD ["npm", "start"]
