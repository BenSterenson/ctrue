CONTAINER_NAME="collection"

docker build -t $CONTAINER_NAME .

docker container ls -a

docker stop $CONTAINER_NAME

docker run --rm --name $CONTAINER_NAME -p 80:80 $CONTAINER_NAME
