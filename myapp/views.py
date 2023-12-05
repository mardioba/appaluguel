from django.shortcuts import render, redirect
from .models import Immobile, ImmobileImage
from .forms import ClientForm, ImmobileForm
from django.urls import reverse_lazy


def list_location(request):
    immobiles = Immobile.objects.filter(is_locate=False)
    context = {"immobiles": immobiles}
    return render(request, template_name="list-location.html", context=context)


def form_client(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_location")
    return render(request, "form-client.html", {"form": form})


def form_immobile(request):
    form = ImmobileForm()
    if request.method == "POST":
        form = ImmobileForm(request.POST, request.FILES)
        if form.is_valid():
            immobile = form.save()
            files = request.FILES.getlist("immobile")  ## pega todas as imagens
            if files:
                for f in files:
                    ImmobileImage.objects.create(  # cria instance para imagens
                        immobile=immobile, image=f
                    )
            return redirect("list_location")
    return render(request, template_name="form-immobile.html", context={"form": form})
