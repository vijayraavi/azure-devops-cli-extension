# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


def transform_banner_table_output(result):
    table_output = []
    for k, v in result.items():
        table_output.append(_transform_banner_row(k, v))
    return table_output


def _transform_banner_row(key, value):
    table_row = OrderedDict()
    table_row['ID'] = key
    if 'message' in value:
        table_row['Message'] = value['message']
    else:
        table_row['Message'] = ' '
    if 'level' in value:
        level = value['level']
        if level is not None and level != '':
            level = level[0:1].upper() + level[1:]
        table_row['Level'] = level
    else:
        table_row['Level'] = 'Info'
    if 'expirationDate' in value:
        table_row['Expiration Date'] = value['expirationDate']
    else:
        table_row['Expiration Date'] = ' '
    return table_row


def transform_users_table_output(result):
    table_output = []
    for item in result:
        table_output.append(_transform_users_row(item))
    return table_output


def transform_user_table_output(result):
    table_output = [_transform_users_row(result)]
    return table_output


def _transform_users_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    if 'user' in row:
        table_row['Display Name'] = row['user']['displayName']
    else:
        table_row['Display Name'] = ' '
    if 'accessLevel' in row:
        table_row['License'] = row['accessLevel']['licenseDisplayName']
        table_row['Status'] = row['accessLevel']['status']
    else:
        table_row['License'] = ' '
        table_row['Status'] = ' '
    return table_row
