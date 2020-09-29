import json
from pprint import pprint
import yaml
from configparser import ConfigParser

# INI
config = ConfigParser()
config.read("../extras/config.ini")

sections = config.sections()
print(sections)
for section in sections:
    opts = config.options(section)
    for opt in opts:
        value = config.get(section, opt)
        print(f"sekcja={section}, opcja={opt}, wartosc={value}")

value = config.get("GeneraL", "COMpiler", fallback="Unknown")
print(value)
print("="*80)

# JSON
with open("../extras/config.json") as fd:
    json_config = json.load(fd)
    pprint(json_config, indent=4)
    json_config["manufacturer"] = "CISCO"
    with open("config-new.json","wt") as fd2:
        json.dump(json_config, fd2 )

print("="*80)
# YAML
with open("../extras/config.yaml", "rt") as fd:
    items = list(yaml.load_all(fd, Loader=yaml.FullLoader))
    for item in items:
        for k,v in item.items():
            print(f"{k} -> {v}")
