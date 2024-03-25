from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PermissionLevel, SecurityGroup
from .forms import SecurityGroupForm

@login_required
def manage_security_groups(request):
    """
    View to manage security groups, including creating, editing, and deleting them.
    """
    security_groups = SecurityGroup.objects.all()
    return render(request, 'security/manage_security_groups.html', {'security_groups': security_groups})

@login_required
def create_security_group(request):
    """
    View to create a new security group.
    """
    if request.method == 'POST':
        form = SecurityGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_security_groups')
    else:
        form = SecurityGroupForm()
    return render(request, 'security/create_security_group.html', {'form': form})

@login_required
def edit_security_group(request, group_id):
    """
    View to edit an existing security group.
    """
    security_group = SecurityGroup.objects.get(id=group_id)
    if request.method == 'POST':
        form = SecurityGroupForm(request.POST, instance=security_group)
        if form.is_valid():
            form.save()
            return redirect('manage_security_groups')
    else:
        form = SecurityGroupForm(instance=security_group)
    return render(request, 'security/edit_security_group.html', {'form': form})

@login_required
def delete_security_group(request, group_id):
    """
    View to delete an existing security group.
    """
    security_group = SecurityGroup.objects.get(id=group_id)
    if request.method == 'POST':
        security_group.delete()
        return redirect('manage_security_groups')
    return render(request, 'security/delete_security_group.html', {'security_group': security_group})
