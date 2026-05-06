# Cloud Reliability Platform

A cloud platform for testing system reliability, failure recovery, and observability under realistic production conditions.

## Stack
- FastAPI (application/API service)
- Docker (container)
- Terraform (IaC)
- Azure Kubernetes Service (AKS)
- GitHub Actions (CI/CD automation)

## System Design
- FastAPI service runs in Docker containers deployed to AKS.
- Terraform provisions all Azure infrastructure.
- GitHub Actions handles CI/CD automation.

## SLOs
- Service availability tracking with success/error rate
- Latency targets

## Reliability Design
- Failure injection endpoints for controlled fault testing
- Kubernetes health checks
- Kubernetes container restarts
- Autoscaling triggers based on load

## Observability
- Structured JSON logging
- Request IDs for tracing
- Metrics collection

## Deployment checklist
1. Build FastAPI service
2. Containerize with Docker
3. Provision Azure infrastructure with Terraform
4. Deploy AKS cluster
5. Deploy application via Kubernetes
6. Configure GitHub Actions CI/CD pipeline
7. Validate SLOs, observability, and failure scenarios