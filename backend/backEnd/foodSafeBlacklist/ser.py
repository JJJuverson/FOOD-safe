from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from foodSafeBlacklist.models import foodSafe_blacklist

#分页设置类继承
class pagenationsetting(PageNumberPagination):
    page_size = 2
    page_query_param = 'pageIndex'
    page_size_query_param = 'pageSize'
    max_page_size = 3

class foodSafe_blacklist_serializer(serializers.ModelSerializer):
    class Meta:
        model = foodSafe_blacklist
        fields = '__all__'

@api_view(['GET'])
def Blacklist_data(request):
    search_wd = request.GET.get('keywords','')
    if search_wd != '':
        blacklist = foodSafe_blacklist.objects.filter(enterprise_name__icontains = search_wd)
    else:
        blacklist = foodSafe_blacklist.objects.all()
    #分页
    pnp = pagenationsetting()
    food_Safe_blacklist = pnp.paginate_queryset(blacklist,request)
    bd = foodSafe_blacklist_serializer(food_Safe_blacklist,many = True)	
    return Response(bd.data)