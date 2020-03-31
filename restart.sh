#!/bin/sh

docker-compose down

python3 parse_maps.py ./map-download/maps . ng-quake3-fe/map-images

docker-compose build
docker-compose up -d
