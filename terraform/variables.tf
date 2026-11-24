variable "aws_region" {
  description = "AWS region to deploy into."
  type        = string
  default     = "eu-north-1"
}

variable "vpc_cidr_block" {
  description = "CIDR block for the VPC."
  type        = string
  default     = "10.0.0.0/16"
}

variable "cluster_name" {
  description = "Name used for the ECS cluster, service, and task."
  type        = string
  default     = "orichen-exam"
}

variable "image" {
  description = "Name used for the ECS cluster, service, and task."
  type        = string
  default     = "094032936054.dkr.ecr.eu-north-1.amazonaws.com/orichen/exam:1.2.3"
}

variable "container_port" {
  description = "Port on which the container will listen."
  type        = number
  default     = 8080
}
