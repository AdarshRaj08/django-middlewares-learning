from django.shortcuts import HttpResponse



class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response
    
    def process_view(request, *args, **kwargs):
        print("This is process view - Before view")
        # return HttpResponse("This is before view")
        return None
    


class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response
    

    # this middleware is active when the exception occurred
    def process_exception(self,request,exception):
        msg = exception
        return HttpResponse(msg)
        # return None



class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response
    

    def process_template_response(self,request,response):
        print("Process Template Response From Middleware")
        response.context_data['name'] = 'Sonam'
        return response
