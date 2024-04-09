from django.contrib.auth.middleware import AuthenticationMiddleware
from django.http import JsonResponse
from decouple import config


class APIAuthenticationMiddleware(AuthenticationMiddleware):
    """
    Custom Middleware for authenticating requests based on the API Key
    """

    def process_request(self, request):
        # Check if API key is present in the request headers
        api_key = request.GET.get('api_key')

        valid_api_key = config('OPENWEATHER_API_KEY')

        # Validate the API key
        if api_key != valid_api_key:
            return JsonResponse({'error': 'Unauthorized'}, status=401)