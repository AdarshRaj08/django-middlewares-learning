# When using multiple middleware components, each one performs specific tasks during the request-response cycle.

# ################################ How It Works: #####################################
# Request Phase:
# Requests pass through middleware in the order listed in MIDDLEWARE setting.
# Each middleware can modify the request or return a response directly.

# View Execution:
# After passing through middleware, the request reaches the view for processing.

# Response Phase:
# The response passes back through the middleware in reverse order.
# Each middleware can modify the response before sending it to the client.

from django.shortcuts import HttpResponse

class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time Brother initialization")

    def __call__(self,request):                 
        print("This is Brother before view")
        response = self.get_response(request)
        print("this is Brother after view")
        return response


class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time Father initialization")

    def __call__(self,request):                 
        print("This is Father before view")
        # response = self.get_response(request)
        response = HttpResponse("Nikal lo")
        print("this is Father after view")
        return response
    


class MummyMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time Mummy initialization")

    def __call__(self,request):                 
        print("This is Mummy before view")
        response = self.get_response(request)
        print("this is Mummy after view")
        return response