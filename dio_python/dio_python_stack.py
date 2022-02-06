from aws_cdk import (
    Stack,
    aws_codepipeline,
    aws_codepipeline_actions,
    aws_s3
)
from constructs import Construct

class DioPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the inital pipeline
        pipeline = aws_codepipeline.Pipeline(self, "DioPythonPipeline",
            pipeline_name="DioPythonPipeline"
        )

        # Check out the original source from GitHub
        source_output = aws_codepipeline.Artifact()
        source_action = aws_codepipeline_actions.CodeStarConnectionsSourceAction(
            action_name="Code_Source",
            owner="brentgfoxaws",
            repo="goa-test-app",
            connection_arn="arn:aws:codestar-connections:us-west-2:492199546644:connection/5054d256-4253-4d4b-aeed-3828a581ffba",
            output=source_output
        )
        pipeline.add_stage(
            stage_name="Source",
            actions=[source_action]
        )
        
        target_bucket = aws_s3.Bucket(self, "dio-pipeline-test-output")
        deploy_stage = pipeline.add_stage(stage_name="Deploy")
        deploy_stage.add_action(aws_codepipeline_actions.S3DeployAction(
                action_name="s3-deploy-action",
                input=source_output,
                bucket=target_bucket
            )
        )