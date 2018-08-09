# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.commands import CommandGroup
from ._format import transform_users_table_output, transform_user_table_output, transform_banner_table_output


def load_admin_commands(cli_command_loader):
    with CommandGroup(cli_command_loader, 'admin', 'vsts.cli.admin.common.banner#{}') as g:
        g.command('banner list', 'banner_list', table_transformer=transform_banner_table_output)
        g.command('banner show', 'banner_show', table_transformer=transform_banner_table_output)
        g.command('banner add', 'banner_add', table_transformer=transform_banner_table_output)
        g.command('banner remove', 'banner_remove')
        g.command('banner update', 'banner_update', table_transformer=transform_banner_table_output)
    with CommandGroup(cli_command_loader, 'admin', 'vsts.cli.admin.common.user#{}') as g:
        g.command('user list', 'user_entitlement_list', table_transformer=transform_users_table_output)
        g.command('user show', 'user_entitlement_show', table_transformer=transform_user_table_output)
        g.command('user add', 'add_user', table_transformer=transform_user_table_output)
        g.command('user remove', 'remove_user')
