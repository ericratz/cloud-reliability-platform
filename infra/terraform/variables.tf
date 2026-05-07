variable "location" {
  type    = string
  default = "westus2"
}

variable "resource_group_name" {
  type    = string
  default = "cloud-reliability-rg"
}

variable "aks_name" {
  type    = string
  default = "cloud-reliability-aks"
}

variable "acr_name" {
  type        = string
  description = "Must be globally unique, lowercase, no hyphens in some cases"
}