PORT=8080
WWW_ROOT=/usr/src/app
VERSION=latest
PYTHON_VERSION=3.6.5

build:
	docker build -t kirtivr/parkinator .

run:
	docker run --name parkinator -p $(PORT):$(PORT) kirtivr/parkinator
