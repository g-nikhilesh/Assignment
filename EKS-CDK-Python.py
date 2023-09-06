from aws_cdk import (
    aws_eks as eks,
    aws_ec2 as ec2,
    aws_iam as iam,
    core
)

class EksClusterStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # import default VPC
        vpc = ec2.Vpc(self, 'MyVPC', max_azs=3)

        # Create an IAM role
        eks_admin_role = aws_iam.Role(self, 'AdminRole',
                                      assumed_by=aws_iam.AccountPrincipal(
                                          account_id=self.account)
        )

    

        # Create the EKS cluster
        cluster = eks.Cluster(self, 'MyEksCluster',
            default_capacity=0, 
            vpc=vpc,
            default_capacity_instance=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
          
        )

      
        cluster.add_auto_scaling_group_capacity('MyNodes',
            min_capacity=, 
            max_capacity=, 
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
        )
