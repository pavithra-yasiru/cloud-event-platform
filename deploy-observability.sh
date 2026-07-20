#!/bin/bash

echo "==============================================="
echo " Cloud Event Platform - Observability Deployment"
echo "==============================================="

set -e

PROJECT_DIR=~/cloud-event-platform

##############################################
# Monitoring Namespace
##############################################

echo ""
echo "===== Creating Monitoring Namespace ====="

sudo kubectl apply -f $PROJECT_DIR/observability/namespace.yaml

##############################################
# Prometheus
##############################################

echo ""
echo "===== Deploying Prometheus ====="

sudo kubectl apply -f $PROJECT_DIR/observability/prometheus/kubernetes/prometheus-configmap.yaml
sudo kubectl apply -f $PROJECT_DIR/observability/prometheus/kubernetes/prometheus-deployment.yaml
sudo kubectl apply -f $PROJECT_DIR/observability/prometheus/kubernetes/prometheus-service.yaml

##############################################
# Grafana
##############################################

echo ""
echo "===== Deploying Grafana ====="

sudo kubectl apply -f $PROJECT_DIR/observability/grafana/kubernetes/grafana-pvc.yaml
sudo kubectl apply -f $PROJECT_DIR/observability/grafana/kubernetes/grafana-deployment.yaml
sudo kubectl apply -f $PROJECT_DIR/observability/grafana/kubernetes/grafana-service.yaml

##############################################
# kube-state-metrics
##############################################

echo ""
echo "===== Deploying kube-state-metrics ====="

sudo kubectl apply -f $PROJECT_DIR/observability/kube-state-metrics/service-account.yaml
sudo kubectl apply -f $PROJECT_DIR/observability/kube-state-metrics/cluster-role.yaml
sudo kubectl apply -f $PROJECT_DIR/observability/kube-state-metrics/cluster-role-binding.yaml
sudo kubectl apply -f $PROJECT_DIR/observability/kube-state-metrics/deployment.yaml
sudo kubectl apply -f $PROJECT_DIR/observability/kube-state-metrics/service.yaml

##############################################
# Node Exporter
##############################################

echo ""
echo "===== Deploying Node Exporter ====="

sudo kubectl apply -f $PROJECT_DIR/observability/node-exporter/namespace.yaml
sudo kubectl apply -f $PROJECT_DIR/observability/node-exporter/node-exporter-daemonset.yaml
sudo kubectl apply -f $PROJECT_DIR/observability/node-exporter/node-exporter-service.yaml

##############################################
# Restart Monitoring Components
##############################################

echo ""
echo "===== Restarting Monitoring Components ====="

sudo kubectl rollout restart deployment prometheus -n monitoring
sudo kubectl rollout restart deployment grafana -n monitoring

##############################################
# Wait for Rollout
##############################################

echo ""
echo "===== Waiting for Deployments ====="

sudo kubectl rollout status deployment/prometheus -n monitoring
sudo kubectl rollout status deployment/grafana -n monitoring
sudo kubectl rollout status deployment/kube-state-metrics -n kube-system
sudo kubectl rollout status daemonset/node-exporter -n monitoring

##############################################
# Summary
##############################################

echo ""
echo "===== Monitoring Pods ====="

sudo kubectl get pods -n monitoring

echo ""
echo "===== kube-system Pods ====="

sudo kubectl get pods -n kube-system | grep kube-state

echo ""
echo "===== Monitoring Services ====="

sudo kubectl get svc -n monitoring

echo ""
echo "==============================================="
echo " Observability Deployment Successful!"
echo "==============================================="

echo ""
echo "Monitoring Services:"
echo "  Prometheus : http://13.233.81.248:30089"
echo "  Prometheus Targets : http://13.233.81.248:30089/targets"
echo "  Grafana    : http://13.233.81.248:30090"
echo ""
echo "Deployment completed."
