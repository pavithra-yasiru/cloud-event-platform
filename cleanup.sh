#!/bin/bash

echo "Cleaning temporary deployment files..."

find ~/cloud-event-platform -name "*.tar" -delete

echo "Removing unused Docker images..."

sudo docker image prune -f

echo "Cleanup completed."
