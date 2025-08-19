from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Expense

def home(request):
    if request.method == "POST":
        description = request.POST.get("description", "").strip()
        amount = request.POST.get("amount", "").strip()
        date = request.POST.get("date", "").strip()
        category = request.POST.get("category", "").strip() if "category" in request.POST else ""

        # Basic validation
        if not description or not amount or not date:
            messages.error(request, "Please fill Description, Amount and Date.")
        else:
            try:
                Expense.objects.create(
                    description=description,
                    amount=amount,
                    date=date,
                    category=category,
                )
                messages.success(request, "Expense added.")
                return redirect("home")
            except Exception as e:
                messages.error(request, f"Could not save expense: {e}")

    expenses = Expense.objects.order_by("-date", "-id")
    return render(request, "core/home.html", {"expenses": expenses})

def delete_expense(request, id):
    exp = get_object_or_404(Expense, id=id)
    exp.delete()
    messages.success(request, "Expense removed.")
    return redirect("home")
