#!/usr/bin/env bash

docker logs -f test tee output.log | sudo tee file.txt
