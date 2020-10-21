import json


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))

    return {
        'statuCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }
