# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class AccessLevel(Model):
    """AccessLevel.

    :param account_license_type:
    :type account_license_type: object
    :param assignment_source:
    :type assignment_source: object
    :param license_display_name:
    :type license_display_name: str
    :param licensing_source:
    :type licensing_source: object
    :param msdn_license_type:
    :type msdn_license_type: object
    :param status:
    :type status: object
    :param status_message:
    :type status_message: str
    """

    _attribute_map = {
        'account_license_type': {'key': 'accountLicenseType', 'type': 'object'},
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'license_display_name': {'key': 'licenseDisplayName', 'type': 'str'},
        'licensing_source': {'key': 'licensingSource', 'type': 'object'},
        'msdn_license_type': {'key': 'msdnLicenseType', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'},
        'status_message': {'key': 'statusMessage', 'type': 'str'}
    }

    def __init__(self, account_license_type=None, assignment_source=None, license_display_name=None, licensing_source=None, msdn_license_type=None, status=None, status_message=None):
        super(AccessLevel, self).__init__()
        self.account_license_type = account_license_type
        self.assignment_source = assignment_source
        self.license_display_name = license_display_name
        self.licensing_source = licensing_source
        self.msdn_license_type = msdn_license_type
        self.status = status
        self.status_message = status_message



class BaseOperationResult(Model):
    """BaseOperationResult.

    :param errors: List of error codes paired with their corresponding error messages
    :type errors: list of { key: int; value: str }
    :param is_success: Success status of the operation
    :type is_success: bool
    """

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'}
    }

    def __init__(self, errors=None, is_success=None):
        super(BaseOperationResult, self).__init__()
        self.errors = errors
        self.is_success = is_success



class Extension(Model):
    """Extension.

    :param assignment_source: Assignment source for this extension. I.e. explicitly assigned or from a group rule
    :type assignment_source: object
    :param id: Gallery Id of the Extension
    :type id: str
    :param name: Friendly name of this extension
    :type name: str
    :param source: Source of this extension assignment. Ex: msdn, account, none, ect.
    :type source: object
    """

    _attribute_map = {
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'source': {'key': 'source', 'type': 'object'}
    }

    def __init__(self, assignment_source=None, id=None, name=None, source=None):
        super(Extension, self).__init__()
        self.assignment_source = assignment_source
        self.id = id
        self.name = name
        self.source = source



class GraphSubject(Model):
    """GraphSubject.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <microsoft.-visual-studio.-services.-web-api.v4_0.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, origin=None, origin_id=None, subject_kind=None, url=None):
        super(GraphSubject, self).__init__()
        self._links = _links
        self.descriptor = descriptor
        self.display_name = display_name
        self.origin = origin
        self.origin_id = origin_id
        self.subject_kind = subject_kind
        self.url = url



class Group(Model):
    """Group.

    :param display_name:
    :type display_name: str
    :param group_type:
    :type group_type: object
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'group_type': {'key': 'groupType', 'type': 'object'}
    }

    def __init__(self, display_name=None, group_type=None):
        super(Group, self).__init__()
        self.display_name = display_name
        self.group_type = group_type



class GroupEntitlement(Model):
    """GroupEntitlement.

    :param extension_rules: Extension Rules
    :type extension_rules: list of :class:`Extension <member-entitlement-management.v4_0.models.Extension>`
    :param group: Member reference
    :type group: :class:`GraphGroup <member-entitlement-management.v4_0.models.GraphGroup>`
    :param id: The unique identifier which matches the Id of the GraphMember
    :type id: str
    :param license_rule: License Rule
    :type license_rule: :class:`AccessLevel <member-entitlement-management.v4_0.models.AccessLevel>`
    :param project_entitlements: Relation between a project and the member's effective permissions in that project
    :type project_entitlements: list of :class:`ProjectEntitlement <member-entitlement-management.v4_0.models.ProjectEntitlement>`
    :param status:
    :type status: object
    """

    _attribute_map = {
        'extension_rules': {'key': 'extensionRules', 'type': '[Extension]'},
        'group': {'key': 'group', 'type': 'GraphGroup'},
        'id': {'key': 'id', 'type': 'str'},
        'license_rule': {'key': 'licenseRule', 'type': 'AccessLevel'},
        'project_entitlements': {'key': 'projectEntitlements', 'type': '[ProjectEntitlement]'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, extension_rules=None, group=None, id=None, license_rule=None, project_entitlements=None, status=None):
        super(GroupEntitlement, self).__init__()
        self.extension_rules = extension_rules
        self.group = group
        self.id = id
        self.license_rule = license_rule
        self.project_entitlements = project_entitlements
        self.status = status



class GroupOperationResult(BaseOperationResult):
    """GroupOperationResult.

    :param errors: List of error codes paired with their corresponding error messages
    :type errors: list of { key: int; value: str }
    :param is_success: Success status of the operation
    :type is_success: bool
    :param group_id: Identifier of the Group being acted upon
    :type group_id: str
    :param result: Result of the Groupentitlement after the operation
    :type result: :class:`GroupEntitlement <member-entitlement-management.v4_0.models.GroupEntitlement>`
    """

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'result': {'key': 'result', 'type': 'GroupEntitlement'}
    }

    def __init__(self, errors=None, is_success=None, group_id=None, result=None):
        super(GroupOperationResult, self).__init__(errors=errors, is_success=is_success)
        self.group_id = group_id
        self.result = result



