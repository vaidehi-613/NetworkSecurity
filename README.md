# Network Security Threat Detection Pipeline

An end-to-end MLOps-enabled machine learning pipeline for identifying and classifying network security threats. The pipeline integrates with cloud services, model registries, and GitHub Actions for CI/CD, and is designed to be modular, reproducible, and production-ready.

---

## 🚀 Project Overview

This project uses a multi-stage pipeline architecture to automate the process of:

* Ingesting network traffic data from MongoDB
* Validating and transforming data
* Training and evaluating classification models
* Deploying the best model to cloud (AWS S3) with version control and reproducibility

All stages produce artifacts, are tracked with MLflow, and integrate with GitHub Actions for CI/CD. Dockerized builds are pushed to Amazon ECR.

---

## 🧭 Architecture Diagram

### 🔄 Pipeline Stages

1. **Data Ingestion Component**

   * Connects to MongoDB
   * Reads raw network traffic data
   * Outputs: `Data Ingestion Artifacts`

2. **Data Validation Component**

   * Verifies schema, nulls, duplicates
   * Outputs: `Data Validation Artifacts`

3. **Data Transformation Component**

   * Encodes categorical features
   * Serializes transformer as `preprocessor.pkl`
   * Outputs: `Data Transformation Artifacts`

4. **Model Trainer Component**

   * Trains multiple models (RF, XGB, Logistic Regression, etc.)
   * Logs metrics (F1, precision, recall) via MLflow
   * Outputs: `Model Trainer Artifacts`

5. **Model Evaluation Component**

   * Evaluates model performance on test set
   * If accepted, pushes model forward
   * Outputs: `Model Evaluation Artifacts`

6. **Model Pusher Component**

   * Pushes final `model.pkl` and `preprocessor.pkl`

     * To `final_model/` locally
     * To AWS S3 (`s3://bucket/final_model/`)
     * Logged on DAGsHub with MLflow

---

## 🧪 Technologies Used

* **Backend**: Python, FastAPI
* **Machine Learning**: scikit-learn, pandas, numpy
* **Cloud & DevOps**:

  * AWS S3 (artifact storage)
  * AWS ECR (Docker image storage)
  * GitHub Actions (CI/CD)
  * Docker (containerization)
  * MLflow + DAGsHub (model tracking)
* **Database**: MongoDB

---

## 🐳 Docker & ECR Integration

* Dockerfile builds the app environment
* GitHub Actions job:

  * Builds Docker image
  * Logs in to ECR
  * Pushes tagged image to ECR
* Self-hosted EC2 GitHub runner pulls and runs container

### 📦 Sample ECR URI:

```
266939261225.dkr.ecr.us-east-1.amazonaws.com/networksecurity:latest
```

---

## 📂 Folder Structure

```bash
.
├── Artifacts/                   # Versioned pipeline artifacts
├── final_model/                # Final selected model and preprocessor
├── networksecurity/            # Source code (components, cloud, utils)
│   ├── components/             # Pipeline stage classes
│   ├── cloud/s3_syncer.py      # AWS S3 sync logic
│   ├── utils/                  # Helper modules
├── app.py                      # FastAPI serving script
├── Dockerfile                  # For containerization
├── .github/workflows/          # CI/CD workflow YAML
├── requirements.txt            # Python dependencies
├── README.md
```

---

## 🔒 Secrets Used in GitHub Actions

Set the following secrets under your GitHub repo settings:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
ECR_REPOSITORY_NAME
AWS_ECR_LOGIN_URI
```

---

## 📽️ Demo Video

Embed a demo `.mp4` by uploading it and linking below:

```markdown
https://github.com/<user>/<repo>/assets/demo.mp4
```

Alternatively, upload to YouTube and add a badge:

---

## ✨ Future Enhancements

* Add model versioning via MLflow Registry
* Trigger SageMaker/ECS deployment from CI
* Add monitoring with Prometheus & Grafana
* Introduce concept drift detection

---

## 🤝 Contributing

Pull requests and issues are welcome! Feel free to fork and improve.

---

## 📧 Contact

**Author:** Vaidehi Pawar
**Email:** [vpawar9107@sdsu.edu](mailto:vpawar9107@sdsu.edu)


---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
