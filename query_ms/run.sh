#!/usr/bin/env bash

CONTAINER_NAME="ctrue-query"

docker build -t ${CONTAINER_NAME} .

docker container ls -a

docker stop ${CONTAINER_NAME}

#docker run --rm -d --name ${CONTAINER_NAME} -p 80:80 $CONTAINER_NAME
docker run --name ${CONTAINER_NAME}
