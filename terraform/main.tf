provider "aws" {
  region = "${var.aws_region}"
}

module "ecs" {
  source  = "terraform-aws-modules/ecs/aws"
  version = "7.6.3"

  cluster_name = "${var.cluster_name}"

  services = {
    my-service = {
      cpu    = 256
      memory = 512

      container_definitions = {
        app = {
          essential = true
          image     = "${var.image}"
          portMappings = [
            {
              containerPort = var.container_port
              protocol      = "tcp"
            }
          ]
        }
      }

      load_balancer = {
        service = {
          target_group_arn = aws_lb_target_group.app.arn
          container_name   = "app"
          container_port   = var.container_port
        }
      }

      subnet_ids       = aws_subnet.private[*].id
      assign_public_ip = false

      security_group_ingress_rules = {
        alb_access = {
          from_port                    = var.container_port
          to_port                      = var.container_port
          ip_protocol                  = "tcp"
          referenced_security_group_id = aws_security_group.alb.id
        }
      }

      security_group_egress_rules = {
        all = {
          ip_protocol = "-1"
          cidr_ipv4   = "0.0.0.0/0"
        }
      }
    }
  }
}