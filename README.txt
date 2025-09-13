This directory is for a basic website that I designed to submit 
assignments for global Illuminations.

Hosting was done for free with GitHub pages
- url KevinJSL.github.io

How to use:
- create venv: <python -m venv .venv>
- activate (on windows): <.venv\Scripts\Activate>
    - try <Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force>
    if you are getting a permission error 
- get imports: <pip install -r requirements.txt>

For local development:
- run route.py
- Navigate to http://127.0.0.1:5000

Actual Cite:
- run route.py build
- Upload the build directory to AWS s3 bucket
- Navigate to www.kevinland.portfolio