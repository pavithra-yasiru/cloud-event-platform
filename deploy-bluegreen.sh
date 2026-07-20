#!/bin/bash

set -e

echo "========================================="
echo " Blue-Green Deployment"
echo "========================================="

PROJECT_DIR=~/cloud-event-platform

####################################################
# Detect active deployment
####################################################

CURRENT=$(sudo kubectl get service event-service \
-o jsonpath='{.spec.selector.version}')

echo ""
echo "Current active deployment : $CURRENT"

if [ "$CURRENT" = "blue" ]; then
    TARGET="green"
    DEPLOYMENT="event-service-green"
    YAML="event-green-deployment.yaml"
else
    TARGET="blue"
    DEPLOYMENT="event-service-blue"
    YAML="event-blue-deployment.yaml"
fi

echo "Target deployment         : $TARGET"

####################################################
# Build latest image
####################################################

echo ""
echo "Building latest Event Service..."

cd $PROJECT_DIR/event-service

sudo docker build -t event-service:latest .
sudo docker save event-service:latest -o event-service.tar
sudo k3s ctr images import event-service.tar

####################################################
# Deploy inactive deployment
####################################################

echo ""
echo "Deploying $TARGET..."

sudo kubectl apply -f kubernetes/$YAML

sudo kubectl rollout restart deployment/$DEPLOYMENT

####################################################
# Wait until deployment becomes READY
####################################################

echo ""
echo "Waiting for deployment to become healthy..."

sudo kubectl rollout status deployment/$DEPLOYMENT --timeout=180s

####################################################
# Switch traffic
####################################################

echo ""
echo "Switching traffic to $TARGET..."

sudo kubectl patch service event-service \
-p "{\"spec\":{\"selector\":{\"app\":\"event-service\",\"version\":\"$TARGET\"}}}"

####################################################
# Verify switch
####################################################

ACTIVE=$(sudo kubectl get service event-service \
-o jsonpath='{.spec.selector.version}')

if [ "$ACTIVE" != "$TARGET" ]; then
    echo ""
    echo "ERROR: Service switch failed."
    exit 1
fi

####################################################
# Finished
####################################################

echo ""
echo "========================================="
echo " Blue-Green Deployment Completed"
echo "========================================="
echo "Previous deployment : $CURRENT"
echo "Current deployment  : $TARGET"
echo "Rollback available  : $CURRENT"
