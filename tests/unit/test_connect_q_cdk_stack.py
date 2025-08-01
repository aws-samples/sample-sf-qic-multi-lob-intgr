import aws_cdk as core
import aws_cdk.assertions as assertions

from connect_q_cdk.connect_q_cdk_stack import ConnectQCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in connect_q_cdk/connect_q_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ConnectQCdkStack(app, "connect-q-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
