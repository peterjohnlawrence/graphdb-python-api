from __future__ import print_function
import sys
import six
sys.path.append('/Users/peter/git/graphdb-python-api/graphdb-python-api/src')
import graphdb
import time
from pprint import pprint
from graphdb  import rdf4j
configuration = rdf4j.Configuration()
configuration.host = "http://localhost:8080/rdf4j-server"
api_instance = rdf4j.ContextsApi(rdf4j.ApiClient(configuration))
repository_id = 'northwind' # str | The repository ID

'''
try:
    # Gets a list of resources that are used as context identifiers.
    api_response = api_instance.get_repository_contexts(repository_id) 
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->get_repository_contexts: %s\n" % e)
'''
'''
api_instance = rdf4j.RepositoriesApi(rdf4j.ApiClient(configuration))
try:
    # Gets a list of resources that are used as context identifiers.
    api_response = api_instance.get_all_repositories()
    pprint(api_response)
except rdf4j.rest.ApiException as e:
    print("Exception : %s\n" % e)
'''
api_instance = rdf4j.RepositoriesApi(rdf4j.ApiClient(configuration))
try:
    # Gets a list of resources that are used as context identifiers.
    api_response = api_instance.get_repository_size(repository_id)
    pprint(api_response)
except rdf4j.rest.ApiException as e:
    print("Exception : %s\n" % e)
'''
api_instance = rdf4j.RepositoriesApi(rdf4j.ApiClient(configuration))
try:
    # Gets a list of resources that are used as context identifiers.
    api_response = api_instance.get_all_statements(repository_id, subj='<http://northwind.com/Order-10664>')
    pprint(api_response)
except rdf4j.rest.ApiException as e:
    print("Exception : %s\n" % e)
'''
'''
api_instance = rdf4j.SparqlApi(rdf4j.ApiClient(configuration))
try:
    # Gets a list of resources that are used as context identifiers.
    #api_response = api_instance.execute_get_select_query(repository_id, query='describe <http://northwind.com/Order-10664>')
    api_response = api_instance.execute_get_select_query(repository_id, query='SELECT * WHERE {?S ?P ?O } LIMIT 10')
    pprint(api_response)
except rdf4j.rest.ApiException as e:
    print("Exception : %s\n" % e)
'''
'''
api_instance = rdf4j.NamespacesApi(rdf4j.ApiClient(configuration))
try:
    # Gets a list of resources that are used as context identifiers.
    api_response = api_instance.get_namespace_for_prefix(repository_id, namespaces_prefix='northwind')
    pprint(api_response)
except rdf4j.rest.ApiException as e:
    print("Exception : %s\n" % e)
'''
'''
api_instance = rdf4j.NamespacesApi(rdf4j.ApiClient(configuration))
try:
    # Gets a list of resources that are used as context identifiers.
    api_response = api_instance.get_namespaces(repository_id)
    pprint(api_response)
except rdf4j.rest.ApiException as e:
    print("Exception : %s\n" % e)
'''
'''
api_instance = rdf4j.ProtocolApi(rdf4j.ApiClient(configuration))
try:
    # Gets a list of resources that are used as context identifiers.
    api_response = api_instance.get_protocol_version()
    pprint(api_response)
except rdf4j.rest.ApiException as e:
    print("Exception : %s\n" % e)
'''