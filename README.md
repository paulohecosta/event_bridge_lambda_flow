# event_bridge_lambda_flow

## TEST
sam local invoke "ExampleOne" --env-vars env.json

## Build on AWS

`aws cloudformation package --template-file template.yaml --s3-bucket coins-artifacts --s3-prefix builds --output-template-file template-output.yaml --profile personal`
## Deploy on AWS

`aws cloudformation deploy --template-file template-output.yaml --s3-bucket coins-artifacts --s3-prefix builds --stack-name event-bridge-example --capabilities CAPABILITY_NAMED_IAM --profile personal --parameter-overrides $(jq -r '.Parameters | to_entries | map("\(.key)=\(.value|tostring)") | .[]' config.json)`

### References

https://lumigo.io/blog/5-reasons-why-you-should-use-eventbridge-instead-of-sns/

https://aws.amazon.com/pt/blogs/compute/reducing-custom-code-by-using-advanced-rules-in-amazon-eventbridge/

http://man.hubwiz.com/docset/Boto3.docset/Contents/Resources/Documents/guide/cw-example-events.html


### Slide Presentation

#### Design Pattern - Domínios Online Agnósticos e Arquitetura a Evento Low Code

#### Design Pattern - Observabilidade no Barramentos de Eventos com SNS/EventBridge

#### Comparação de Custo - Os 64kb de cada Evento

SNS, SQS e Event Bridge Transitam registros de até 256kb
64kb cobra 1 transação -> 256kb cobram 4!!!
