# distribution/views.py
from django.shortcuts import render, redirect
from .forms import TransferForm
from .models import Transfer

def transfer_form(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            transfer = form.save()
            return redirect('label_print', pk=transfer.pk)
    else:
        form = TransferForm()
    return render(request, 'distribution/transfer_form.html', {'form': form})

def label_print(request, pk):
    transfer = Transfer.objects.get(pk=pk)
    context = {
        'transfer': transfer,
        'labels': range(transfer.volume)
    }
    return render(request, 'distribution/label_print.html', context)
