#!/usr/bin/env python3
"""Demonstrates Anchor (&), Alias (*), and Merge Key (<<:) resolution"""
import yaml

raw_yaml = """
base_config: &base
  timeout: 30
  retry: 3
  debug: false

service_a:
  <<: *base
  endpoint: "https://a.api.io"

service_b:
  <<: *base
  endpoint: "https://b.api.io"
  retry: 5 # override base
"""

def main():
    data = yaml.safe_load(raw_yaml)
    print("Resolved YAML dictionary:")
    print(data)
    print("\nRe-serialized normalized YAML:")
    print(yaml.dump(data, default_flow_style=False))

if __name__ == "__main__":
    main()
