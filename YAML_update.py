import yaml
with open('config.yaml') as file:
    try:
        data = yaml.safe_load(file)
        for key, value in data.items():
            print(key, ":", value)
    except yaml.YAMLError as exception:
        print(exception)