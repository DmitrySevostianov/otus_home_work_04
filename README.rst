# otus_home_work_04


# simple_framework это простой uWSGI-совместимый фреймворк, позволяющий ...


# Пример использования:

.. code-block:: python

    from simple_framework import application, define_response_decorator
    
    @define_response_decorator('/hello/')
       def route_to():
          path_to_html_file = 'hello.html'
          return path_to_html_file
