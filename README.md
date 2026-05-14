# Cloud Reliability Platform

A cloud-native platform for testing system reliability, failure recovery, and observability under production-like conditions using Kubernetes on Azure. Simulates real-world distributed system behavior and validates reliability through metrics, SLOs, controlled failure injection, and automated load testing.

## Stack
- FastAPI - core API service
- Docker - containerization
- Kubernetes (AKS) - orchestration layer 
- Terraform - infrastructure as code (Azure)
- Azure Container Registry (ACR) - image registry
- Azure Kubernetes Service (AKS) - cluster runtime
- GitHub Actions - CI/CD automation
- Helm - Kubernetes package manager
- Prometheus - metrics collection
- Grafana - dashboards and visualization
- Loki+Promtail - log aggregation
- k6 - load testing
- kubectl - cluster operations and debugging

## System Design
- FastAPI service runs in Docker containers.
- Containers are built and pushed to ACR.
- AKS pulls images from ACR and runs the application.
- Terraform provisions Azure infrastructure.
- GitHub Actions handles build, push, deployment, and reliability validation.
- Helm manages Grafana, Prometheus, and Loki deployments via chart values.
- Prometheus scrapes metrics from Kubernetes pods.
- Grafana visualizes SLOs, latency, error rates, and Loki logs.

## API Endpoints
- / - service index with links
- /health -  health check with restart count, memory, disk, and SLO status.
- /metrics - displays raw prometheus metrics
- /slo - current SLO snapshot (availability, 500 errors, p95 latency)
- /reliability/status - shows current injection state
- POST /reliability/toggle-latency - injects 500ms latency
- POST /reliability/toggle-errors - injects 500 errors on all non-reliability requests
- POST /reliability/trigger-error - injects one 500 error
- /docs - Swagger UI

## SLOs (Service Level Objectives)
- Service availability
- Error rate (5xx tracking)
- p95 latency

## Reliability Design
- Kubernetes restart policies for failure recovery
- Liveness/readiness probes
- Controlled failure injection via API
- Rolling deployments for zero-downtime updates
- Horizontal Pod Autoscaling
- Grafana customized alert rules based on SLOs
- k6 load testing
- CI/CD reliability gate

## Observability
- Prometheus scrapes metrics every 30s
- Loki log aggregation with Promtail on all cluster nodes
- Grafana dashboard for SLO and log visualization
- Structured JSON logging on each request
- Access Grafana: kubectl port-forward svc/grafana 3000:80
- Access Prometheus: kubectl port-forward svc/prometheus-server 9090:80

## CI/CD
- CI: Python env setup, dependency installation, FastAPI import validation
- CD: Docker image build, push to ACR, Kubernetes deployment, rolling update verification, k6 reliability gate