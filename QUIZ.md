# YAML Specification & Cloud-Native Architecture - Masterclass Examination (24 Questions)

> **Instructions**: Test your comprehensive knowledge across all 6 core levels and industrial practices. Each question contains four choices with exactly one correct answer. An in-depth Answer Key with technical explanations is provided at the bottom.

## Questions

### Question 1
**Which character is strictly prohibited for block indentation in valid YAML configuration files?**

- **A)** Space character
- **B)** Tab character (\\t)
- **C)** Hyphen followed by space
- **D)** Colon followed by space

### Question 2
**What is the universal industry standard indentation level for YAML cloud configurations (Kubernetes, Compose, CI/CD)?**

- **A)** 1 space
- **B)** 2 spaces
- **C)** 4 spaces
- **D)** 8 spaces

### Question 3
**Which syntax is used to represent an item in an ordered YAML sequence (list)?**

- **A)** key: value
- **B)** - item (hyphen followed by a space)
- **C)** * item (asterisk)
- **D)** item; (trailing semicolon)

### Question 4
**What is the famous 'Norway Problem' in YAML 1.1 parsers?**

- **A)** YAML cannot represent Scandinavian character encodings
- **B)** The unquoted two-letter country code 'no' is automatically parsed as a Boolean False
- **C)** YAML parsers crash when encountering European decimal commas
- **D)** Country codes must be prefixed with an ISO tag

### Question 5
**What is the semantic distinction between the pipe '|' and greater-than '>' multiline string operators in YAML?**

- **A)** | folds lines into a single sentence; > preserves literal newlines
- **B)** | preserves literal newlines (literal block); > folds newlines into spaces (folded block)
- **C)** | is reserved for comment blocks; > is for string templates
- **D)** | indicates a list of strings; > indicates a key-value mapping

### Question 6
**How do you declare a reusable anchor in YAML and subsequently reference (alias) it?**

- **A)** Declare with &anchor_name; reference with *anchor_name
- **B)** Declare with @anchor_name; reference with #anchor_name
- **C)** Declare with $anchor_name; reference with %anchor_name
- **D)** Declare with ref: anchor_name; reference with use: anchor_name

### Question 7
**Which operator is used to merge all keys from an anchored mapping into another mapping in YAML?**

- **A)** &&:
- **B)** merge:
- **C)** <<:
- **D)** ++:

### Question 8
**Which of the following demonstrates valid YAML compact inline flow sequence syntax?**

- **A)** branches: (main, staging)
- **B)** branches: [ 'main', 'staging' ]
- **C)** branches: <main, staging>
- **D)** branches: { main, staging }

### Question 9
**Which character initiates a single-line comment in YAML files?**