class JsonPatchOperation(Model):
    """JsonPatchOperation.

    :param from_: The path to copy from for the Move/Copy operation.
    :type from_: str
    :param op: The patch operation
    :type op: object
    :param path: The path for the operation
    :type path: str
    :param value: The value for the operation. This is either a primitive or a JToken.
    :type value: object
    """

    _attribute_map = {
        'from_': {'key': 'from', 'type': 'str'},
        'op': {'key': 'op', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, from_=None, op=None, path=None, value=None):
        super(JsonPatchOperation, self).__init__()
        self.from_ = from_
        self.op = op
        self.path = path
        self.value = value



class MemberEntitlement(Model):
    """MemberEntitlement.

    :param access_level: Member's access level denoted by a license
    :type access_level: :class:`AccessLevel <member-entitlement-management.v4_0.models.AccessLevel>`
    :param extensions: Member's extensions
    :type extensions: list of :class:`Extension <member-entitlement-management.v4_0.models.Extension>`
    :param group_assignments: GroupEntitlements that this member belongs to
    :type group_assignments: list of :class:`GroupEntitlement <member-entitlement-management.v4_0.models.GroupEntitlement>`
    :param id: The unique identifier which matches the Id of the GraphMember
    :type id: str
    :param last_accessed_date: Date the Member last access the collection
    :type last_accessed_date: datetime
    :param member: Member reference
    :type member: :class:`GraphMember <member-entitlement-management.v4_0.models.GraphMember>`
    :param project_entitlements: Relation between a project and the member's effective permissions in that project
    :type project_entitlements: list of :class:`ProjectEntitlement <member-entitlement-management.v4_0.models.ProjectEntitlement>`
    """

    _attribute_map = {
        'access_level': {'key': 'accessLevel', 'type': 'AccessLevel'},
        'extensions': {'key': 'extensions', 'type': '[Extension]'},
        'group_assignments': {'key': 'groupAssignments', 'type': '[GroupEntitlement]'},
        'id': {'key': 'id', 'type': 'str'},
        'last_accessed_date': {'key': 'lastAccessedDate', 'type': 'iso-8601'},
        'member': {'key': 'member', 'type': 'GraphMember'},
        'project_entitlements': {'key': 'projectEntitlements', 'type': '[ProjectEntitlement]'}
    }

    def __init__(self, access_level=None, extensions=None, group_assignments=None, id=None, last_accessed_date=None, member=None, project_entitlements=None):
        super(MemberEntitlement, self).__init__()
        self.access_level = access_level
        self.extensions = extensions
        self.group_assignments = group_assignments
        self.id = id
        self.last_accessed_date = last_accessed_date
        self.member = member
        self.project_entitlements = project_entitlements



class MemberEntitlementsResponseBase(Model):
    """MemberEntitlementsResponseBase.

    :param is_success: True if all operations were successful
    :type is_success: bool
    :param member_entitlement: Result of the member entitlement after the operations have been applied
    :type member_entitlement: :class:`MemberEntitlement <member-entitlement-management.v4_0.models.MemberEntitlement>`
    """

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_entitlement': {'key': 'memberEntitlement', 'type': 'MemberEntitlement'}
    }

    def __init__(self, is_success=None, member_entitlement=None):
        super(MemberEntitlementsResponseBase, self).__init__()
        self.is_success = is_success
        self.member_entitlement = member_entitlement



