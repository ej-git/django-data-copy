from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Post


class Index(generic.ListView):
    model = Post


class Create(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:index')


class Update(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:index')


class Delete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('app:index')


class Copy(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:index')

    def form_valid(self, form):
        post = form.save(commit=False)
        latest_pk = Post.objects.latest('pk').pk + 1
        post.pk = latest_pk
        post.save()
        return redirect(self.success_url)
