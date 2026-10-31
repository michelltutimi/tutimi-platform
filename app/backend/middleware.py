import os

class SubdomainRoutingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the request host, ignoring the port if present
        host = request.get_host().split(':')[0]
        
        # Read the subdomain from .env (or use a default locally)
        demo_domain = os.getenv('DEMO_SUBDOMAIN')

        if host == demo_domain:
            # If the host matches the demo, switch the URL configuration dynamically
            request.urlconf = 'demojango.urls'
        
        return self.get_response(request)