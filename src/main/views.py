from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class UserHomeView(View):
    """
    The home page for a user.
    """
    def get(self, request, *args, **kwargs):
        """
        Build up the user home page.

        :param request: HTTP request holding the user.
        :return: render: the home page template.
        """
        context = {}

        return render(request, 'home.html', context)
