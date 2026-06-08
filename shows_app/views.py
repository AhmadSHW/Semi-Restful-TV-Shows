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
		errors = {}

		title=request.POST['title']
		network=request.POST['network']
		release_date=request.POST['release_date']
		description=request.POST['description']

		#===========Validation=============
		if len(title) < 2:
			errors['title'] = 'Title must be at Least 2 characters'
		if len(network) < 1:
			errors['network'] = 'network is required'

		if len(release_date) < 1:
			errors['release_date'] = 'Release date is required'

		if len(description) < 10:
			errors['description'] = 'Description must be at least 10 characters'

		if errors:
			return render(request, 'shows/new.html', {
				'errors': errors,
				'data': request.POST
			})

		Show.objects.create (
			title=title,
			network=network,
			release_date=release_date,
			description=description,

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
		errors = {}

		title = request.POST['title']
		network = request.POST['network']
		release_date = request.POST['release_date']
		description = request.POST['description']

		if len(title) < 2:
			errors['title'] = 'Title must be at least 2 characters'

		if len(network) < 1:
			errors['network'] = 'network is required'

		if len(release_date) < 1:
			errors['release_date'] = 'Description must be at lease 10 characters'

		if errors:
			show = Show.objects.get(id=show_id)
			return render(request, 'shows/edit.html', {
				'errors': errors,
				'show': show,
				'data': request.POST
			})
		
		show = Show.objects.get(id=show_id)
		show.title = title
		show.network = network
		show.release_date = release_date
		show.description = description
		show.save()

		return redirect(f'/shows/{show_id}/')
	return redirect(f'/shows/{show_id}/edit/')
	

# ===================== DESTROY =================
# POST/show/<id>/destroy/

def destroy_show(request, show_id):
	show = Show.objects.get(id=show_id)
	show.delete()
	return redirect('/shows/')