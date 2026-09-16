from django.shortcuts import render


from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import mixins
class EmployeeListCreateModelMixin(mixins.CreateModelMixin,ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmployeeRetrieveUpdateDestroy(mixins.UpdateModelMixin, mixins.DestroyModelMixin,RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


