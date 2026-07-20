# Cloud Event Platform

## Overview

The Cloud Event Platform is a cloud-native microservices application developed for the MSc Big Data Analytics (Cloud Computing) coursework. The project demonstrates containerization, Kubernetes orchestration, cloud deployment, analytics, observability, and deployment automation using AWS EC2 and K3s.

The platform allows users to browse events, register for programs, collect analytics, and monitor the infrastructure using modern cloud technologies.

---

## Technologies Used

### Cloud Infrastructure
- AWS EC2 (Ubuntu 24.04 LTS)
- K3s Kubernetes
- Docker

### Backend
- FastAPI
- Python 3.12

### Frontend
- HTML
- CSS
- JavaScript

### Databases
- PostgreSQL
- ClickHouse

### Analytics
- Metabase

### Observability
- Prometheus
- Grafana
- Node Exporter
- kube-state-metrics

---

## Project Structure

```
cloud-event-platform/
│
├── analytics-service/
├── clickhouse/
├── dashboard-service/
├── docs/
├── event-service/
├── frontend/
├── kubernetes/
├── lambda/
├── metabase/
├── observability/
├── postgres/
├── program-service/
├── registration-service/
├── screenshots/
│
├── deploy-all.sh
├── deploy-observability.sh
├── cleanup.sh
└── README.md
```

---

## Architecture

The platform consists of the following components:

- Frontend Web Application
- Event Service
- Program Service
- Registration Service
- Analytics Service
- PostgreSQL Database
- ClickHouse Analytics Database
- Metabase Dashboard
- Prometheus Monitoring
- Grafana Dashboard

All services are deployed as Docker containers on Kubernetes (K3s).

---

## Deployment

### Deploy the Application

```bash
chmod +x deploy-all.sh
./deploy-all.sh
```

### Deploy Monitoring

```bash
chmod +x deploy-observability.sh
./deploy-observability.sh
```

---

## Application URLs

| Service | URL |
|----------|-----|
| Frontend | hhttp://13.233.81.248:30083 |
| Event Service | http://13.233.81.248:30081/docs |
| Program Service | http://13.233.81.248:30082/docs |
| Registration Service | http://13.233.81.248:30084 |
| Analytics Service | http://13.233.81.248:30085 |
| Dashboard | http://13.233.81.248:30086 |
| Metabase | http://13.233.81.248:30087 |
| Prometheus | http://13.233.81.248:30089 |
| Grafana | http://13.233.81.248:30090 |

---

## Monitoring

The project includes:

- Prometheus for metrics collection
- Node Exporter for system metrics
- kube-state-metrics for Kubernetes metrics
- Grafana dashboards for infrastructure monitoring

---

## Analytics

Analytics events are collected through the Analytics Service and stored in ClickHouse.

Metabase is connected to ClickHouse and provides dashboards including:

- Total Analytics Events
- Event Type Distribution
- Events Over Time
- Most Visited Pages
- Latest Analytics Events

---

## Screenshots

Project screenshots are available in the `screenshots/` directory and demonstrate:

- AWS EC2 deployment
- Docker images
- Kubernetes resources
- Microservices
- PostgreSQL
- ClickHouse
- Metabase dashboards
- Prometheus monitoring
- Grafana dashboards

---

## Author

**Pavithra Yasiru**

MSc Big Data Analytics

Cloud Computing Coursework
