# Serverless API Ingestion & Gateway Telemetry Auditor

A Python-based security auditing framework engineered to analyze transaction behaviors, endpoint resilience, and automated rate-throttling enforcement mechanisms on distributed public serverless gateways (AWS Lambda & API Gateway micro-services).

## 📊 Core Operational Mechanism (Kaam)
* **API Transaction Probing:** Automates sequential, parameterized HTTP GET payloads configured with precise cross-origin headers (`CORS`) to simulate real-world web application requests.
* **Response Telemetry Extraction:** Intercepts dynamic JSON payloads from the cloud gateway, extracting processing attempt timelines (`second`), payload statuses, and base64 encoded strings.
* **Rate-Limit Auditing:** Monitors backend response mutation under continuous execution to evaluate how the infrastructure mitigates serverless compute resource exhaustion.

## 🛡️ Practical Security Use-Cases (Use)
* **Infrastructure Resilience Testing:** Validates if public endpoints are protected against automated payload amplification attacks and rapid resource exhaustion.
* **Edge Caching Policy Evaluation:** Demonstrates how public cloud gateways enforce fallback policies (such as serving cached static media nodes) when a specific client IP exceeds transaction thresholds.
* 
