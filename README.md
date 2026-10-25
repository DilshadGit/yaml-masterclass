# ⚙️ YAML Specification & Cloud-Native Architecture Masterclass

[![YAML](https://img.shields.io/badge/YAML-1.2%20Spec-CB171E?style=for-the-badge&logo=yaml&logoColor=white)](https://yaml.org)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Manifests-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v2.x-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![Helm](https://img.shields.io/badge/Helm-Values-0F1689?style=for-the-badge&logo=helm&logoColor=white)](https://helm.sh)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

> Complete zero-to-hero curriculum in YAML specifications, the strict 2-space law, scalar type coercion, multiline string chomping (`|` vs `>`), DRY inheritance with Anchors & Aliases (`&`, `*`, `<<:`), production Kubernetes architecture, Docker Compose stacks, and Python safe deserialization.

---

## 📑 Curriculum & Architecture Roadmap

```
Foundations: 2-Space Law & Scalars ──► Multiline Strings (| vs >) ──► DRY Anchors & Aliases (&, *, <<:)
                                                                                  │
Security Pitfalls (Norway Problem) ◄── Helm & GitHub Actions ◄── Kubernetes & Docker Compose
```

| Chapter | Topic | Highlights | Document |
|---|---|---|---|
| **Overview** | **Masterclass Blueprint** | Indentation rules, scalar types, block mapping, sequences | [`YAML_MASTERCLASS_BLUEPRINT.md`](docs/YAML_MASTERCLASS_BLUEPRINT.md) |
| **Guide** | **Installation & CLI Tools** | `yamllint`, `yq`, `helm template`, schema validation | [`YAML_GUIDE_AND_INSTALLATION.md`](docs/YAML_GUIDE_AND_INSTALLATION.md) |
| **Security** | **Security & Parsing Pitfalls** | Norway problem (`NO: false`), octal zeros, Billion Laughs attacks | [`YAML_SECURITY_AND_PARSING_PITFALLS.md`](docs/YAML_SECURITY_AND_PARSING_PITFALLS.md) |
| **Docker Compose** | **Multi-Service Architecture** | Web, Redis, Postgres, health checks, networks, anchor logging | [`docker-compose.production.yml`](blueprints/docker-compose.production.yml) |
| **Kubernetes** | **Production K8s Manifests** | Namespace, ConfigMap, Secrets, Deployment, Service, HPA | [`k8s/`](blueprints/k8s/) |
| **Helm** | **Production Helm Values** | Ingress TLS, autoscaling metrics, probes, resource bounds | [`values.production.yaml`](blueprints/helm/values.production.yaml) |
| **Python Tools** | **Safe Load & Validation** | Python scripts for schema validation and anchor resolution | [`python_tools/`](python_tools/) |
| **Exam** | **Masterclass Examination** | 24 Multiple-choice questions with deep technical rationale | [`QUIZ.md`](QUIZ.md) |

---

## 🏛️ Multiline Strings: Literal (`|`) vs Folded (`>`)

| Syntax | Name | Behavior | Newlines | Common Use Case |
|---|---|---|---|---|
| `key: \|` | **Literal Block** | Preserves newlines exactly as written in the block. | Kept (`\n`) | Shell scripts, private keys, certificates, config files |
| `key: >` | **Folded Block** | Folds consecutive lines into a single spaced string. | Converted to space | Long prose paragraphs, error messages, descriptions |
| `key: \|-` | **Strip Chomping** | Trims all trailing newlines and whitespace. | Removed | Single-line secrets, environment variable values |
| `key: \|+` | **Keep Chomping** | Retains all trailing newlines at the end of the block. | Preserved | Exact EOF-sensitive file templates |

---

## 🔄 DRY Architecture: Anchors (`&`), Aliases (`*`), and Merge Keys (`<<:`)

Eliminate duplicated configuration across services:

```yaml
# Define anchor with &
x-common-logging: &logging-config
  driver: "json-file"
  options:
    max-size: "100m"
    max-file: "5"

services:
  service-alpha:
    image: alpha:v1
    logging: *logging-config  # Dereference alias with *

  service-beta:
    image: beta:v1
    logging: *logging-config
```

---

## 🛠️ Complete Blueprints & Tools Included

1. **Production Docker Compose**: [`blueprints/docker-compose.production.yml`](blueprints/docker-compose.production.yml)
2. **Kubernetes Architecture**: Complete stack in [`blueprints/k8s/`](blueprints/k8s/)
3. **Helm Values Blueprint**: [`blueprints/helm/values.production.yaml`](blueprints/helm/values.production.yaml)
4. **Python Validation Tools**: [`python_tools/yaml_validator.py`](python_tools/yaml_validator.py) & [`yaml_merger.py`](python_tools/yaml_merger.py)

---

## 🧪 Masterclass Examination

Test your YAML mastery in [`QUIZ.md`](QUIZ.md) covering scalar typing rules, flow vs block styles, merge key precedence, and security protections.
