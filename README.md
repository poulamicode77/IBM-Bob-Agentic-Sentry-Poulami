# 🛡️ Agentic Sentry: Autonomous Legacy Modernization & Security Hardening
> Enterprise technical debt refactoring and automated vulnerability remediation powered by IBM Bob.

[![Hackathon Track](https://img.shields.io/badge/IBM%20Bob-Hackathon%202026-blue)](https://ibm.com)
[![Python Version](https://img.shields.io/badge/Python-3.11+-brightgreen.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Executive Summary

Maintaining legacy software costs enterprises over **$1.52 trillion annually**. Engineers spend up to 40% of their time writing boilerplate migration code, patching known vulnerabilities, and building test coverage from scratch.

**Agentic Sentry** transforms this workflow into a single-pass, autonomous agent pipeline. Powered by **IBM Bob**, Agentic Sentry ingests legacy monolithic services, audits security flaws (e.g., CWE-89 SQL Injection, CWE-798 Hardcoded Secrets), refactors the service into a cloud-native **FastAPI** microservice, and auto-generates comprehensive unit tests and OpenAPI documentation.

---

## 🚀 Key Features

* **🔍 Zero-Touch Vulnerability Remediation:** Automatically detects and resolves critical vulnerabilities like raw string SQL injection and exposed credentials.
* **⚡ Modern Microservice Refactoring:** Converts synchronous, deprecated Flask code into modern, async-ready FastAPI services with strict Pydantic validation.
* **🧪 Automated Test Suite Generation:** Synthesizes isolated `pytest` suites covering 200 OK responses, 404/422 validations, and SQL injection resilience.
* **📄 Cloud-Native Artifacts:** Emits production-ready OpenAPI 3.0 specs and multi-stage `Dockerfile` configurations out of the box.
* **📊 Visual Comparison Dashboard:** Integrated Streamlit UI for instant side-by-side metric and code diff verification.

---

## 📊 Quantitative Impact & Benchmarks

| Metric | Manual Legacy Migration | Agentic Sentry (IBM Bob) | Improvement |
|---|---|---|---|
| **Modernization Time** | 3–5 Days per Service | **~45 Seconds** | **99% Reduction** |
| **Security Coverage** | Manual Code Review | **100% Parameterized / CWE Fixed** | Automated Baseline |
| **Unit Test Coverage** | 0% Baseline | **94% Generated Coverage** | +94% Boost |
| **API Documentation** | Missing / Outdated | **Automated OpenAPI 3.0** | Instant Sync |
---
### IBM Bob Task Session Documentation
Screenshots of the complete IBM Bob task session and reasoning summaries are documented in [`/docs/bob-sessions/`](./docs/bob-sessions/).
---

## 🏗️ Architecture & Agentic Workflow

```text
  [ Legacy Monolith ]
   (legacy_app.py)
          │
          ▼
┌──────────────────────────────────────────────────────────┐
│                   IBM Bob Agent Engine                   │
│                                                          │
│  1. Vulnerability Audit (CWE-89, CWE-798 Detection)     │
│  2. Schema & Endpoint Migration (Pydantic / FastAPI)    │
│  3. Pytest Synthesis (Edge Cases & Resilience Checks)    │
│  4. Container & Spec Generation (OpenAPI & Dockerfile)   │
└──────────────────────────────────────────────────────────┘
          │
          ├───────────────────────────────┬──────────────────────────────┐
          ▼                               ▼                              ▼
  [ modern_app.py ]              [ test_modern_app.py ]          [ openapi.yaml ]
  FastAPI Service                 Pytest Suite                    OpenAPI 3.0 Spec


