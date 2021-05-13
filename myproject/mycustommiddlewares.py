from django.http import HttpResponse







class mycustommiddlewareone:
    def __init__(self, get_response):
        self.get_response = get_response
        print("\nHitting middleawre......\n")

    def __call__(self, request):
        # return HttpResponse("I am middleware")
        request.extra_info = "this info comming from middleware"
        return self.get_response(request)
    


    # availabe hooks are:

    # *********** for request *************
        # process_request(self, request)
        # process_view(self, request, view_func, view_args, view_kwargs)

    # *********** for response **********
        # process_template_response(self, request, response) (only for template responses)
        # process_response(self, request, response)
        # process_exception(self, request, exception) (only if the view raised an exception)
    
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("from process view request.extra_info:", request.extra_info)
        print("My custom middleware can change the view response")
    
    def process_request(self, request):
        print("My Custom midlleware is intercepting the reuests...\n")

    def process_response(self, request, response):
        print("My custom middleware can change the response")