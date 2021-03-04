from django.http import HttpResponse


class StripeWH_Handler:
    """ Handeling Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handeling generic/unknown webhook event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)
