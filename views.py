from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render

def demo(request):
    result = ""

    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operation = request.POST.get("operation")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"

    return render(request, "index.html", {"result": result})
