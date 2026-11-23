variable "aws_region" {
  description = "AWS region to deploy into."
  type        = string
  default     = "eu-west-2"
}

variable "image" {
  description = "Name used for the ECS cluster, service, and task."
  type        = string
  default     = "public.ecr.aws/docker/library/httpd:latest"
}
