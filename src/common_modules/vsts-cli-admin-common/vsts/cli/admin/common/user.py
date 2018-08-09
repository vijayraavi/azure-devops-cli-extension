# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

from vsts.member_entitlement_management.v4_1.models.access_level import AccessLevel
from vsts.member_entitlement_management.v4_1.models.graph_user import GraphUser
from vsts.member_entitlement_management.v4_1.models.user_entitlement import UserEntitlement
from vsts.cli.common.services import (get_member_entitlement_management_client,
                                      resolve_instance)
from vsts.cli.common.identities import resolve_identity_as_id


def user_entitlement_list(team_instance=None, top=None, skip=None, detect=None):
    """List User Entitlements.
    List the user entitlements for an organization.
    :param int top: Maximum number of the users to return. Max value is 10000. Default value is 100
    :param int skip: Offset: Number of records to skip.
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: [UserEntitlement]
    """
    team_instance = resolve_instance(detect=detect, team_instance=team_instance)
    client = get_member_entitlement_management_client(team_instance)
    member_entitlements = client.get_user_entitlements(top=top, skip=skip)
    return member_entitlements


def user_entitlement_show(user, team_instance=None, detect=None):
    """Show User Entitlement.
    Show a user's entitlements.
    :param str user: The user to show entitlements for.
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: UserEntitlement
    """
    team_instance = resolve_instance(detect=detect, team_instance=team_instance)
    user_id = resolve_identity_as_id(user, team_instance)
    client = get_member_entitlement_management_client(team_instance)
    member_entitlements = client.get_user_entitlement(user_id=user_id)
    return member_entitlements


def add_user(user, access_level, team_instance=None, detect=None):
    """Add a user to an organization.
    Add a user to an organization.
    :param str user: The user's ID.
    :param str access_level: The user's access level denoted by a license.
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: OperationResult
    """
    team_instance = resolve_instance(detect=detect, team_instance=team_instance)
    identity_id = resolve_identity_as_id(user, team_instance)
    client = get_member_entitlement_management_client(team_instance)
    user_entitlement = UserEntitlement()
    user_entitlement.id = identity_id
    user_entitlement.access_level = AccessLevel()
    user_entitlement.access_level.account_license_type = access_level
    user_entitlement.user = GraphUser()
    user_entitlement.user.subject_kind = 'user'
    response = client.add_user_entitlement(user_entitlement=user_entitlement)
    if not response.is_success:
        if response.operation_result is not None and response.operation_result.errors:
            message = ' '.join([error['value'] for error in response.operation_result.errors])
        else:
            message = 'Failed to add user.'
        raise CLIError(message)
    return response.user_entitlement


def remove_user(user, team_instance=None, detect=None):
    """Remove a user from an organization.
    :param str user: The user to remove.
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: OperationResult
    """
    team_instance = resolve_instance(detect=detect, team_instance=team_instance)
    identity_id = resolve_identity_as_id(user, team_instance)
    client = get_member_entitlement_management_client(team_instance)
    client.delete_user_entitlement(user_id=identity_id)
