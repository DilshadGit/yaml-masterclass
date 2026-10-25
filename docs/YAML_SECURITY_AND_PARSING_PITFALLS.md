# YAML Security & Parsing Pitfalls

Comprehensive technical analysis of YAML spec quirks, common developer bugs, and security vulnerabilities.

---

## 1. The Norway Problem (Boolean Coercion)
In YAML 1.1, unquoted `NO` is coerced to boolean `false`.
```yaml
# BUG:
country_code: NO   # Evaluates to boolean: False!

# FIX:
country_code: "NO" # Evaluates to string: "NO"
```

## 2. Accidental Octal and Sexagesimal Numbers
```yaml
# BUG: Leading zeroes evaluate to octal or strings depending on parser version:
user_pin: 0123     # May parse as 83 in decimal or throw syntax error

# FIX: Always quote numeric codes:
user_pin: "0123"
```

## 3. Billion Laughs / Entity Expansion Attacks
Never use `yaml.load()` without `SafeLoader` in Python:
```python
# VULNERABLE TO REMOTE CODE EXECUTION:
data = yaml.load(user_input, Loader=yaml.Loader)

# SECURE:
data = yaml.safe_load(user_input)
```
