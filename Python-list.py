# Initialing the array of AWS services
aws_services = []

# Appending items to list
aws_services.append('vpc')
aws_services.append('lambda')
aws_services.append('EC2')
aws_services.append('S3')
aws_services.append('RDS')

# Printing my list of AWS services
print(aws_services)

# Assigning a variable to the lenght of array
lenght_aws_services = len (aws_services)

# Printing my lenght of array
print('the lenght of array is', lenght_aws_services) 

# Removing two AWS services from my array
aws_services.remove('S3')
aws_services.remove('EC2')

#Assigning a variable to my new lenght of array
new_lenght_aws_services = len (aws_services)

# Printing my new list and the lenght of my new list
print(aws_services)
print('the lenght of array is', new_lenght_aws_services)