class OperationReference(Model):
    """OperationReference.

    :param id: The identifier for this operation.
    :type id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: Url to get the full object.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, status=None, url=None):
        super(OperationReference, self).__init__()
        self.id = id
        self.status = status
        self.url = url



class OperationResult(Model):
    """OperationResult.

    :param errors: List of error codes paired with their corresponding error messages
    :type errors: list of { key: int; value: str }
    :param is_success: Success status of the operation
    :type is_success: bool
    :param member_id: Identifier of the Member being acted upon
    :type member_id: str
    :param result: Result of the MemberEntitlement after the operation
    :type result: :class:`MemberEntitlement <member-entitlement-management.v4_0.models.MemberEntitlement>`
    """

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_id': {'key': 'memberId', 'type': 'str'},
        'result': {'key': 'result', 'type': 'MemberEntitlement'}
    }

    def __init__(self, errors=None, is_success=None, member_id=None, result=None):
        super(OperationResult, self).__init__()
        self.errors = errors
        self.is_success = is_success
        self.member_id = member_id
        self.result = result



class ProjectEntitlement(Model):
    """ProjectEntitlement.

    :param assignment_source:
    :type assignment_source: object
    :param group:
    :type group: :class:`Group <member-entitlement-management.v4_0.models.Group>`
    :param is_project_permission_inherited:
    :type is_project_permission_inherited: bool
    :param project_ref:
    :type project_ref: :class:`ProjectRef <member-entitlement-management.v4_0.models.ProjectRef>`
    :param team_refs:
    :type team_refs: list of :class:`TeamRef <member-entitlement-management.v4_0.models.TeamRef>`
    """

    _attribute_map = {
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'group': {'key': 'group', 'type': 'Group'},
        'is_project_permission_inherited': {'key': 'isProjectPermissionInherited', 'type': 'bool'},
        'project_ref': {'key': 'projectRef', 'type': 'ProjectRef'},
        'team_refs': {'key': 'teamRefs', 'type': '[TeamRef]'}
    }

    def __init__(self, assignment_source=None, group=None, is_project_permission_inherited=None, project_ref=None, team_refs=None):
        super(ProjectEntitlement, self).__init__()
        self.assignment_source = assignment_source
        self.group = group
        self.is_project_permission_inherited = is_project_permission_inherited
        self.project_ref = project_ref
        self.team_refs = team_refs



class ProjectRef(Model):
    """ProjectRef.

    :param id:
    :type id: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ProjectRef, self).__init__()
        self.id = id
        self.name = name



class ReferenceLinks(Model):
    """ReferenceLinks.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links



class TeamRef(Model):
    """TeamRef.

    :param id:
    :type id: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(TeamRef, self).__init__()
        self.id = id
        self.name = name



