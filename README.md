# shotty
Project which takes the snapshot of amazon EC2 instances

## About
This project uses the boto3 to manage AWS EC2 instance snapshot.

## Configure
shotty uses the configuration used by AWS CLI e.g

`aws configure --profile shotty`

## Running

`pipenv run "python shotty/shotty.py <command> <subcommand> <--project=PROJECT>"`

*Command* is list, snapshot, start or stop
*Subcommand* depends on command
*project*  is optional


