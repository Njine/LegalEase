from django.shortcuts import render
from django.db import connection

def connect_to_database(request):
    """View function for connecting to the database."""
    # Implement your database connection logic here
    # Example: connection.connect_to_database(host, username, password, database)
    # Replace 'connection.connect_to_database' with your actual function for connecting to the database
    return render(request, 'database_manager/connect_to_database.html')

def query_database(request):
    """View function for querying the database."""
    if request.method == 'POST':
        query = request.POST.get('query')
        # Execute the query on the database
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return render(request, 'database_manager/query_result.html', {'results': results, 'query': query})
    return render(request, 'database_manager/query_database.html')
