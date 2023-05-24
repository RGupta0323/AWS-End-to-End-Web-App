# can rename this file later. 
import os 
from constructs import Construct
from aws_cdk import (Stack, aws_lambda, aws_dynamodb, aws_kms)

class CdkStack(Stack): 
    def __init__(self, scope: Construct, id: str, **kwargs) -> None: 
        super().__init__(scope, id, **kwargs)
        # cdk code here... 