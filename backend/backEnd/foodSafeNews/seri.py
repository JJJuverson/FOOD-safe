from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from foodSafeNews.models import foodSafe_news



class foodSafe_news_serializer(serializers.ModelSerializer):
    class Meta:
        model = foodSafe_news
        fields = '__all__'

@api_view(['GET'])
def News_data(request):
    search_wd = request.GET.get('keywords','')
    if search_wd != '':
        news = foodSafe_news.objects.filter(content__icontains = search_wd)
    else:
        news = foodSafe_news.objects.all()
    nd = foodSafe_news_serializer(news,many = True)	
    return Response(nd.data)