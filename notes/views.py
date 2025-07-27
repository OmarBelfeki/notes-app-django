from django.shortcuts import render, redirect, get_object_or_404
from .models import Note


def home(request):
    notes = Note.objects.all().order_by("-create_at")
    return render(request, "notes/home.html", {"notes": notes})


def add_note(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Note.objects.create(title=title, content=content)
        return redirect("home")
    return render(request, "notes/add_note.html")


def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect("home")
