from apps.authentication.views import authprint, AuthToken
from apps.crud.views import crudprints, CrudOperations


authprint.add_url_rule('/token/','authtoken',AuthToken.as_view('authtoken'), methods =['GET','POST'])

crudprints.add_url_rule('/books/','crud_operations',CrudOperations.as_view('crudoperations'),methods=['GET','POST'])

crudprints.add_url_rule('/books/<int:id>','single_crud_oprations',CrudOperations.as_view('crudoperations'),methods=['GET','PATCH','DELETE'])
