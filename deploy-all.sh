#!/bin/bash

echo "=========================================="
echo " Cloud Event Platform Deployment Script"
echo "=========================================="

set -e

echo ""
echo "Cleaning previous deployment archives..."

find ~/cloud-event-platform -name "*.tar" -delete

PROJECT_DIR=~/cloud-event-platform

##############################################
# Event Service (Blue-Green)
##############################################

echo ""
echo "===== Deploying Event Service (Blue-Green) ====="

cd $PROJECT_DIR/event-service

sudo docker build -t event-service:latest .
sudo docker save event-service:latest -o event-service.tar
sudo k3s ctr images import event-service.tar

sudo kubectl apply -f kubernetes/event-blue-deployment.yaml
sudo kubectl apply -f kubernetes/event-green-deployment.yaml
sudo kubectl apply -f kubernetes/event-service-bluegreen.yaml

sudo kubectl rollout restart deployment/event-service-blue
sudo kubectl rollout restart deployment/event-service-green

##############################################
# Program Service
##############################################

echo ""
echo "===== Deploying Program Service ====="

cd $PROJECT_DIR/program-service

sudo docker build -t program-service:latest .
sudo docker save program-service:latest -o program-service.tar
sudo k3s ctr images import program-service.tar

sudo kubectl apply -f kubernetes/program-deployment.yaml
sudo kubectl rollout restart deployment program-service

##############################################
# Registration Service
##############################################

echo ""
echo "===== Deploying Registration Service ====="

cd $PROJECT_DIR/registration-service

sudo docker build -t registration-service:latest .
sudo docker save registration-service:latest -o registration-service.tar
sudo k3s ctr images import registration-service.tar

sudo kubectl apply -f kubernetes/registration-deployment.yaml
sudo kubectl rollout restart deployment registration-service

##############################################
# Analytics Service
##############################################

echo ""
echo "===== Deploying Analytics Service ====="

cd $PROJECT_DIR/analytics-service

sudo docker build -t analytics-service:latest .
sudo docker save analytics-service:latest -o analytics-service.tar
sudo k3s ctr images import analytics-service.tar

sudo kubectl apply -f kubernetes/analytics-deployment.yaml
sudo kubectl rollout restart deployment analytics-service

##############################################
# Frontend
##############################################

echo ""
echo "===== Deploying Frontend ====="

cd $PROJECT_DIR/frontend

sudo docker build -t frontend:latest .
sudo docker save frontend:latest -o frontend.tar
sudo k3s ctr images import frontend.tar

sudo kubectl apply -f kubernetes/frontend-deployment.yaml
sudo kubectl rollout restart deployment frontend

##############################################
# Dashboard Service
##############################################

echo ""
echo "===== Deploying Dashboard Service ====="

cd $PROJECT_DIR/dashboard-service

sudo docker build -t dashboard:latest .
sudo docker save dashboard:latest -o dashboard.tar
sudo k3s ctr images import dashboard.tar

sudo kubectl apply -f kubernetes/dashboard-deployment.yaml
sudo kubectl apply -f kubernetes/dashboard-service.yaml

sudo kubectl rollout restart deployment dashboard

##############################################
# Wait for Rollout
##############################################

echo ""
echo "===== Waiting for Deployments ====="

sudo kubectl rollout status deployment/event-service-blue
sudo kubectl rollout status deployment/event-service-green
sudo kubectl rollout status deployment/program-service
sudo kubectl rollout status deployment/registration-service
sudo kubectl rollout status deployment/analytics-service
sudo kubectl rollout status deployment/frontend
sudo kubectl rollout status deployment/dashboard

echo ""
echo "Starting Blue-Green switch..."

$PROJECT_DIR/switch-event-service.sh

echo ""

##############################################
# Summary
##############################################

echo ""
echo "===== Pods ====="

sudo kubectl get pods

echo ""
echo "===== Services ====="

sudo kubectl get services

echo ""
echo "==============================================="
echo " Cloud Event Platform Deployment Successful!"
echo "==============================================="

echo ""
echo "Services:"
echo "  Frontend      : http://13.233.81.248:30083"
echo "  Dashboard     : http://13.233.81.248:30086"
echo "  Event API     : http://13.233.81.248:30081/docs"
echo "  Program API   : http://13.233.81.248:30082/docs"
echo "  Registration  : http://13.233.81.248:30084/docs"
echo "  Analytics API : http://13.233.81.248:30085/docs"
echo "  Metabase      : http://13.233.81.248:30087"
echo "  Prometheus    : http://13.233.81.248:30089"
echo "  Grafana       : http://13.233.81.248:30090"
echo ""
echo "Deployment completed."
