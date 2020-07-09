import boto
import sys
conn= boto.ec2.connection.EC2connection()
inst_type=sys.argv[1]
instances=conn.get_all_instances(filter={'instance_type';inst_type})
else;
instances=conn.get_all_instances()
for instance in instances;
print(instance.id,instance.instance_type)