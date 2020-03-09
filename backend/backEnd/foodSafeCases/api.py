from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from foodSafeCases.models import foodSafe_cases

#分页设置类继承
class pagenationsetting(PageNumberPagination):
    page_size = 2
    page_query_param = 'pageIndex'
    page_size_query_param = 'pageSize'
    max_page_size = 3

class foodSafe_cases_serializer(serializers.ModelSerializer):
    class Meta:
        model = foodSafe_cases
        fields = '__all__'

@api_view(['GET'])
def Cases_data(request):
    search_wd = request.GET.get('keywords','')
    if search_wd != '':
        cases = foodSafe_cases.objects.filter(case_name__icontains = search_wd)
    else:
        cases = foodSafe_cases.objects.all()
    #分页
    pnp = pagenationsetting()
    food_Safe_case = pnp.paginate_queryset(cases,request)
    fd = foodSafe_cases_serializer(food_Safe_case,many = True)	
    return Response(fd.data)