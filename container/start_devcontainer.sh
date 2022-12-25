set -e

DOCKER_TAG=adventofcode22:latest
WORKING_DIR=/adventofcode22
ENTRYPOINT="bash"

docker build \
    .. \
    -f Dockerfile \
    -t $DOCKER_TAG

docker run \
    -it \
    --rm \
    --entrypoint bash \
    -v $(pwd)/..:$WORKING_DIR \
    -w $WORKING_DIR \
    adventofcode22:latest \
    container/on_start.sh