- **A)** //
- **B)** --
- **C)** #
- **D)** /*

### Question 10
**In Kubernetes manifest YAML files, which top-level attribute identifies the schema version of the resource?**

- **A)** kind
- **B)** apiVersion
- **C)** metadata
- **D)** spec

### Question 11
**Which scalar data type is inferred by YAML parsers for unquoted values 'true' and 'false'?**

- **A)** String
- **B)** Boolean
- **C)** Symbol
- **D)** Null

### Question 12
**Which syntax represents a null (empty) value in standard YAML documents?**

- **A)** null or ~ (tilde)
- **B)** void
- **C)** nil
- **D)** none()

### Question 13
**What occurs when a colon in a key-value mapping is not followed by a space (e.g. 'port:8080')?**

- **A)** It parses successfully as key 'port' and integer 8080
- **B)** It is parsed as a single plain string scalar 'port:8080' rather than a key-value mapping
- **C)** The YAML parser automatically inserts a space
- **D)** It creates an anonymous sequence

### Question 14
**In Docker Compose YAML, what is the architectural function of the 'depends_on' configuration key?**

- **A)** Defines CPU cores and memory allocations for the container
- **B)** Specifies container startup dependency order between services (e.g., web waiting for db)
- **C)** Binds container ports directly to host IP addresses
- **D)** Enforces volume backup frequency

### Question 15
**Which character token separates multiple distinct YAML documents within a single physical file stream?**

- **A)** --- (three hyphens)
- **B)** === (three equals)
- **C)** ### (three hashes)
- **D)** ::: (three colons)

### Question 16
**Which token denotes the formal end of a YAML document stream without opening a subsequent document?**

- **A)** ... (three periods)
- **B)** ---
- **C)** ###
- **D)** EOF

### Question 17
**In GitHub Actions CI/CD workflows, which top-level YAML key declares the triggers or webhook events that initiate the pipeline?**

- **A)** runs-on
- **B)** on
- **C)** jobs
- **D)** steps

### Question 18
**In YAML chomping indicators, what does placing a minus sign after a block operator (|- or >-) signify?**

- **A)** Strip all trailing newlines and whitespace from the scalar string
- **B)** Preserve all trailing newlines and blank lines
- **C)** Indents the block by negative two spaces
- **D)** Encrypts the resulting string using AES

### Question 19
**In YAML chomping indicators, what does placing a plus sign after a block operator (|+ or >+) signify?**

- **A)** Preserve all trailing newlines and trailing whitespace at the conclusion of the string
- **B)** Strip all newlines completely
- **C)** Prepend a leading newline to the string
- **D)** Automatically convert tabs to spaces

### Question 20
**Which PyYAML loading function is considered the secure DevOps industry standard to prevent arbitrary code execution vulnerabilities?**

- **A)** yaml.load()
- **B)** yaml.safe_load()
- **C)** yaml.unsafe_load()
- **D)** yaml.eval()

### Question 21
**What data structure does a YAML document root compile into when reading key-value mappings?**

- **A)** Linked list
- **B)** Associative array (Dictionary / Map / Object)
- **C)** Relational table
- **D)** Binary tree

### Question 22
**How can you explicitly force a YAML parser to treat a scalar as a string or integer using standard tags?**

- **A)** !!str '123' or !!int 456
- **B)** $str '123' or $int 456
- **C)** (string)'123' or (int)456
- **D)** cast:string -> '123'

### Question 23
**What is the formal relationship between the JSON data format and YAML 1.2?**

- **A)** JSON and YAML are completely incompatible and mutually exclusive formats
- **B)** JSON is a strict mathematical and syntactic subset of YAML 1.2
- **C)** YAML is a binary encoding of JSON
- **D)** YAML cannot deserialize JSON objects with nested arrays

## Comprehensive Answer Key & Technical Explanations

### Q1: **Option B** — `Tab character (\\t)`

- **Deep Technical Rationale**: The YAML specification strictly forbids **tab characters (\\t)** for block indentation; indentation must consist solely of spaces.

### Q2: **Option B** — `2 spaces`

- **Deep Technical Rationale**: Modern cloud infrastructure manifests (Kubernetes, Docker Compose, GitHub Actions) universally standardize on **2 spaces** per level.

### Q3: **Option B** — `- item (hyphen followed by a space)`

- **Deep Technical Rationale**: YAML sequences (lists) use a **hyphen followed by at least one space (`- item`)**.

### Q4: **Option B** — `The unquoted two-letter country code 'no' is automatically parsed as a Boolean False`

- **Deep Technical Rationale**: In YAML 1.1, unquoted `no`, `yes`, `on`, and `off` are evaluated as boolean values. Country code `no` becomes `False`.

### Q5: **Option B** — `| preserves literal newlines (literal block); > folds newlines into spaces (folded block)`

- **Deep Technical Rationale**: The **pipe (|)** preserves literal line breaks (ideal for bash scripts); the **greater-than (>)** folds lines into a continuous sentence.

### Q6: **Option A** — `Declare with &anchor_name; reference with *anchor_name`

- **Deep Technical Rationale**: YAML anchors are defined using an ampersand (**&name**) and referenced using an asterisk alias (***name**).

### Q7: **Option C** — `<<:`

- **Deep Technical Rationale**: The merge key operator (**<<: *anchor**) injects all key-value mappings from the referenced anchor into the target dictionary.

### Q8: **Option B** — `branches: [ 'main', 'staging' ]`

- **Deep Technical Rationale**: YAML supports compact flow sequences using JSON-style square brackets: `[ 'item1', 'item2' ]`.

### Q9: **Option C** — `#`

- **Deep Technical Rationale**: Comments in YAML begin with the hash (**#**) character and extend to the end of that line.

### Q10: **Option B** — `apiVersion`

- **Deep Technical Rationale**: **apiVersion** specifies the versioned schema (e.g., `apps/v1`, `v1`) against which Kubernetes evaluates the resource definition.

### Q11: **Option B** — `Boolean`

- **Deep Technical Rationale**: Unquoted `true` and `false` are automatically cast to native boolean primitives.

### Q12: **Option A** — `null or ~ (tilde)`

- **Deep Technical Rationale**: YAML represents null values using either the literal `null` keyword or a solitary tilde (`~`).

### Q13: **Option B** — `It is parsed as a single plain string scalar 'port:8080' rather than a key-value mapping`

- **Deep Technical Rationale**: YAML mappings mandate whitespace after the colon; without space, `port:8080` is evaluated as a single string literal.

### Q14: **Option B** — `Specifies container startup dependency order between services (e.g., web waiting for db)`

- **Deep Technical Rationale**: **depends_on** expresses startup and shutdown sequencing between services when executing `docker compose up`.

### Q15: **Option A** — `--- (three hyphens)`

- **Deep Technical Rationale**: Three hyphens (**---**) mark the beginning of a new YAML document within a multi-document file.

### Q16: **Option A** — `... (three periods)`

- **Deep Technical Rationale**: Three dots (**...**) explicitly signal the termination of a document in a stream.

### Q17: **Option B** — `on`

- **Deep Technical Rationale**: The **on** key defines repository events (e.g., `push`, `pull_request`, `schedule`) that trigger the workflow.

### Q18: **Option A** — `Strip all trailing newlines and whitespace from the scalar string`

- **Deep Technical Rationale**: The strip chomping indicator (**|-** or **>-**) discards all trailing newlines from the final rendered string.

### Q19: **Option A** — `Preserve all trailing newlines and trailing whitespace at the conclusion of the string`

- **Deep Technical Rationale**: The keep chomping indicator (**|+** or **>+**) preserves all trailing newlines and whitespace intact.

### Q20: **Option B** — `yaml.safe_load()`

- **Deep Technical Rationale**: **yaml.safe_load()** restricts parsing to standard scalar types and collections, preventing remote arbitrary object instantiation attacks.

### Q21: **Option B** — `Associative array (Dictionary / Map / Object)`

- **Deep Technical Rationale**: YAML key-value mappings compile into an associative array (Python `dict`, JavaScript `Object`, Go `map`).

### Q22: **Option A** — `!!str '123' or !!int 456`

- **Deep Technical Rationale**: YAML explicit type tags begin with double exclamation marks (**!!str**, **!!int**, **!!float**, **!!bool**).

### Q23: **Option B** — `JSON is a strict mathematical and syntactic subset of YAML 1.2`

- **Deep Technical Rationale**: By formal specification, **JSON is a strict syntactic subset of YAML 1.2**; every valid JSON document is valid YAML 1.2.
