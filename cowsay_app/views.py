import subprocess

from django.shortcuts import render


from cowsay_app.form import AddMessageForm
from cowsay_app.models import Message

# Create your views here.


def index(request, ):
    html = 'index.html'

    if request.method == 'POST':
        form = AddMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Message.objects.create(message=data['message'])
            user_input = data['message']
            cow_sub = subprocess.run(['cowsay', user_input],
                                     capture_output=True, text=True)

            return render(request, html, {'form': AddMessageForm(),
                          'output': cow_sub.stdout})

    form = AddMessageForm()
    return render(request, html, {'form': form})


def most_recent(request):

    top_ten = Message.objects.filter().order_by("-id")[:10]
    return render(request, 'm_recent.html', {'top_ten': top_ten})
