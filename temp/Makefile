PORT=9090
WWW_ROOT=/usr/src/app

build:
	docker build -t kirtivr/alexa .

run:
	docker run --name alexator --mount source=/home/ec2-user/.aws,target=/root/.aws -p $(PORT):9090 kirtivr/alexa
