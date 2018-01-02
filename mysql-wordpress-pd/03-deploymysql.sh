#!/bin/bash -x
# export MYSQL_ROOT_PASSWORD=b@dp@ss
kubectl create -f mysql-deployment.yaml
kubectl get pods
