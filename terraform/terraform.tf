# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

terraform {
  # backend "s3" {
  #   bucket       = "exam-orichen"
  #   key          = "terraform/state"
  #   region       = "eu-west-2"
  #   use_lockfile = true
  # }
  required_version = ">= 1.5.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 6.41"
    }
  }
}