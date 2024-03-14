from django.shortcuts import render
from django.db import connection
from .models import DatabaseLog

def connect_to_database(request):
    """View function for connecting to the database."""
    # No specific action required here as Django handles database connection automatically
    return render(request, 'database_manager/connect_to_database.html')

def query_database(request):
    """View function for querying the database."""
    if request.method == 'POST':
        query = request.POST.get('query')
        # Execute the query on the database
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        # Log the query execution
        log_entry = DatabaseLog.objects.create(message=f"Query executed: {query}")
        return render(request, 'database_manager/query_result.html', {'results': results, 'query': query, 'log_entry': log_entry})
    return render(request, 'database_manager/query_database.html')

def database_insert(request):
    """View function for inserting data into the database."""
    if request.method == 'POST':
        # Process form data to insert data into the database
        # Example: data = DataModel.objects.create(field1=request.POST['field1'], field2=request.POST['field2'])
        # Replace 'DataModel.objects.create' with your actual logic for inserting data
        # Log the data insertion
        log_entry = DatabaseLog.objects.create(message="Data inserted into the database")
        return render(request, 'database_manager/insert_success.html', {'log_entry': log_entry})
    return render(request, 'database_manager/insert_form.html')
