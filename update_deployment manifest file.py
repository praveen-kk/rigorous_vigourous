import yaml

# Read the Deployment manifest file
with open('deployment.yaml', 'r') as file:
    deployment_manifest = yaml.safe_load(file)

# Modify the desired fields in the Deployment manifest
deployment_manifest['spec']['replicas'] = 100
deployment_manifest['spec']['template']['spec']['containers'][0]['image'] = 'new-image:latest'

# Write the updated Deployment manifest back to the file
with open('deployment.yaml', 'w') as file:
    yaml.dump(deployment_manifest, file)
    file.close()
print(deployment_manifest)



# import yaml
# with open('manifestfile.yaml', 'r') as file:
#     mani_fest_file = yaml.safe_load(file)
