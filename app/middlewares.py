# Middleware in Django is a framework of hooks into Django’s request/response processing.
#  It’s a way to process requests globally before they reach the view or after the view 
#   has processed them. Middleware is a lightweight, low-level plugin system for globally altering Django’s input or output.

# TYPES OF MIDDLEWARE
#   1. BUILT-IN
#   2. CUSTOM


# How Middleware Works
# 1. Request Phase: When a request comes in, Django passes it through each middleware 
#       component in the order they are defined. Each middleware can:
#       => Modify the request object.
#       => Return an HTTP response directly, stopping the processing and bypassing the view.

# 2. View Phase: If no middleware returns a response, Django calls the appropriate view
#           , passing it the request object.

# 3. Response Phase: After the view has processed the request and returned a response, 
#          the response is passed back through each middleware component in reverse order. Each middleware can:
#       => Modify the response object.
#       => Replace the response entirely.


# TWO way to create custom middleware 
# 1. Function based
# 2. class based

# ################### STEPS FOLLWOED IN CREATING MIDDLEWARE ################################

# 1.creates middlewares.py file (not strict that name should be middleware.py you can name any)
# 2.then write middleware
# 3.go in settings.py and then add that middleware into that 
#   ('appname.middleware(filename in which middleware present).middlewarename')


# ##################v function middleware ###################

# def my_middleware(get_response):
#     only one time will run when the server start
#     print("One time initialization")

#     def my_function(request):                             # this will run every time we hit request
#         print("this is before view")
#         response = get_response(request)
#         print("this is after view")
#         return response
#     return my_function


# #################### class Middleware ##########################

class MyMiddleware:
    # only one time will run when the server start
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time initialization")

    def __call__(self,request):                 # this will run every time we hit request
        print("This is before view")
        response = self.get_response(request)
        print("this is after view")
        return response