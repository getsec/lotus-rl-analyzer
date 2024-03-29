import yaml


def load_yaml(path):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return config
