# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType
from ._format import (transform_pull_request_table_output,
                      transform_pull_requests_table_output,
                      transform_repo_table_output,
                      transform_repos_table_output,
                      transform_reviewers_table_output,
                      transform_reviewer_table_output,
                      transform_policies_table_output,
                      transform_policy_table_output,
                      transform_work_items_table_output,
                      transform_repo_import_table_output,
                      transform_repo_policy_table_output,
                      transform_repo_policies_table_output)


reposPullRequestOps = CliCommandType(
    operations_tmpl='azext_devops.dev.repos.pull_request#{}'
)

reposRepositoryOps = CliCommandType(
    operations_tmpl='azext_devops.dev.repos.repository#{}'
)

reposImportOps = CliCommandType(
    operations_tmpl='azext_devops.dev.repos.import_request#{}'
)

policyOps = CliCommandType(
    operations_tmpl='azext_devops.dev.repos.policy#{}'
)


def load_code_commands(self, _):
    with self.command_group('repos', command_type=reposRepositoryOps) as g:
        # repository commands
        g.command('create', 'create_repo', table_transformer=transform_repo_table_output)
        g.command('delete', 'delete_repo', confirmation='Are you sure you want to delete this repository?')
        g.command('list', 'list_repos', table_transformer=transform_repos_table_output)
        g.command('show', 'show_repo', table_transformer=transform_repo_table_output)
        g.command('update', 'update_repo', table_transformer=transform_repo_table_output)

    with self.command_group('repos policy', command_type=policyOps) as g:
        # repository/ branch policies
        g.command('create', 'create_policy', table_transformer=transform_repo_policy_table_output)
        g.command('list', 'list_policy', table_transformer=transform_repo_policies_table_output)
        g.command('show', 'get_policy', table_transformer=transform_repo_policy_table_output)
        g.command('update', 'update_policy', table_transformer=transform_repo_policy_table_output)
        g.command('delete', 'delete_policy', confirmation='Are you sure you want to delete this policy?')

    with self.command_group('repos pr', command_type=reposPullRequestOps) as g:
        # basic pr commands
        g.command('create', 'create_pull_request', table_transformer=transform_pull_request_table_output)
        g.command('update', 'update_pull_request', table_transformer=transform_pull_request_table_output)
        g.command('show', 'show_pull_request', table_transformer=transform_pull_request_table_output)
        g.command('list', 'list_pull_requests', table_transformer=transform_pull_requests_table_output)

        # pr status update commands
        g.command('complete', 'complete_pull_request', table_transformer=transform_pull_request_table_output)
        g.command('abandon', 'abandon_pull_request', table_transformer=transform_pull_request_table_output)
        g.command('reactivate', 'reactivate_pull_request', table_transformer=transform_pull_request_table_output)

        # pr reviewer commands
        g.command('reviewer add', 'create_pull_request_reviewers', table_transformer=transform_reviewers_table_output)
        g.command('reviewer list', 'list_pull_request_reviewers', table_transformer=transform_reviewers_table_output)
        g.command('reviewer remove', 'delete_pull_request_reviewers',
                  table_transformer=transform_reviewers_table_output)

        # pr work item commands
        g.command('work-item add', 'add_pull_request_work_items', table_transformer=transform_work_items_table_output)
        g.command('work-item list', 'list_pull_request_work_items',
                  table_transformer=transform_work_items_table_output)
        g.command('work-item remove', 'remove_pull_request_work_items',
                  table_transformer=transform_work_items_table_output)

        # pr set-vote commands
        g.command('set-vote', 'vote_pull_request', table_transformer=transform_reviewer_table_output)

        # pr policy commands
        g.command('policy list', 'list_pr_policies', table_transformer=transform_policies_table_output)
        g.command('policy queue', 'queue_pr_policy', table_transformer=transform_policy_table_output)

    with self.command_group('repos import', command_type=reposImportOps) as g:
        # import request
        g.command('create', 'create_import_request', table_transformer=transform_repo_import_table_output)
