from django.http import JsonResponse


def staff(request):
    print('hi')
    return JsonResponse({'directive': 'staff'})