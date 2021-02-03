import boto3

client = boto3.client('iam')


all_policies = client.list_policies(
    Scope='Local'
)

customer_managed_policies = []

all_policies_length = len((all_policies['Policies']))

for i in range (all_policies_length):
    customer_managed_policies.append(all_policies['Policies'][i]['Arn'])

print(customer_managed_policies)

batch_infra_policies = []

for i in range(len(customer_managed_policies)):
    if "batch-infra" in customer_managed_policies[i]:
        batch_infra_policies.append(customer_managed_policies[i])

print(batch_infra_policies)
