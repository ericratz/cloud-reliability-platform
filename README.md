# Cloud Reliability Platform - 50% complete

A cloud platform for testing system reliability, failure recovery, and observability under realistic production conditions.

## Stack
- FastAPI (application/API service)
- Docker (container)
- Terraform (IaC)
- Azure Kubernetes Service (AKS)
- Azure Container Registry (ACR)
- GitHub Actions (CI/CD automation)
- kubectl - Kubernetes deplyment operations

## System Design
- FastAPI service runs in Docker containers.
- Containers are built and pushed to ACR.
- AKS pulls images from ACR and runs the application.
- Terraform provisions all Azure infrastructure.
- GitHub Actions handles build, push, deployment automation.

## SLOs
- Service availability tracking with success/error rate
- Latency targets
- Health endpoint monitoring

## Reliability Design
- Kubernetes restart policies for failed containers
- Liveness probes
- Controlled failure injection endpoints
- Horizontal scaling via AKS
- Rolling updates for zero-downtime deployments

## Observability
- Structured JSON logging
- Request IDs for tracing
- Kubernetes logs
- Metrics collection

## Terraform
- Azure Resource Group
- Azure Kubernetes Service
- Azure Container Registry
- Role Assignment

## Kubernetes Deployment
Apply manifests, update image (CI/CD), expose service:
```bash
kubectl apply -f k8s/
kubectl set image deployment/crp crp=ericratz.azurecr.io/crp:<tag>
kubectl get svc
```

## Deployment checklist
1. Build FastAPI service - done
2. Containerize with Docker - done
3. GitHub Actions CI setup - done
4. Provision Azure infrastructure (Terraform) - done
5. Deploy AKS cluster - done
6. Deploy application via Kubernetes - done
7. Configure CI/CD pipeline - done
8. Automate deployments via kubectl/GitHub Actions - done
9. Validate SLOs, observability, and failure scenarios (todo)

## Lessons Learned
- Azure AKS region + VM SKU availability matters (e.g., westus3 vs westus2 issues)
- ACR requires authentication for Kubernetes image pulls
- Terraform state must be respected (don’t delete Azure manually mid-state)
- Kubernetes uses rolling updates when image tags change
- ImagePullBackOff usually = auth or registry access issue, not build issue