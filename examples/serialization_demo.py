import yaml
import json

data = {
    "service": "authentication-api",
    "version": "2.4.0",
    "replicas": 3,
    "features": ["oauth2", "jwt", "rate-limiting"],
    "enabled": True
}

# 1. Serialization (Python -> YAML text)
yaml_text = yaml.dump(data, sort_keys=False)
print("=== Serialized YAML ===")
print(yaml_text)

# 2. Deserialization (YAML text -> Python Object)
parsed = yaml.safe_load(yaml_text)
print("=== Deserialized Python Dict ===")
print(parsed)
assert parsed["service"] == "authentication-api"
print("✓ Serialization roundtrip successful!")