class GraphMember(GraphSubject):
    """GraphMember.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <microsoft.-visual-studio.-services.-web-api.v4_0.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param domain: This represents the name of the container of origin for a graph member. (For MSA this is "Windows Live ID", for AD the name of the domain, for AAD the name of the directory, for Vsts groups the ScopeId, etc)
    :type domain: str
    :param mail_address: The email address of record for a given graph member. This may be different than the principal name.
    :type mail_address: str
    :param principal_name: This is the PrincipalName of this graph member from the source provider. The source provider may change this field over time and it is not guaranteed to be immutable for the life of the graph member by Vsts.
    :type principal_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, origin=None, origin_id=None, subject_kind=None, url=None, domain=None, mail_address=None, principal_name=None):
        super(GraphMember, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, origin=origin, origin_id=origin_id, subject_kind=subject_kind, url=url)
        self.domain = domain
        self.mail_address = mail_address
        self.principal_name = principal_name



class GroupEntitlementOperationReference(OperationReference):
    """GroupEntitlementOperationReference.

    :param id: The identifier for this operation.
    :type id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: Url to get the full object.
    :type url: str
    :param completed: Operation completed with success or failure
    :type completed: bool
    :param have_results_succeeded: True if all operations were successful
    :type have_results_succeeded: bool
    :param results: List of results for each operation
    :type results: list of :class:`GroupOperationResult <member-entitlement-management.v4_0.models.GroupOperationResult>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'completed': {'key': 'completed', 'type': 'bool'},
        'have_results_succeeded': {'key': 'haveResultsSucceeded', 'type': 'bool'},
        'results': {'key': 'results', 'type': '[GroupOperationResult]'}
    }

    def __init__(self, id=None, status=None, url=None, completed=None, have_results_succeeded=None, results=None):
        super(GroupEntitlementOperationReference, self).__init__(id=id, status=status, url=url)
        self.completed = completed
        self.have_results_succeeded = have_results_succeeded
        self.results = results



class MemberEntitlementsPatchResponse(MemberEntitlementsResponseBase):
    """MemberEntitlementsPatchResponse.

    :param is_success: True if all operations were successful
    :type is_success: bool
    :param member_entitlement: Result of the member entitlement after the operations have been applied
    :type member_entitlement: :class:`MemberEntitlement <member-entitlement-management.v4_0.models.MemberEntitlement>`
    :param operation_results: List of results for each operation
    :type operation_results: list of :class:`OperationResult <member-entitlement-management.v4_0.models.OperationResult>`
    """

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_entitlement': {'key': 'memberEntitlement', 'type': 'MemberEntitlement'},
        'operation_results': {'key': 'operationResults', 'type': '[OperationResult]'}
    }

    def __init__(self, is_success=None, member_entitlement=None, operation_results=None):
        super(MemberEntitlementsPatchResponse, self).__init__(is_success=is_success, member_entitlement=member_entitlement)
        self.operation_results = operation_results



class MemberEntitlementsPostResponse(MemberEntitlementsResponseBase):
    """MemberEntitlementsPostResponse.

    :param is_success: True if all operations were successful
    :type is_success: bool
    :param member_entitlement: Result of the member entitlement after the operations have been applied
    :type member_entitlement: :class:`MemberEntitlement <member-entitlement-management.v4_0.models.MemberEntitlement>`
    :param operation_result: Operation result
    :type operation_result: :class:`OperationResult <member-entitlement-management.v4_0.models.OperationResult>`
    """

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_entitlement': {'key': 'memberEntitlement', 'type': 'MemberEntitlement'},
        'operation_result': {'key': 'operationResult', 'type': 'OperationResult'}
    }

    def __init__(self, is_success=None, member_entitlement=None, operation_result=None):
        super(MemberEntitlementsPostResponse, self).__init__(is_success=is_success, member_entitlement=member_entitlement)
        self.operation_result = operation_result



class MemberEntitlementOperationReference(OperationReference):
    """MemberEntitlementOperationReference.

    :param id: The identifier for this operation.
    :type id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: Url to get the full object.
    :type url: str
    :param completed: Operation completed with success or failure
    :type completed: bool
    :param have_results_succeeded: True if all operations were successful
    :type have_results_succeeded: bool
    :param results: List of results for each operation
    :type results: list of :class:`OperationResult <member-entitlement-management.v4_0.models.OperationResult>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'completed': {'key': 'completed', 'type': 'bool'},
        'have_results_succeeded': {'key': 'haveResultsSucceeded', 'type': 'bool'},
        'results': {'key': 'results', 'type': '[OperationResult]'}
    }

    def __init__(self, id=None, status=None, url=None, completed=None, have_results_succeeded=None, results=None):
        super(MemberEntitlementOperationReference, self).__init__(id=id, status=status, url=url)
        self.completed = completed
        self.have_results_succeeded = have_results_succeeded
        self.results = results



class GraphGroup(GraphMember):
    """GraphGroup.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <microsoft.-visual-studio.-services.-web-api.v4_0.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param domain: This represents the name of the container of origin for a graph member. (For MSA this is "Windows Live ID", for AD the name of the domain, for AAD the name of the directory, for Vsts groups the ScopeId, etc)
    :type domain: str
    :param mail_address: The email address of record for a given graph member. This may be different than the principal name.
    :type mail_address: str
    :param principal_name: This is the PrincipalName of this graph member from the source provider. The source provider may change this field over time and it is not guaranteed to be immutable for the life of the graph member by Vsts.
    :type principal_name: str
    :param description: A short phrase to help human readers disambiguate groups with similar names
    :type description: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, origin=None, origin_id=None, subject_kind=None, url=None, domain=None, mail_address=None, principal_name=None, description=None):
        super(GraphGroup, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, origin=origin, origin_id=origin_id, subject_kind=subject_kind, url=url, domain=domain, mail_address=mail_address, principal_name=principal_name)
        self.description = description
