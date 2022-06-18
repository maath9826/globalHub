from globalHub.models import Contact_us


def add_variable_to_context(request):
    return {
                "contact_info": Contact_us.objects.last(),
    }