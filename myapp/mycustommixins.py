from django.shortcuts import render


class MyCustGenListMixin:
    cust_data = None
    template = None

    def get(self, request):
        return render(request, self.template, self.cust_data)
