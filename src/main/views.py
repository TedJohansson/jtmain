from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, Http404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, UpdateView
from .forms import PostForm, LoginForm
from .models import Post, User

def login_to_app(request):
    """
    Login is required to access the main pages.

    The login screen passes data through to here where we can validate and then redirect.

    Currently we redirect to the 'Create Session' page.

    :param request: HTTP request object
    :return: redirect to the load_file window.
    """

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.login()

            if user:
                login(request, user)

                if request.POST.get('next'):
                    return redirect(request.POST.get('next', 'main:user_home'))
                else:
                    return redirect('main:user_home', )
    else:
        form = LoginForm()
    # If we have reached here, the user has not registered as logged in.
    return render(request, 'login.html', {'form': form})


def logout_of_app(request):
    """
    Basic view to logout a user. Redirects to the login screen.

    :param request: HTTP Request containing the user.
    :return: redirect to login page.
    """
    logout(request)
    return redirect('main:login')


class UserHomeView(ListView):
    """
    The home page for a user.
    """

    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'

    def get_queryset(self):

        return Post.objects.all()


class AddPostView(LoginRequiredMixin, View):
    FORM_CLASS = PostForm
    MODEL = Post

    def get(self, request):

        form = self.FORM_CLASS(request.user)

        return render(request, 'add_post.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Handle the post data from an input file form.

        :param request: HTTP request holding the user.
        :return: redirect: a page showing the new file.
        """
        form = self.FORM_CLASS(request.user, request.POST)

        if form.is_valid():
            new_post = self.MODEL(**form.cleaned_data)
            new_post.save()

            return redirect('main:user_home', )

        return render(request, 'add_post.html', {'form': form})

class UserUpdate(LoginRequiredMixin, UpdateView):
    """
    Manage feed updates.
    """
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'user_update_form.html'

    def get(self, *args, **kwargs):
        """
        Ensure that the person accessing this feed is allowed access.

        :return: Http response, 404 or successful feed update form.
        """
        user = User.objects.get(pk=kwargs['pk'])

        if self.request.user.pk == user.pk:
            return super(UserUpdate, self).get(*args, **kwargs)
        else:
            return Http404('Sorry you cannot access this user.')

    def get_success_url(self):
        """
        On success return the update page for this user.

        :return: HTTP, response for update page.
        """
        return reverse('main:update_user', kwargs={'pk': self.object.id})