import os
import json

def generatePolicy(principalId, effect, methodArn):
    authResponse = {}
    authResponse['principalId'] = principalId
 
    if effect and methodArn:
        policyDocument = {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Sid': 'FirstStatement',
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': methodArn
                }
            ]
        }
 
        authResponse['policyDocument'] = policyDocument
 
    return authResponse

def return_http_code(code, item):
    return {
        'statusCode': code,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-All,ow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(item)
    }

def exception_handler(e):
    # exception to status code mapping goes here...
    return return_http_code(500,  {'message': str(e), "error": True, "success": False, "data": None})    
