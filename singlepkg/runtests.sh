#! /bin/bash

find . -name "*.pyc" -exec rm {}\;
coverage run -p --source=tests,helloworld -m unittest
coverage combine
echo -e "\n\n===================================================="
echo "Test Coverage"
coverage report -m
echo -e "\nrun \"coverage html\" for full report"
echo -e "\n"

# pyflakes or its like should go here

