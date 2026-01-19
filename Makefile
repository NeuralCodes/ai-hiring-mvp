.PHONY: help tf-init tf-plan tf-apply deploy-ingest deploy-evaluate deploy-push deploy-all

help:
	@echo "Available targets:"
	@echo "  tf-init       - Initialize Terraform"
	@echo "  tf-plan       - Plan Terraform changes"
	@echo "  tf-apply      - Apply Terraform changes"
	@echo "  deploy-ingest - Deploy ingest_getonboard function"
	@echo "  deploy-evaluate - Deploy evaluate_candidate function"
	@echo "  deploy-push   - Deploy push_teamtailor function"
	@echo "  deploy-all    - Deploy all functions"

# Terraform targets
tf-init:
	# cd infra/terraform && terraform init

tf-plan:
	# cd infra/terraform && terraform plan

tf-apply:
	# cd infra/terraform && terraform apply

# Function deployment targets
deploy-ingest:
	# TODO: gcloud functions deploy ingest_getonboard ...

deploy-evaluate:
	# TODO: gcloud functions deploy evaluate_candidate ...

deploy-push:
	# TODO: gcloud functions deploy push_teamtailor ...

deploy-all: deploy-ingest deploy-evaluate deploy-push
