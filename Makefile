PORT=8080
WWW_ROOT=/usr/src/app
VERSION=latest
PYTHON_VERSION=3.6.5

build:
	docker image build $(BUILD_ARGS) -f Dockerfile .

run:
	docker container run --rm -p $(PORT):$(PORT)
