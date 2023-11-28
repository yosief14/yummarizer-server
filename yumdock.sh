#!/bin/bash
#build docker image
docker build --tag yummarizer-server .
#run docker image
docker run -p 5000:5000 yummarizer-server