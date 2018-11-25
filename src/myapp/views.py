from django.shortcuts import render


# Create your views here.
from .forms import NameForm 
from .models import PageView
# from analytics.models import TotalCount

def form_info(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			if(PageView.objects.count()<=0):
				x=PageView.objects.create()
				x.save()
			else:
				x=PageView.objects.all()[0]
				x.hits=x.hits+1
				x.save()
				context={'page':x.hits}
				return render(request, 'sucess.html', context=context)

	else:
		form = NameForm()

	return render(request, 'home.html', {'form':form})
