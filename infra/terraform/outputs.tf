output "artifacts_bucket" {
  value = aws_s3_bucket.artifacts.bucket
}

output "logs_bucket" {
  value = aws_s3_bucket.logs.bucket
}

output "dev_instance_id" {
  value = aws_instance.dev_build.id
}

output "dev_instance_public_ip" {
  value = aws_instance.dev_build.public_ip
}

output "dev_iam_role_arn" {
  value = aws_iam_role.dev_instance.arn
}
