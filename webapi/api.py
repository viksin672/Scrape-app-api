from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .scrap import Scrapscript, main2
import asyncio
loop = asyncio.get_event_loop()

class PhoneList(APIView):
	def get(self,request):
		print("before scrap")
		#xio = Scrapscript()
		main2.delay()
		print("after scrap")
		return Response("Scrape Started")
	def post(self, request):
		serializer = PhonesSerializer(data=request.data)
		print(serializer)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data , status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScrapStatus(APIView):
	def get(self,request):
		status = phones.objects.all().count()
		return Response(status)

class PhoneBrands(APIView):
	def get(self,request):
		model = phones.objects.values('brand').distinct()
		#serializer = PhonesSerializer(model,many=True)
		return Response(model)

class PhoneByBrand(APIView):
	def get(self,request):
		reqbrand = request.GET['brand']

		data = phones.objects.all().filter(brand = reqbrand)
		serializer = PhonesSerializer(data,many=True)
		return Response(serializer.data)
