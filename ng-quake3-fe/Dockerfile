#STAGE 1: Build ###

# We label our stage as ‘builder’
FROM node:10-alpine as builder

RUN apk --no-cache add git && \
    git clone https://github.com/random-dwi/q3-server-docker-webUI-angular ./ng-app


WORKDIR /ng-app

## Storing node modules on a separate layer will prevent unnecessary npm installs at each build

RUN npm ci && \
    npm run ng build -- --prod --output-path=dist  && \
    pwd

### STAGE 2: Setup ###

FROM nginx:1.14.1-alpine

## Copy our default nginx config
COPY nginx/*.conf /etc/nginx/conf.d/

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

## From ‘builder’ stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder /ng-app/dist /usr/share/nginx/html

## copy map images
COPY map-images/*.jpg /usr/share/nginx/html/assets/images/

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
