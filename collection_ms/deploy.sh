CONTAINER_NAME="collection"

docker build -t $CONTAINER_NAME .

docker container ls -a

docker stop $CONTAINER_NAME
docker_id=$(docker container ls -a | grep $CONTAINER_NAME | cut -d' ' -f1)

echo $docker_id
docker container rm $docker_id

docker run -d --name $CONTAINER_NAME -p 80:80 $CONTAINER_NAME
