# Cloud Reliability Platform - 75% Complete

A cloud-native platform for testing system reliability, failure recovery, and observability under production-like conditions using Kubernetes on Azure. Simulates real-world distributed system behavior and validate reliability through metrics, SLOs, and controlled failure scenarios.

## Stack
- FastAPI - core API service
- Docker - containerization
- Kubernetes (AKS) - orchestration layer 
- Terraform - infrastructure as code (Azure)
- Azure Container Registry (ACR) - image registry
- Azure Kubernetes Service (AKS) - cluster runtime
- GitHub Actions - CI/CD automation
- Prometheus - metrics collection
- Grafana - dashboards and visualization
- kubectl - cluster operations and debugging

## System Design
- FastAPI service runs in Docker containers.
- Containers are built and pushed to ACR.
- AKS pulls images from ACR and runs the application.
- Terraform provisions Azure infrastructure.
- GitHub Actions handles build, push, deployment automation.
- Prometheus scrapes metrics from Kubernetes.
- Grafana visualizes SLOs, latency, and error rates.

## SLOs (Service Level Objectives)
- Service availability
- Error rate (5xx tracking)
- p95 latency

## Reliability Design (In Progress)
- Kubernetes restart policies for failure recovery
- Liveness/readiness probes
- Controlled failure injection endpoints
- Horizontal scaling via AKS
- Rolling deployments for zero-downtime updates
- Load testing scripts

## Observability (In Progress)
- Prometheus for metrics - done
- Grafana for metric visualization - done
- Structured JSON logging
- Request IDs for tracing
- Kubernetes logs
- Loki log aggregation

## CI/CD
- CI: Python env setup, dependency installation, FastAPI import validation
- CD: Docker image build, push to ACR, Kubernetes deployment, rolling update verification