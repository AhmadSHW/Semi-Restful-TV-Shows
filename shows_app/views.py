from django.shortcuts import render, redirect
from .models import Show

# ================ROOT =============

def index(request):
	return redirect('/shows/')

#============== READ ALL =============
# GET /shows/

def all_shows(request):
	all_shows = Show.objects.all()
	return render(request, 'shows/index.html', {'shows': all_shows})

#=============== NEW FORM ===================================
#get/shows/new/

def new_show(request):
	return render(request, 'shows/new.html')

#================== CREATE ==================

# POST/shows/create/

def create_show(request):
	if request.method == 'POST':
		Show.objects.create(
			title=request.POST['title'],
			network=request.POST['network'],
			release_date=request.POST['release_date'],
			description=request.POST['description'],
		)

		new_show = Show.objects.last()
		return redirect(f'/shows/{new_show.id}/')
	return redirect('/shows/new/')
	
#===================== READ ONE ===================================
# GET/shows/<id>/


def show_detail(request, show_id):
	show = Show.objects.get(id=show_id)
	return render(request, 'shows/show.html', {'show': show})

#============================== EDIT FORM ============================
# GET /shows/<id>/edit/

def edit_show(request, show_id):
	show = Show.objects.get(id=show_id)
	return render(request, 'shows/edit.html', {'show': show})




#========================= UPDATE ===============
#POST /shows/<id>/update/

def update_show(request, show_id):
	if request.method == 'POST':
		show = Show.objects.get(id=show_id)
		show.title = request.POST['title']
		show.network = request.POST['network']
		show.release_date = request.POST['release_date']
		show.description = request.POST['description']
		show.save()
		
		return redirect(f'/shows/{show_id}/')
	return redirect('/shows/update')
	

# ===================== DESTROY =================
# POST/show/<id>/destroy/

def destroy_show(request, show_id):
	show = Show.objects.get(id=show_id)
	show.delete()
	return redirect('/shows/')