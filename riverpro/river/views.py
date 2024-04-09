
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import River

class Add_river(CreateView):
    model = River
    fields = "__all__"


class List_river(ListView):
    model = River

class Detail_river(DetailView):
    model = River


class Update_river(UpdateView):
    model = River

    fields = "__all__"
    success_url = "/"

class Delete_river(DeleteView):
    model = River
    success_url = "/"
    template_name = "River/River_confirm.html"
