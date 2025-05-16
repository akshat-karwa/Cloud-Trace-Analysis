# ☁️ Cloud Trace Analysis: Cross-Platform Cloud Utilization Analysis

**Authors**: Akshat Karwa (akarwa7@gatech.edu), Mehul Rastogi (mehulrastogi@gatech.edu)  
**Affiliation**: Georgia Institute of Technology

## 📌 Project Overview

**Cloud Trace Analysis** is a comparative analysis of cloud resource utilization patterns across **Google Cloud**, **Microsoft Azure**, and **Alibaba Cloud**, using publicly available trace datasets. We explore the **utilization gap**—the difference between allocated and actual resource usage—and provide insights for improving **resource allocation** and reducing **operational costs**.

---

## 📈 Motivation

Cloud platforms often over-provision resources, resulting in idle capacity and higher costs. While many prior studies focus on a single provider, our project performs a **cross-platform analysis** to identify both shared inefficiencies and provider-specific strategies.

---

## 🧠 Key Contributions

- Normalization and analysis of heterogeneous cloud trace datasets.
- Visualization of time-series, instance-level, and machine-level utilization.
- Predictive modeling using **XGBoost** to forecast CPU and memory usage.
- Comparative evaluation of resource allocation strategies.

---

## 📊 Datasets

| Provider       | Dataset Source | Key Metrics              |
|----------------|----------------|--------------------------|
| Google Cloud   | [Google Cluster Data](https://github.com/google/cluster-data) | CPU, Memory, Task Type, Priority |
| Microsoft Azure| [Azure Public Dataset](https://github.com/Azure/AzurePublicDataset) | CPU, VM Config, Category |
| Alibaba Cloud  | [Alibaba Cluster Trace](https://github.com/alibaba/clusterdata) | CPU, Memory, Task Type |

---

## 🔍 Methodology

### 1. Data Preprocessing
- Unified schemas and normalized key metrics.
- Merged relevant tables (e.g., instance usage, machine metadata).
- Cleaned and sampled large-scale data (up to millions of rows).

### 2. Exploratory Analysis
- Time-series plots for CPU/Memory usage.
- Histogram and distribution visualizations at machine and task level.

### 3. Predictive Modeling
- Trained **XGBoost** regressors to predict CPU and memory usage.
- Evaluated using RMSE and a ±10% accuracy threshold.

---

## 🧪 Results Summary

| Cloud Provider | Avg. CPU Util | Avg. Memory Util | CPU Prediction Accuracy | Memory Prediction Accuracy |
|----------------|---------------|------------------|--------------------------|-----------------------------|
| Google Cloud   | 26.14%        | 44.0%            | 81.8%                    | 67.3%                       |
| Azure          | 15.6%         | *N/A*            | 65.3%                    | *N/A*                       |
| Alibaba Cloud  | 38.2%         | 88.2%            | 52.5%                    | 87.7%                       |

---

## 🔧 Technologies Used

- Python (Pandas, NumPy, Matplotlib, XGBoost)
- Jupyter Notebooks
- Google BigQuery
- Git / GitHub

---
