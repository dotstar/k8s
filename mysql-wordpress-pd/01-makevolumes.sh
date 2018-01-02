#!/bin/bash -x
kubectl create -f local-volumes.yaml
kubectl get pv

