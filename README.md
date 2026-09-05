# SynapseMesh 🧠🕸️
> **Autonomous Multi-Agent Task Orchestrator & Knowledge Graph Memory Engine**

[![Python 3.11](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Neo4j](https://img.shields.io/badge/Neo4j-5.18.0-blue.svg)](https://neo4j.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)](https://fastapi.tiangolo.com/)

---

## 📌 Executive Summary

**SynapseMesh** is an autonomous AI agent orchestration platform that organizes multi-agent execution workflows (Planner, Executor, Evaluator) and maintains long-term contextual memory using a **Neo4j Graph Database**.

---

## 🏗️ Graph Memory Architecture

Nodes and Edges created dynamically in Neo4j via Cypher queries:
```text
(:Agent {name: 'PlannerAgent'}) -[:EXECUTES]-> (:Task {title: 'Analyze Enterprise Vulnerabilities'})
(:Task) -[:STORED_MEMORY]-> (:MemoryNode {content: 'PII Redacted & Verification Complete'})
```

---

---

## Author

**Spandan Gowda B C**
* **GitHub**: [@SpandanGowdaBC](https://github.com/SpandanGowdaBC)
* **Repository**: [SynapseMesh](https://github.com/SpandanGowdaBC/synapsemesh)