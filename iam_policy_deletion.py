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

customer_managed_policies = client.list_policies(
    Scope='Local'
)

arn_customer_managed_policies = []

customer_managed_policies_length = len((customer_managed_policies['Policies']))

for i in range (customer_managed_policies_length):
    arn_customer_managed_policies.append(customer_managed_policies['Policies'][i]['Arn'])

attached_batch_infra_policies = []

for i in range(len(arn_customer_managed_policies)):
    if arn_customer_managed_policies[i].endswith("batch-job-policy"):
        attached_batch_infra_policies.append(arn_customer_managed_policies[i])


## List of ARN's that are to be deleted

arn_policy_deletion_list = list(set(attached_batch_infra_policies) - set(arn_attached_policies))


## Deletion API call

for i in range(len(arn_policy_deletion_list)):
    delete_unused_policies = client.delete_policy(
    PolicyArn= arn_policy_deletion_list[i]
)

print("Deleted unused policies with substring 'batch-infra' ")






