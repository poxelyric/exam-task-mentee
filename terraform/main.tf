data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
}

resource "aws_subnet" "public" {
  count                   = 2
  vpc_id                  = aws_vpc.main.id
  cidr_block              = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index + 10)
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true
}

resource "aws_route_table_association" "public" {
  count          = length(aws_subnet.public)
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

module "ecs" {
  source  = "terraform-aws-modules/ecs/aws"
  version = "7.6.3"

  cluster_name = "my-cluster"

  services = {
    my-service = {
      cpu    = 256
      memory = 512

      container_definitions = {
        app = {
          enable_cloudwatch_logging = false
          essential = true
          image     = "${var.image}"
          portMappings = [
            {
              containerPort = 8000
              protocol      = "tcp"
            }
          ]
        }
      }

      subnet_ids       = aws_subnet.public[*].id
      assign_public_ip = true

      security_group_ingress_rules = {
        port_8000 = {
          from_port   = 8000
          to_port     = 8000
          ip_protocol = "tcp"
          cidr_ipv4   = "0.0.0.0/0"
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