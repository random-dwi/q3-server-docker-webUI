#STAGE 1: Build ###

# We label our stage as ‘builder’
FROM node:10-alpine

WORKDIR /var/

RUN apk --no-cache add git && \
    git clone https://github.com/random-dwi/q3-server-docker-mattermost-webhook  && \
    cd ./q3-server-docker-mattermost-webhook/ && \
    npm install

WORKDIR /var/q3-server-docker-mattermost-webhook/

ENV REST_API_HOST ng-quake3-be
ENV REST_API_PORT 9009

CMD ["npm", "start"]
