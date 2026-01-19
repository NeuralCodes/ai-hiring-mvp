terraform {
  required_version = ">= 1.0.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# TODO: Enable required GCP APIs
# resource "google_project_service" "cloudfunctions" {
#   service = "cloudfunctions.googleapis.com"
# }
#
# resource "google_project_service" "cloudbuild" {
#   service = "cloudbuild.googleapis.com"
# }
#
# resource "google_project_service" "sheets" {
#   service = "sheets.googleapis.com"
# }

# TODO: Cloud Function - ingest_getonboard
# resource "google_cloudfunctions2_function" "ingest_getonboard" {
#   name     = "ingest-getonboard"
#   location = var.region
#
#   build_config {
#     runtime     = "python311"
#     entry_point = "main"
#     source {
#       storage_source {
#         bucket = var.source_bucket
#         object = "ingest_getonboard.zip"
#       }
#     }
#   }
#
#   service_config {
#     max_instance_count = 1
#     available_memory   = "256M"
#     timeout_seconds    = 60
#   }
# }

# TODO: Cloud Function - evaluate_candidate
# resource "google_cloudfunctions2_function" "evaluate_candidate" {
#   name     = "evaluate-candidate"
#   location = var.region
#   ...
# }

# TODO: Cloud Function - push_teamtailor
# resource "google_cloudfunctions2_function" "push_teamtailor" {
#   name     = "push-teamtailor"
#   location = var.region
#   ...
# }
