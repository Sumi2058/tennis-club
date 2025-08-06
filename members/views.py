from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Member,MemberForm
from django.shortcuts import render, get_object_or_404, redirect


def members(request):
  template = loader.get_template('myfirst.html')
  save(request)
  findall(request)
  return HttpResponse(template.render())

def save(request):
  member=Member(firstname='Sumi',lastname='Baniya')
  member.save()

def findall(request):
  members=Member.objects.all().values()
  print(members)

def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})  

def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'member_detail.html', {'member': member})

def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'member_form.html', {'form': form})

def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'member_form.html', {'form': form})

def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'member_confirm_delete.html', {'member': member})
