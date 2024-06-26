from django.shortcuts import render , get_object_or_404, redirect, HttpResponse
from django.http import JsonResponse

from .models import Agent
from .forms import AgentForm
from .decorators import allowed_suers

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control, never_cache

from django.views.decorators.http import require_GET

# Create your views here.

@login_required()
@require_GET
def validate(request):
    qr_code = request.GET.get('q', '')
    try:
        agent = Agent.objects.filter(id_carnet__icontains=qr_code).last()
        if agent:
            # Assuming your Agent model has fields like name, email, and phone
            agent_data = {
                'status': 'found',
                'first_name': agent.first_name,
                'last_name': agent.last_name,
                'rank': agent.rank,
                'employee_status':agent.employee_status,
                # Add more fields as needed
            }
            return JsonResponse(agent_data)
        else:
            return JsonResponse({'status': 'not_found'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

@login_required(login_url='welcome')
def scan_qr(request):  

    return render(request,'carnetgenerator/read_qr.html',)


@login_required(login_url='welcome')
@allowed_suers(allowed_roles=['Admin'])
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def home(request):

    agents = Agent.objects.all().order_by('-created')
    context = {'agents':agents}
    return render(request,'carnetgenerator/home.html',context)

@login_required()
@allowed_suers(allowed_roles=['Admin'])
def agent_add(request):
    if request.user.has_perm('agent.add_agent'):

        if request.method == "POST":
            agent_form = AgentForm(request.POST, request.FILES)
            if agent_form.is_valid():
                agent = agent_form.save(commit=False)
                agent.added_by = request.user
                agent.save()
                messages.success(request, 'Agent saved successfully!')
                return redirect('home')
        else:
            # If it's a GET request, create a new form instance
            agent_form = AgentForm()

    return render(request, 'carnetgenerator/add_carnet.html', {'agent_form': agent_form})


#________________HTMX__________________
def check_id(request):
    identification = request.POST.get('identification')
    if Agent.objects.filter(identification=identification).exists():
        return HttpResponse("<div class='text-danger bolder'>Ya registrado.</div>")
    else:
        return HttpResponse("<div class='text-success bolder'>Disponible.</div>")
    
    
    
@login_required()
@allowed_suers(allowed_roles=['Admin'])
def agent_update(request, agent_id):
    agent = get_object_or_404(Agent, id=agent_id)
    
    if request.user.has_perm('agent.add_agent'):
        if request.method == "POST":
            agent_form = AgentForm(request.POST, request.FILES, instance=agent)
            if agent_form.is_valid():
                agent = agent_form.save(commit=False)
                agent.added_by = request.user
                agent.save()
                messages.success(request, 'Actualizado!')
                return redirect('home')
            else:
                print("Errores de validación en POST:", agent_form.errors)
        else:
            agent_form = AgentForm(instance=agent)
    else:
        messages.error(request, 'No tiene permiso para actualizar este agente.')
        return redirect('home')

    context = {'agent_form': agent_form}
    return render(request, 'carnetgenerator/add_carnet.html', context)





@login_required()
@allowed_suers(allowed_roles=['Admin'])
def agent_detail(request,agent_id):
    agent = Agent.objects.get(id=agent_id)
    context = {'agent':agent}
    return render(request,'carnetgenerator/detail.html',context)


