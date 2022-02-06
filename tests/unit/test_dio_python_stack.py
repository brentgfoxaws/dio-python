import aws_cdk as core
import aws_cdk.assertions as assertions

from dio_python.dio_python_stack import DioPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dio_python/dio_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DioPythonStack(app, "dio-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
