# Kanizsa Analytics Service

**Version:** 1.1.0  
**Last Updated:** August 9, 2025, 12:03:30 CDT  
**Purpose:** Advanced Analytics & Data Processing Platform for Kanizsa Ecosystem

## 🎯 **Overview**

The Kanizsa Analytics Service provides advanced data processing, machine learning, and business intelligence capabilities for the Kanizsa ecosystem. This service enables real-time analytics, batch processing, and predictive modeling.

## 🏗️ **Architecture**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Sources  │───▶│   Analytics     │───▶│   Insights &    │
│                 │    │   Service       │    │   Reports       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Data Storage  │
                       │   & Processing  │
                       └─────────────────┘
```

## 🚀 **Quick Start**

### Prerequisites
- Docker and Docker Compose
- At least 8GB RAM available
- 20GB+ disk space

### Containerized Setup
```bash
# Clone the repository
git clone https://github.com/wcervin/kanizsa-analytics.git
cd kanizsa-analytics

# Copy environment variables
cp env.example .env

# Start the analytics stack
docker-compose up -d

# Access services
# Spark Master: http://localhost:8080
# Flink JobManager: http://localhost:8081
# ClickHouse: http://localhost:8123
```

## 🔧 **Analytics Services**

### **Apache Spark**
- **Purpose:** Batch data processing and machine learning
- **Port:** 8080 (Master), 7077 (RPC)
- **Features:**
  - Large-scale data processing
  - Machine learning pipelines
  - SQL analytics
  - Graph processing

### **Apache Flink**
- **Purpose:** Real-time stream processing
- **Port:** 8081 (JobManager)
- **Features:**
  - Event-time processing
  - Stateful computations
  - CEP (Complex Event Processing)
  - Real-time analytics

### **ClickHouse**
- **Purpose:** High-performance analytics database
- **Port:** 8123 (HTTP), 9000 (Native)
- **Features:**
  - Columnar storage
  - Real-time query processing
  - High compression ratios
  - SQL compatibility

## 📊 **Configuration**

### Environment Variables
```bash
# Spark Configuration
SPARK_MASTER_URL=spark://spark-master:7077
SPARK_WORKER_MEMORY=1G
SPARK_WORKER_CORES=1

# Flink Configuration
FLINK_JOBMANAGER_URL=http://flink-jobmanager:8081
FLINK_TASKMANAGER_SLOTS=2

# ClickHouse Configuration
CLICKHOUSE_HOST=clickhouse
CLICKHOUSE_PORT=8123
CLICKHOUSE_DB=kanizsa_analytics
CLICKHOUSE_USER=default
CLICKHOUSE_PASSWORD=clickhouse_password
```

## 🔍 **Analytics Capabilities**

### **Data Processing**
- ETL (Extract, Transform, Load) pipelines
- Data quality validation
- Schema evolution management
- Data lineage tracking

### **Machine Learning**
- Predictive modeling
- Anomaly detection
- Recommendation systems
- Natural language processing

### **Real-time Analytics**
- Stream processing
- Real-time dashboards
- Event correlation
- Alert generation

### **Business Intelligence**
- Interactive dashboards
- Ad-hoc querying
- Report generation
- Data visualization

## 🔒 **Security**

### **Data Protection**
- Data encryption at rest
- Secure data transmission
- Access control and authentication
- Audit logging

### **Privacy Compliance**
- GDPR compliance
- Data anonymization
- Consent management
- Data retention policies

## 🚨 **Monitoring**

### **Performance Monitoring**
- Processing latency tracking
- Resource utilization monitoring
- Error rate monitoring
- Throughput metrics

### **Data Quality Monitoring**
- Data completeness checks
- Data accuracy validation
- Schema validation
- Anomaly detection

## 🚀 **Deployment**

### **Production Deployment**
```bash
# Production environment setup
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Scale services
docker-compose up -d --scale spark-worker=3
docker-compose up -d --scale flink-taskmanager=2
```

### **High Availability**
- Spark cluster with multiple workers
- Flink cluster with multiple task managers
- ClickHouse cluster with replication
- Load balancing and failover

## 🧪 **Testing**

### **Health Checks**
```bash
# Check service health
curl http://localhost:8000/health

# Check Spark status
curl http://localhost:8080

# Check Flink status
curl http://localhost:8081

# Check ClickHouse
curl http://localhost:8123/ping
```

### **Data Processing Tests**
```bash
# Submit Spark job
spark-submit --master spark://localhost:7077 job.py

# Submit Flink job
flink run -m localhost:8081 job.jar
```

## 📚 **Documentation**

- [Apache Spark Documentation](https://spark.apache.org/docs/)
- [Apache Flink Documentation](https://flink.apache.org/docs/)
- [ClickHouse Documentation](https://clickhouse.com/docs/)
- [Kanizsa Ecosystem Documentation](../kanizsa-photo-categorizer/README.md)

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Footer:** Kanizsa Analytics Service v1.1.0 | Last Updated: August 9, 2025, 12:03:30 CDT
