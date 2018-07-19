PORT=8080
WWW_ROOT=/usr/src/app
VERSION=latest
PYTHON_VERSION=3.6.5

build:
	docker build -t kirtivr/parkinator .

run:
	docker run --rm --name parkinator -d -p $(PORT):$(PORT) kirtivr/parkinator
