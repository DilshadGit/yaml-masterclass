# YAML Architecture, Data Types & Cross-Platform Installation Guide

## 1. Introduction to YAML
**YAML** (*YAML Ain't Markup Language*) is a human-readable data serialization standard widely used in cloud infrastructure, CI/CD pipelines (**GitHub Actions**, **GitLab CI**), container orchestration (**Docker Compose**, **Kubernetes**), and configuration management (**Helm**, **Ansible**).

Unlike JSON or XML, YAML emphasizes minimal visual syntax:
- **No curly braces `{}` or brackets `[]` required** (uses indentation for hierarchy).
- **Strict 2-space indentation law** (tab characters `\t` are strictly forbidden).
- **Native comments supported** via the hash `#` symbol.

---

## 2. Serialization vs. Deserialization

When software applications communicate, configure servers, or launch containers, they continuously convert live data between computer memory and text files:

```
[In-Memory Python Objects (dict, list, int)]
      │
      ├─── 1. Serialization (yaml.dump) ──────► [Human-Readable YAML Text Stream]
      │                                                         │
      └──◄── 2. Deserialization (yaml.safe_load) ───────────────┘
```

### A. Serialization (Dumping / Encoding)
Converting **in-memory data objects** (such as Python dictionaries or lists) into a readable YAML text file or string that can be saved to disk or transmitted over the network.
```python
import yaml

data = {
    "project": "TeachCloud",
    "tier": "backend",
    "replicas": 3,
    "active": True
}

yaml_text = yaml.dump(data, sort_keys=False)
print(yaml_text)
```

### B. Deserialization (Loading / Parsing)
Taking a **raw YAML file or string** from disk or network and parsing it into native in-memory objects that your program can query and execute.
```python
import yaml

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

print(config["project"])
```

> [!CAUTION]
> **Security Rule**: Always deserialize untrusted YAML using `yaml.safe_load()`. Standard `yaml.load()` allows arbitrary Python object instantiation, which attackers can exploit to execute malicious code on your server!

---

## 3. Data Types & Explicit Tags Reference

YAML infers data types automatically, but explicit type tags can be specified using double exclamation marks (`!!`):

### A. Core Scalar Types
- **Integer (`!!int`)**: `zero: !!int 0`, `negative: !!int -23`, `positive: !!int 45`
- **Float (`!!float`)**: `marks: !!float 54.47`, `exponential: 6.245e-4`
- **Boolean (`!!bool`)**: `is_active: true`, `is_debug: false`
- **Null (`!!null`)**: `empty_val: null` or `~`
- **Timestamp (`!!timestamp`)**: `created_at: 2026-10-24T15:30:00Z`

### B. Numeric Bases & Special Floats
- **Binary**: `binary: 0b011011` (base-2)
- **Hexadecimal**: `hex: 0x34` (base-16)
- **Octal**: `octal: 0o755` (base-8)
- **Underscore Separators**: `readable: 548_321` (evaluated as integer `548321`)
- **Special Floats**: `infinite: .inf`, `not_a_num: .nan`

### C. Advanced Collections
- **Sequences (`!!seq`)**: Ordered lists introduced with `- item`.
- **Mappings (`!!map`)**: Associative key-value dictionaries.
- **Pairs (`!!pairs`)**: Ordered key-value pairs allowing duplicate keys:
  ```yaml
  roles: !!pairs
    - job: student
    - job: teacher
  ```
- **Sets (`!!set`)**: Unique collections introduced with `?`:
  ```yaml
  names: !!set
    ? Dilshad
    ? TeachCloud
  ```
- **Ordered Maps (`!!omap`)**: Maps that strictly preserve insertion order.

### D. DRY Anchors & Merge Keys
Avoid code duplication using anchors (`&`), aliases (`*`), and merge keys (`<<: *`):
```yaml
base_config: &base_env
  environment: "production"
  region: "eu-west-1"

web_service:
  <<: *base_env
  service_name: "auth-api"
  port: 8080
```

---

## 4. Cross-Platform Installation Guide

Because YAML is a data specification (plain text format), you do not install YAML itself. Instead, you install the **Python parser (`PyYAML`)** to work with it in code, and **CLI tools (`yq` / `yamllint`)** to query and validate YAML files in the terminal.

### 🐧 Linux (Ubuntu, Debian, RedHat)
```bash
# 1. Python PyYAML Parser:
pip install PyYAML
# Or OS package:
sudo apt update && sudo apt install -y python3-yaml

# 2. CLI YAML Processor (yq):
sudo snap install yq

# 3. YAML Linter:
sudo apt install -y yamllint
```

### 🍎 macOS (Homebrew)
```bash
# 1. Python PyYAML Parser:
pip install PyYAML
# Or Homebrew:
brew install pyyaml

# 2. CLI Tools (yq & yamllint):
brew install yq yamllint
```

### 🪟 Windows (PowerShell / CMD)
```powershell
# 1. Python PyYAML Parser:
py -m pip install PyYAML
# Or standard pip:
pip install pyyaml

# 2. CLI Tools (yq via winget or chocolatey):
winget install MikeFarah.yq
# Or Chocolatey:
choco install yq
```

### Verification (Any OS)
```bash
python -c "import yaml; print('PyYAML successfully loaded:', yaml.__version__)"
```

---

## 5. Masterclass 24-Question Quiz Answer Key

| # | Question Summary | Correct Answer | Explanation |
| :--- | :--- | :--- | :--- |
| **1** | What does YAML stand for? | **B** | YAML Ain't Markup Language (recursive acronym). |
| **2** | Common file extension? | **C** | `.yaml` or `.yml`. |
| **3** | Key-value separator? | **B** | Colon followed by space (`: `). |
| **4** | Comment symbol? | **C** | Hash (`#`). |
| **5** | Indentation style? | **B** | Spaces strictly required; tabs forbidden. |
| **6** | String scalar example? | **A** | `name: Dilshad`. |
| **7** | Block list representation? | **B** | Hyphen + space (`- item`). |
| **8** | Flow-style sequence? | **B** | Square brackets `[Python, Java, Go]`. |
| **9** | Canonical Boolean true? | **A** | `true`. |
| **10** | Numeric integer? | **B** | `age: 25`. |
| **11** | Null representation? | **C** | The absence of a value (`null` or `~`). |
| **12** | Nested mapping syntax? | **B** | Two spaces of indentation under parent key. |
| **13** | Python dict equivalent? | **A** | Mapping (Key: Value). |
| **14** | Python list equivalent? | **B** | Sequence (Ordered collection). |
| **15** | Quotation marks purpose? | **B** | Preserve literal strings, spaces, and escape sequences. |
| **16** | Literal block scalar (preserves newlines)? | **A** | Pipe (`\|`). |
| **17** | Folded block scalar (folds to spaces)? | **B** | Greater-than (`>`). |
| **18** | Purpose of an anchor? | **B** | Reusing a node with an alias (`*`). |
| **19** | Anchor definition symbol? | **C** | Ampersand (`&`). |
| **20** | Anchor alias reference symbol? | **A** | Asterisk (`*`). |
| **21** | Start document marker? | **B** | Three hyphens (`---`). |
| **22** | Standard Python YAML library? | **C** | `PyYAML`. |
| **23** | Recommended safe loader function? | **B** | `yaml.safe_load()`. |
| **24** | Most common DevOps use case? | **A** | Application configs, Docker Compose, K8s, and CI/CD pipelines. |
