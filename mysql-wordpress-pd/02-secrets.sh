#!/bin/bash -x
kubectl create secret generic mysql-pass --from-literal=password=b@dp@ss
kubectl get secrets
