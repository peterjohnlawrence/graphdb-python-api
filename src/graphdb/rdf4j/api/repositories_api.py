# coding: utf-8

"""
    RDF4J API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from graphdb.rdf4j.api_client import ApiClient


class RepositoriesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_repository(self, repository_id, **kwargs):  # noqa: E501
        """Repository removal  # noqa: E501

        Delete a specific repository by ID. Care should be taken with the use of this method: the result of this operation is the complete removal of the repository from the server, including its configuration settings and (if present) data directory  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repository(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_repository_with_http_info(repository_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_repository_with_http_info(repository_id, **kwargs)  # noqa: E501
            return data

    def delete_repository_with_http_info(self, repository_id, **kwargs):  # noqa: E501
        """Repository removal  # noqa: E501

        Delete a specific repository by ID. Care should be taken with the use of this method: the result of this operation is the complete removal of the repository from the server, including its configuration settings and (if present) data directory  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repository_with_http_info(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and ('repository_id' not in params or
                                                       params['repository_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repository_id` when calling `delete_repository`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryID'] = params['repository_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories/{repositoryID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_statements(self, repository_id, **kwargs):  # noqa: E501
        """Deletes statements from the repository.  # noqa: E501

        Deletes statements from the repository matching the filtering parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_statements(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str subj: Restricts the operation to statements with the specified N-Triples encoded resource as subject.
        :param str pred: Restricts the operation to statements with the specified N-Triples encoded URI as predicate.
        :param str obj: Restricts the operation to statements with the specified N-Triples encoded value as object.
        :param str context: If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_statements_with_http_info(repository_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_statements_with_http_info(repository_id, **kwargs)  # noqa: E501
            return data

    def delete_statements_with_http_info(self, repository_id, **kwargs):  # noqa: E501
        """Deletes statements from the repository.  # noqa: E501

        Deletes statements from the repository matching the filtering parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_statements_with_http_info(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str subj: Restricts the operation to statements with the specified N-Triples encoded resource as subject.
        :param str pred: Restricts the operation to statements with the specified N-Triples encoded URI as predicate.
        :param str obj: Restricts the operation to statements with the specified N-Triples encoded value as object.
        :param str context: If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository_id', 'subj', 'pred', 'obj', 'context']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_statements" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and ('repository_id' not in params or
                                                       params['repository_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repository_id` when calling `delete_statements`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryID'] = params['repository_id']  # noqa: E501

        query_params = []
        if 'subj' in params:
            query_params.append(('subj', params['subj']))  # noqa: E501
        if 'pred' in params:
            query_params.append(('pred', params['pred']))  # noqa: E501
        if 'obj' in params:
            query_params.append(('obj', params['obj']))  # noqa: E501
        if 'context' in params:
            query_params.append(('context', params['context']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories/{repositoryID}/statements', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_repositories(self, **kwargs):  # noqa: E501
        """An overview of the repositories that are available on a server.  # noqa: E501

        Get an list of available repositories, including ID, title, read- and write access parameters for each listed repository. The list is formatted as a tuple query result with variables 'uri', 'id', 'title', 'readable' and 'writable'. The 'uri' value gives the URI/URL for the repository and the 'readable' and 'writable' values are xsd:boolean typed literals indicating read- and write permissions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_repositories(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_repositories_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_repositories_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_repositories_with_http_info(self, **kwargs):  # noqa: E501
        """An overview of the repositories that are available on a server.  # noqa: E501

        Get an list of available repositories, including ID, title, read- and write access parameters for each listed repository. The list is formatted as a tuple query result with variables 'uri', 'id', 'title', 'readable' and 'writable'. The 'uri' value gives the URI/URL for the repository and the 'readable' and 'writable' values are xsd:boolean typed literals indicating read- and write permissions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_repositories_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_repositories" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object', #'int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_statements(self, repository_id, **kwargs):  # noqa: E501
        """Fetches statements from the repository.  # noqa: E501

        Get statements from the repository matching the filtering parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_statements(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str subj: Restricts the operation to statements with the specified N-Triples encoded resource as subject.
        :param str pred: Restricts the operation to statements with the specified N-Triples encoded URI as predicate.
        :param str obj: Restricts the operation to statements with the specified N-Triples encoded value as object.
        :param str context: If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified.
        :param str infer: Specifies whether inferred statements should be included in the result of GET requests. Inferred statements are included by default. Specifying any value other than 'true' (ignoring case) restricts the request to explicit statements only.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_statements_with_http_info(repository_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_statements_with_http_info(repository_id, **kwargs)  # noqa: E501
            return data

    def get_all_statements_with_http_info(self, repository_id, **kwargs):  # noqa: E501
        """Fetches statements from the repository.  # noqa: E501

        Get statements from the repository matching the filtering parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_statements_with_http_info(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str subj: Restricts the operation to statements with the specified N-Triples encoded resource as subject.
        :param str pred: Restricts the operation to statements with the specified N-Triples encoded URI as predicate.
        :param str obj: Restricts the operation to statements with the specified N-Triples encoded value as object.
        :param str context: If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified.
        :param str infer: Specifies whether inferred statements should be included in the result of GET requests. Inferred statements are included by default. Specifying any value other than 'true' (ignoring case) restricts the request to explicit statements only.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository_id', 'subj', 'pred', 'obj', 'context', 'infer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_statements" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and ('repository_id' not in params or
                                                       params['repository_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repository_id` when calling `get_all_statements`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryID'] = params['repository_id']  # noqa: E501

        query_params = []
        if 'subj' in params:
            query_params.append(('subj', params['subj']))  # noqa: E501
        if 'pred' in params:
            query_params.append(('pred', params['pred']))  # noqa: E501
        if 'obj' in params:
            query_params.append(('obj', params['obj']))  # noqa: E501
        if 'context' in params:
            query_params.append(('context', params['context']))  # noqa: E501
        if 'infer' in params:
            query_params.append(('infer', params['infer']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/rdf+xml', 'text/plain', 'text/turtle', 'text/rdf+n3', 'text/x-nquads', 'application/rdf+json', 'application/trix', 'application/x-trig', 'application/x-binary-rdf'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories/{repositoryID}/statements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object', #'int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_repository_size(self, repository_id, **kwargs):  # noqa: E501
        """The repository size (defined as the number of statements it contains)  # noqa: E501

        The endpoint will give you the number of statements in the repository or in the given context  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repository_size(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str context: If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_repository_size_with_http_info(repository_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_repository_size_with_http_info(repository_id, **kwargs)  # noqa: E501
            return data

    def get_repository_size_with_http_info(self, repository_id, **kwargs):  # noqa: E501
        """The repository size (defined as the number of statements it contains)  # noqa: E501

        The endpoint will give you the number of statements in the repository or in the given context  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repository_size_with_http_info(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str context: If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository_id', 'context']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_repository_size" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and ('repository_id' not in params or
                                                       params['repository_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repository_id` when calling `get_repository_size`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryID'] = params['repository_id']  # noqa: E501

        query_params = []
        if 'context' in params:
            query_params.append(('context', params['context']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories/{repositoryID}/size', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_statements(self, repository_id, **kwargs):  # noqa: E501
        """Updates data in the repository, replacing any existing data with the supplied data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_statements(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str context: If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified.
        :param str base_uri: Specifies the base URI to resolve any relative URIs found in uploaded data against
        :param str rdf_data: The supplied data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_statements_with_http_info(repository_id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_statements_with_http_info(repository_id, **kwargs)  # noqa: E501
            return data

    def put_statements_with_http_info(self, repository_id, **kwargs):  # noqa: E501
        """Updates data in the repository, replacing any existing data with the supplied data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_statements_with_http_info(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str context: If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified.
        :param str base_uri: Specifies the base URI to resolve any relative URIs found in uploaded data against
        :param str rdf_data: The supplied data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository_id', 'context', 'base_uri', 'rdf_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_statements" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and ('repository_id' not in params or
                                                       params['repository_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repository_id` when calling `put_statements`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryID'] = params['repository_id']  # noqa: E501

        query_params = []
        if 'context' in params:
            query_params.append(('context', params['context']))  # noqa: E501
        if 'base_uri' in params:
            query_params.append(('baseURI', params['base_uri']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rdf_data' in params:
            body_params = params['rdf_data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/rdf+xml', 'text/plain', 'text/turtle', 'text/rdf+n3', 'text/x-nquads', 'application/rdf+json', 'application/trix', 'application/x-trig', 'application/x-binary-rdf'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories/{repositoryID}/statements', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
