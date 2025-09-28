#!/usr/bin/env python
import os
import sys
import subprocess

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)

if __name__ == "__main__":
    print("Setting up Django project...")
    
    # Collect static files
    run_command("python manage.py collectstatic --noinput")
    
    # Make migrations
    run_command("python manage.py makemigrations")
    
    # Apply migrations
    run_command("python manage.py migrate")
    
    print("Starting Django development server...")
    run_command("python manage.py runserver")