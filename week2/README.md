## Run from scratch

```bash
docker build --tag tagtag .
docker run -dit --name cName --mount type=bind,source="$(pwd)"/vol,target=/app/vol -e INPUT_DATA='/app/vol/starspace_input_file.txt' tagtag
docker exec -ti cName /bin/bash
```
## Additional commands

```bash
docker images ## images
docker rmi image_name
docker ps ## running containers
docker ps -a ## all containers
docker stop container_id_name ## stop containers
docker rm container_id_name ## remove containers
docker inspect smth ## meta info about smth
```
docker run --name cName --mount type=bind,source="$(pwd)"/vol,target=/app/vol -e INPUT_DATA='/app/vol/starspace_input_file.txt' tagtag --user "$(id -u):$(id -g)"

docker run -dit  --mount type=bind,source="$(pwd)"/vol,target=/app/vol -e INPUT_DATA='/app/vol/starspace_input_file.txt' tagtag

/app/Starspace/starspace train -trainFile "$INPUT_DATA" -model "/app/vol/modelSavedFile"

/app/Starspace/starspace train -trainFile "$INPUT_DATA" -model "/app/vol/modelSavedFile"




docker build --tag tagtag --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .
docker run --mount type=bind,source="$(pwd)"/vol,target=/app/vol -e INPUT_DATA="/app/vol/starspace_input_file.txt" tagtag


docker ps -a | awk '{print $1}' | xargs docker stop 
docker ps -a | awk '{print $1}' | xargs docker rm 
docker rmi tagtag



# ENTRYPOINT ["/app/Starspace/starspace"]
CMD "/app/Starspace/starspace train -trainFile $INPUT_DATA -model /app/vol/modelSavedFile"