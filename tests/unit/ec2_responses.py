"""Static data for EC2 stubbing."""

from datetime import datetime

EC2_DESCRIBE_INSTANCES_RESPONSE = {
    'Reservations': [
        {
            'Groups': [],
            'Instances': [
                {
                    'AmiLaunchIndex': 0,
                    'Architecture': 'x86_64',
                    'BlockDeviceMappings': [],
                    'CapacityReservationSpecification': {
                        'CapacityReservationPreference': 'open'
                    },
                    'ClientToken': '00000000-0000-0000-0000-000000000000_\
                            subnet-00000000_0',
                    'CpuOptions': {
                        'CoreCount': 1,
                        'ThreadsPerCore': 1
                    },
                    'EbsOptimized': False,
                    'EnaSupport': True,
                    'HibernationOptions': {'Configured': False},
                    'Hypervisor': 'xen',
                    'ImageId': 'ami-00000000000000000',
                    'InstanceId': 'i-00000000000000000',
                    'InstanceType': 't2.small',
                    'KeyName': 'ssh.key',
                    'LaunchTime': datetime.utcnow(),
                    'Monitoring': {'State': 'enabled'},
                    'NetworkInterfaces': [],
                    'Placement': {
                        'AvailabilityZone': 'us-east-1d',
                        'GroupName': '',
                        'Tenancy': 'default'
                    },
                    'PrivateDnsName': '',
                    'ProductCodes': [],
                    'PublicDnsName': '',
                    'RootDeviceName': 'xvda',
                    'RootDeviceType': 'ebs',
                    'SecurityGroups': [],
                    'State': {
                        'Code': 48,
                        'Name': 'terminated'
                    },
                    'StateReason': {
                        'Code': 'Client.UserInitiatedShutdown',
                        'Message': 'Client.UserInitiatedShutdown: User \
                                initiated shutdown'
                    },
                    'StateTransitionReason': 'User initiated (2019-05-30 \
                            13:23:50 GMT)',
                    'Tags': [
                        {
                            'Key': 'SampleTag1',
                            'Value': 'SampleTagValue1'
                        }
                    ],
                    'VirtualizationType': 'hvm'
                }
            ],
            'OwnerId': '000000000000',
            'RequesterId': '000000000000',
            'ReservationId': 'r-00000000000000000'
        },
        {
            'Groups': [],
            'Instances': [
                {
                    'AmiLaunchIndex': 0,
                    'Architecture': 'x86_64',
                    'BlockDeviceMappings': [],
                    'CapacityReservationSpecification': {
                        'CapacityReservationPreference': 'open'
                    },
                    'ClientToken': 'xxxxx-xxxxx-xxxxxxxxxxxxx',
                    'CpuOptions': {
                        'CoreCount': 1,
                        'ThreadsPerCore': 1
                    },
                    'EbsOptimized': False,
                    'EnaSupport': True,
                    'HibernationOptions': {'Configured': False},
                    'Hypervisor': 'xen',
                    'ImageId': 'ami-xxxxxxxxxxxxxxxxx',
                    'InstanceId': 'i-xxxxxxxxxxxxxxxxx',
                    'InstanceType': 't2.micro',
                    'KeyName': 'ssh.key',
                    'LaunchTime': datetime.utcnow(),
                    'Monitoring': {'State': 'disabled'},
                    'NetworkInterfaces': [],
                    'Placement': {
                        'AvailabilityZone': 'us-east-1d',
                        'GroupName': '',
                        'Tenancy': 'default'
                    },
                    'PrivateDnsName': '',
                    'ProductCodes': [],
                    'PublicDnsName': '',
                    'RootDeviceName': 'xvda',
                    'RootDeviceType': 'ebs',
                    'SecurityGroups': [],
                    'State': {
                        'Code': 48,
                        'Name': 'terminated'
                    },
                    'StateReason': {
                        'Code': 'Client.UserInitiatedShutdown',
                        'Message': 'Client.UserInitiatedShutdown: User \
                                initiated shutdown'
                    },
                    'StateTransitionReason': 'User initiated (2019-05-30 \
                            13:23:31 GMT)',
                    'Tags': [
                        {
                            'Key': 'SampleTag1',
                            'Value': 'SampleTagValue1'
                        }
                    ],
                    'VirtualizationType': 'hvm'
                }
            ],
            'OwnerId': 'xxxxxxxxxxxx',
            'RequesterId': 'xxxxxxxxxxxx',
            'ReservationId': 'r-xxxxxxxxxxxxxxxxx'
        },
        {
            'Groups': [],
            'Instances': [
                {
                    'AmiLaunchIndex': 0,
                    'Architecture': 'x86_64',
                    'BlockDeviceMappings': [
                        {
                            'DeviceName': 'xvda',
                            'Ebs': {
                                'AttachTime': datetime.utcnow(),
                                'DeleteOnTermination': True,
                                'Status': 'attached',
                                'VolumeId': 'vol-AAAAAAAAAAAAAAAAA'
                            }
                        }
                    ],
                    'CapacityReservationSpecification': {
                        'CapacityReservationPreference': 'open'
                    },
                    'ClientToken': 'AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA_\
                            subnet-AAAAAAAA_A',
                    'CpuOptions': {
                        'CoreCount': 1,
                        'ThreadsPerCore': 1
                    },
                    'EbsOptimized': False,
                    'EnaSupport': True,
                    'HibernationOptions': {'Configured': False},
                    'Hypervisor': 'xen',
                    'ImageId': 'ami-AAAAAAAAAAAAAAAAA',
                    'InstanceId': 'i-AAAAAAAAAAAAAAAAA',
                    'InstanceType': 't2.small',
                    'LaunchTime': datetime.utcnow(),
                    'Monitoring': {'State': 'enabled'},
                    'NetworkInterfaces': [
                        {
                            'Association': {
                                'IpOwnerId': 'amazon',
                                'PublicDnsName': 'ec2-3-81-252-87.\
                                        compute-1.amazonaws.com',
                                'PublicIp': '3.81.252.87'
                            },
                            'Attachment': {
                                'AttachTime': datetime.utcnow(),
                                'AttachmentId': 'eni-attach-AAAAAAAAAAAAAAAAA',
                                'DeleteOnTermination': True,
                                'DeviceIndex': 0,
                                'Status': 'attached'
                            },
                            'Description': '',
                            'Groups': [
                                {
                                    'GroupId': 'sg-AAAAAAAA',
                                    'GroupName': 'default'
                                }
                            ],
                            'InterfaceType': 'interface',
                            'Ipv6Addresses': [],
                            'MacAddress': '0e:91:94:7e:e5:2a',
                            'NetworkInterfaceId': 'eni-AAAAAAAAAAAAAAAAA',
                            'OwnerId': 'AAAAAAAAAAAA',
                            'PrivateDnsName': 'ip-172-31-38-42.ec2.internal',
                            'PrivateIpAddress': '172.31.38.42',
                            'PrivateIpAddresses': [
                                {
                                    'Association': {
                                        'IpOwnerId': 'amazon',
                                        'PublicDnsName': 'ec2-3-81-252-87.\
                                                compute-1.amazonaws.com',
                                        'PublicIp': '3.81.252.87'
                                    },
                                    'Primary': True,
                                    'PrivateDnsName': 'ip-172-31-38-42.\
                                            ec2.internal',
                                    'PrivateIpAddress': '172.31.38.42'
                                }
                            ],
                            'SourceDestCheck': True,
                            'Status': 'in-use',
                            'SubnetId': 'subnet-AAAAAAAA',
                            'VpcId': 'vpc-AAAAAAAA'
                        }
                    ],
                    'Placement': {
                        'AvailabilityZone': 'us-east-1d',
                        'GroupName': '',
                        'Tenancy': 'default'
                    },
                    'PrivateDnsName': 'ip-172-31-38-42.ec2.internal',
                    'PrivateIpAddress': '172.31.38.42',
                    'ProductCodes': [],
                    'PublicDnsName': 'ec2-3-81-252-87.compute-1.amazonaws.com',
                    'PublicIpAddress': '3.81.252.87',
                    'RootDeviceName': 'xvda',
                    'RootDeviceType': 'ebs',
                    'SecurityGroups': [
                        {
                            'GroupId': 'sg-AAAAAAAA',
                            'GroupName': 'default'
                        }
                    ],
                    'SourceDestCheck': True,
                    'State': {
                        'Code': 16,
                        'Name': 'running'
                    },
                    'StateTransitionReason': '',
                    'SubnetId': 'subnet-AAAAAAAA',
                    'Tags': [
                        {
                            'Key': 'SampleTag1',
                            'Value': 'SampleTagValue1'
                        }
                    ],
                    'VirtualizationType': 'hvm',
                    'VpcId': 'vpc-AAAAAAAA'
                }
            ],
            'OwnerId': 'AAAAAAAAAAAA',
            'RequesterId': 'AAAAAAAAAAAA',
            'ReservationId': 'r-AAAAAAAAAAAAAAAAA'
        },
        {
            'Groups': [],
            'Instances': [
                {
                    'AmiLaunchIndex': 0,
                    'Architecture': 'x86_64',
                    'BlockDeviceMappings': [
                        {
                            'DeviceName': '/dev/sda1',
                            'Ebs': {
                                'AttachTime': datetime.utcnow(),
                                'DeleteOnTermination': False,
                                'Status': 'attached',
                                'VolumeId': 'vol-BBBBBBBBBBBBBBBBB'
                            }
                        }
                    ],
                    'CapacityReservationSpecification': {
                        'CapacityReservationPreference': 'open'
                    },
                    'ClientToken': 'BBBBBBBBBBBBBBBBBB',
                    'CpuOptions': {
                        'CoreCount': 1,
                        'ThreadsPerCore': 1
                    },
                    'EbsOptimized': False,
                    'EnaSupport': True,
                    'HibernationOptions': {'Configured': False},
                    'Hypervisor': 'xen',
                    'ImageId': 'ami-BBBBBBBBBBBBBBBBB',
                    'InstanceId': 'i-BBBBBBBBBBBBBBBBB',
                    'InstanceType': 't2.micro',
                    'LaunchTime': datetime.utcnow(),
                    'Monitoring': {'State': 'disabled'},
                    'NetworkInterfaces': [
                        {
                            'Association': {
                                'IpOwnerId': 'amazon',
                                'PublicDnsName': 'ec2-54-146-180-121.\
                                        compute-1.amazonaws.com',
                                'PublicIp': '54.146.180.121'
                            },
                            'Attachment': {
                                'AttachTime': datetime.utcnow(),
                                'AttachmentId': 'eni-attach-BBBBBBBBBBBBBBBBB',
                                'DeleteOnTermination': True,
                                'DeviceIndex': 0,
                                'Status': 'attached'
                            },
                            'Description': '',
                            'Groups': [
                                {
                                    'GroupId': 'sg-BBBBBBBBBBBBBBBBB',
                                    'GroupName': 'B'
                                }
                            ],
                            'InterfaceType': 'interface',
                            'Ipv6Addresses': [],
                            'MacAddress': '12:46:45:df:fc:a8',
                            'NetworkInterfaceId': 'eni-BBBBBBBBBBBBBBBBB',
                            'OwnerId': 'BBBBBBBBBBBB',
                            'PrivateDnsName': 'ip-172-31-71-43.ec2.internal',
                            'PrivateIpAddress': '172.31.71.43',
                            'PrivateIpAddresses': [
                                {
                                    'Association': {
                                        'IpOwnerId': 'amazon',
                                        'PublicDnsName': 'ec2-54-146-80-21.\
                                                compute-1.amazonaws.com',
                                        'PublicIp': '54.146.80.21'
                                    },
                                    'Primary': True,
                                    'PrivateDnsName': 'ip-172-31-71-43.\
                                            ec2.internal',
                                    'PrivateIpAddress': '172.31.71.43'
                                }
                            ],
                            'SourceDestCheck': True,
                            'Status': 'in-use',
                            'SubnetId': 'subnet-BBBBBBBB',
                            'VpcId': 'vpc-BBBBBBBB'
                        }
                    ],
                    'Placement': {
                        'AvailabilityZone': 'us-east-1e',
                        'GroupName': '',
                        'Tenancy': 'default'
                    },
                    'PrivateDnsName': 'ip-172-31-71-43.ec2.internal',
                    'PrivateIpAddress': '172.31.71.43',
                    'ProductCodes': [
                        {
                            'ProductCodeId': 'BBBBBBBBBBBBBBBBBBBBBBBBB',
                            'ProductCodeType': 'marketplace'
                        }
                    ],
                    'PublicDnsName': 'ec2-54-146-180-121.\
                            compute-1.amazonaws.com',
                    'PublicIpAddress': '54.146.180.121',
                    'RootDeviceName': '/dev/sda1',
                    'RootDeviceType': 'ebs',
                    'SecurityGroups': [
                        {
                            'GroupId': 'sg-BBBBBBBBBBBBBBBBB',
                            'GroupName': 'B'
                        }
                    ],
                    'SourceDestCheck': True,
                    'State': {
                        'Code': 16,
                        'Name': 'running'
                    },
                    'StateTransitionReason': '',
                    'SubnetId': 'subnet-BBBBBBBB',
                    'VirtualizationType': 'hvm',
                    'VpcId': 'vpc-BBBBBBBB'
                }
            ],
            'OwnerId': 'BBBBBBBBBBBB',
            'RequesterId': 'BBBBBBBBBBBB',
            'ReservationId': 'r-BBBBBBBBBBBBBBBBB'
        }
    ],
    'ResponseMetadata': {
        'HTTPHeaders': {
            'content-type': 'text/xml;charset=UTF-8',
            'date': 'Thu, 30 May 2019 13:51:39 GMT',
            'server': 'AmazonEC2',
            'transfer-encoding': 'chunked',
            'vary': 'accept-encoding'
        },
        'HTTPStatusCode': 200,
        'RequestId': '------------------------------------',
        'RetryAttempts': 0
    }
}
