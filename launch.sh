#!/bin/sh

sudo docker image build -t flask_docker .

sudo docker run -it -p 5066:5066 --name flaskmuhehehe -d flask_docker