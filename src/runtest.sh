#!/bin/bash
echo "running docker"
docker run \
  -e MYSQL_ROOT_PASSWORD=example \
  -e MYSQL_DATABASE=automation \
  -e MYSQL_USER=admin \
  -e MYSQL_PASSWORD=example \
  -p 3306:3306 \
  -d mysql
echo "sleep 30"
sleep 30
pytest .