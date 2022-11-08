from django.shortcuts import render
from .forms import ExchangeForm


def exchange(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            from_curr = float(form.cleaned_data.get('from_curr'))
            to_curr = float(form.cleaned_data.get('to_curr'))
            result = round(
                (to_curr / from_curr) * amount, 2
            )
            context = {
                'form': form,
                'result': result,
            }
    elif request.method == 'GET':
        form = ExchangeForm()
        context = {
            'form': form,
        }
    return render(
            request=request,
            template_name='exchange_app/index.html',
            context=context
        )
