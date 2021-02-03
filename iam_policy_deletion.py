import boto3

client = boto3.client('iam')


## List of attached policies ARN

attached_policies = client.list_policies(
    Scope='Local',
    OnlyAttached=True
)

arn_attached_policies = []

attached_policies_length = len((attached_policies['Policies']))

for i in range (attached_policies_length):
    arn_attached_policies.append(attached_policies['Policies'][i]['Arn'])


## List of all customer managed policies ARN with string "batch-infra"

all_policies = client.list_policies(
    Scope='Local'
)

customer_managed_policies = []

all_policies_length = len((all_policies['Policies']))

for i in range (all_policies_length):
    customer_managed_policies.append(all_policies['Policies'][i]['Arn'])

batch_infra_policies = []

for i in range(len(customer_managed_policies)):
    if "batch-infra" in customer_managed_policies[i]:
        batch_infra_policies.append(customer_managed_policies[i])


## List of ARN's that are to be deleted

policy_deletion_list = list(set(batch_infra_policies) - set(arn_attached_policies))


## Deletion API call

for i in range(len(policy_deletion_list)):
    delete_unused_policies = client.delete_policy(
    PolicyArn= policy_deletion_list[i]
)

print("Deleted unused policies")






