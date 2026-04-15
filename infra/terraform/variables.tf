variable "aws_region" {
  default = "us-east-1"
}

variable "environment" {
  default = "dev"
}

variable "instance_type" {
  default = "t3.small"
}

variable "key_pair_name" {
  description = "EC2 key pair name for SSH access"
  type        = string
  default     = ""
}

variable "billing_alert_email" {
  description = "Email for billing alerts"
  type        = string
  default     = "realgenregod@gmail.com"
}
