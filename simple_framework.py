from html import escape

_page_adress_template_dict = {
                           '/': "index.html" ,
                           '/about/': "about.html" ,
                          }


def load_html_file(file_name):

    result = ""
    try:
        file = open(file_name, 'rb')
        result = file.read()
        file.close()
    except OSError:
        print("file does not exist")

    return result


def view_on_route_adress(route_adress, response_page_name):
    _page_adress_template_dict[route_adress] = response_page_name
    print(_page_adress_template_dict)
    


def define_response_decorator(route_adress): ##function_to_decorate
    print('route_adress' , route_adress)
    def decorator(function_to_decorate):
        print('function_to_decorate is: ', function_to_decorate)
        response_page_name = function_to_decorate() 
        print('RASPONSE \n' , response_page_name)
        _page_adress_template_dict[route_adress] = response_page_name    	
        return response_page_name

    return decorator


def get_method_from_environ(environ):
    request_method = environ['REQUEST_METHOD']
    print('REQUEST_METHOD: ',request_method,"\n")

    return request_method



def get_request_uri_from_environ(environ):
    request_URI = environ['REQUEST_URI']
    print('REQUEST_URI: ',request_URI,"\n")

    #route = escape(request_URI)#  ???!

    #print(route)
    return request_URI#route


def define_response(page_route_adress):
    
    try: 
         page_adress = _page_adress_template_dict[page_route_adress]

         response_body = load_html_file(page_adress)
         
         if not response_body:
              response_body = load_html_file('404.html')
              response_status = '404 Not Found'
             
         else:
              response_status = '200 OK'

    except:
         response_body = load_html_file('404.html')
         response_status = '404 Not Found'
    
    response_header = [('Content-Type','text/html')]

    return response_status, response_header, response_body
    
    


def application(environ, start_response):
    #print('===============================\n RAW_environ :\n',environ)
    #print(environ)
    page_route_adress = get_request_uri_from_environ(environ)
    ###################
###############################
    method = get_method_from_environ(environ)
###############################
    #print(page_route_adress)
    
    response_status, response_header, response_body = define_response(page_route_adress) 
    #print(response_status)
    ##response_header = [('Content-Type','text/html')]
    start_response(response_status, response_header)

    return response_body







