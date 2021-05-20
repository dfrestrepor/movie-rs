#!/usr/bin/env python3

# Purpose: Get SSM Parameter Store parameters
# Author:  Gary A. Stafford (December 2020)

import boto3

ssm_client = boto3.client('ssm')


def get_parameters():
    """Load parameter values from AWS Systems Manager (SSM) Parameter Store"""

    params = {
        'airflow_bucket': ssm_client.get_parameter(Name='/movie_sr/airflow_bucket')['Parameter']['Value'],
        'bootstrap_bucket': ssm_client.get_parameter(Name='/movie_sr/bootstrap_bucket')['Parameter']['Value'],
        'bronze_bucket': ssm_client.get_parameter(Name='/movie_sr/bronze_bucket')['Parameter']['Value'],
        'cluster_id': ssm_client.get_parameter(Name='/movie_sr/cluster_id')['Parameter']['Value'],
        'ec2_key_name': ssm_client.get_parameter(Name='/movie_sr/ec2_key_name')['Parameter']['Value'],
        'ec2_subnet_id': ssm_client.get_parameter(Name='/movie_sr/ec2_subnet_id')['Parameter']['Value'],
        'emr_ec2_role': ssm_client.get_parameter(Name='/movie_sr/emr_ec2_role')['Parameter']['Value'],
        'emr_role': ssm_client.get_parameter(Name='/movie_sr/emr_role')['Parameter']['Value'],
        'glue_db_bucket': ssm_client.get_parameter(Name='/movie_sr/glue_db_bucket')['Parameter']['Value'],
        'gold_bucket': ssm_client.get_parameter(Name='/movie_sr/gold_bucket')['Parameter']['Value'],
        'logs_bucket': ssm_client.get_parameter(Name='/movie_sr/logs_bucket')['Parameter']['Value'],
        'master_public_dns': ssm_client.get_parameter(Name='/movie_sr/master_public_dns')['Parameter']['Value'],
        'silver_bucket': ssm_client.get_parameter(Name='/movie_sr/silver_bucket')['Parameter']['Value'],
        'sm_log_group_arn': ssm_client.get_parameter(Name='/movie_sr/sm_log_group_arn')['Parameter']['Value'],
        'sm_role_arn': ssm_client.get_parameter(Name='/movie_sr/sm_role_arn')['Parameter']['Value'],
        'vpc_id': ssm_client.get_parameter(Name='/movie_sr/vpc_id')['Parameter']['Value'],
        'work_bucket': ssm_client.get_parameter(Name='/movie_sr/work_bucket')['Parameter']['Value']
    }

    return params
