#!/bin/bash

echo "===== Blue-Green Switch ====="

CURRENT=$(sudo kubectl get service event-service -o jsonpath='{.spec.selector.version}')

echo "Current active version: $CURRENT"

if [ "$CURRENT" = "blue" ]; then
    TARGET="green"
else
    TARGET="blue"
fi

echo "Switching traffic to: $TARGET"

sudo kubectl patch service event-service \
  -p "{\"spec\":{\"selector\":{\"app\":\"event-service\",\"version\":\"$TARGET\"}}}"

echo "Waiting for service update..."
sleep 5

echo ""
echo "Current selector:"
sudo kubectl describe service event-service | grep Selector

echo ""
echo "Blue-Green deployment completed successfully!"
