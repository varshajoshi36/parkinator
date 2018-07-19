PORT=8080
WWW_ROOT=/usr/src/app
VERSION=latest
PYTHON_VERSION=3.6.5
IMAGE=
build:
	docker image build $(BUILD_ARGS) -t $(IMAGE):$(VERSION) -f docker/webserver/Dockerfile .

run:
	docker container run --rm -p $(PORT):$(PORT)
