from simple_framework import application, view_on_route_adress, define_response_decorator



@define_response_decorator('/hello/')
def route_to():
    path_to_file = 'hello.html'
    print(path_to_file)
    return path_to_file

@define_response_decorator('/contact/')
def route_to():
    path_to_file = 'contact.html'
    print(path_to_file)
    return path_to_file



view_on_route_adress('/admin/', 'admin.html')

