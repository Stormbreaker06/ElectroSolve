from django.shortcuts import render, redirect
from .models import Problem

def homepage(request):
    return render(request, 'homepage.html')  # Render the homepage template

def problem_list(request):
    problems = Problem.objects.all()  # Fetch all problems
    return render(request, 'problem_list.html', {'problems': problems})

def problem_detail(request, problem_id):
    problem = Problem.objects.get(id=problem_id)  # Fetch a specific problem
    
    # Pass the individual options fields instead of 'options'
    return render(request, 'problem_detail.html', {
        'problem': problem,
        'option_a': problem.option_a,
        'option_b': problem.option_b,
        'option_c': problem.option_c,
        'option_d': problem.option_d,
    })

def check_answer(request, problem_id):
    if request.method == "POST":
        selected_answer = request.POST.get('answer')
        problem = Problem.objects.get(id=problem_id)

        # Check if the selected answer is correct
        is_correct = (selected_answer == problem.correct_answer)

        # Pass the individual options fields here as well
        return render(request, 'problem_detail.html', {
            'problem': problem,
            'option_a': problem.option_a,
            'option_b': problem.option_b,
            'option_c': problem.option_c,
            'option_d': problem.option_d,
            'solution_display': is_correct,
        })
