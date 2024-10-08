import setuptools

# Load the long description from the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define package version, name, and author details
setuptools.setup(
    name="credit_default",  # Replace with your package name
    version="0.0.1",  # Initial version
    author="Ayush Bhavsar",  # Replace with your name
    author_email="youremail@example.com",  # Replace with your email
    description="An end-to-end machine learning project for credit default prediction.",  # Brief description
    long_description=long_description,  # Full description (from README.md)
    long_description_content_type="text/markdown",  # Type of README (Markdown in this case)
    url="https://github.com/ayushbhavsar21/Credit_Card",  # URL of the project (e.g., GitHub repo)

    # Specify the project structure
    package_dir={"": "src"},  # Tell Python that your package lives in `src/`
    packages=setuptools.find_packages(where="src"),  # Automatically discover all packages under `src/`
    
    # Add dependencies from requirements.txt
    install_requires=[
        "anyio==4.6.0",
        "argon2-cffi==23.1.0",
        "argon2-cffi-bindings==21.2.0",
        "arrow==1.3.0",
        "asttokens==2.4.1",
        "async-lru==2.0.4",
        "attrs==24.2.0",
        "babel==2.16.0",
        "beautifulsoup4==4.12.3",
        "bleach==6.1.0",
        "blinker==1.8.2",
        "certifi==2024.8.30",
        "cffi==1.17.1",
        "charset-normalizer==3.3.2",
        "click==8.1.7",
        "colorama==0.4.6",
        "comm==0.2.2",
        "contourpy==1.3.0",
        "cycler==0.12.1",
        "debugpy==1.8.6",
        "decorator==5.1.1",
        "defusedxml==0.7.1",
        "ensure==1.0.2",
        "executing==2.1.0",
        "fastjsonschema==2.20.0",
        "Flask==3.0.3",
        "Flask-Cors==5.0.0",
        "fonttools==4.54.1",
        "fqdn==1.5.1",
        "h11==0.14.0",
        "httpcore==1.0.6",
        "httpx==0.27.2",
        "idna==3.10",
        "imbalanced-learn==0.12.3",
        "imblearn==0.0",
        "ipykernel==6.29.5",
        "ipython==8.27.0",
        "isoduration==20.11.0",
        "itsdangerous==2.2.0",
        "jedi==0.19.1",
        "Jinja2==3.1.4",
        "joblib==1.4.2",
        "json5==0.9.25",
        "jsonpointer==3.0.0",
        "jsonschema==4.23.0",
        "jsonschema-specifications==2023.12.1",
        "jupyter-events==0.10.0",
        "jupyter-lsp==2.2.5",
        "jupyter_client==8.6.3",
        "jupyter_core==5.7.2",
        "jupyter_server==2.14.2",
        "jupyter_server_terminals==0.5.3",
        "jupyterlab==4.2.5",
        "jupyterlab_pygments==0.3.0",
        "jupyterlab_server==2.27.3",
        "kiwisolver==1.4.7",
        "markdown-it-py==3.0.0",
        "MarkupSafe==2.1.5",
        "matplotlib==3.9.2",
        "matplotlib-inline==0.1.7",
        "mdurl==0.1.2",
        "mistune==3.0.2",
        "nbclient==0.10.0",
        "nbconvert==7.16.4",
        "nbformat==5.10.4",
        "nest-asyncio==1.6.0",
        "notebook==7.2.2",
        "notebook_shim==0.2.4",
        "numpy==1.26.4",
        "overrides==7.7.0",
        "packaging==24.1",
        "pandas==2.2.3",
        "pandocfilters==1.5.1",
        "parso==0.8.4",
        "pillow==10.4.0",
        "platformdirs==4.3.6",
        "plotly==5.24.1",
        "polars==0.20.31",
        "prometheus_client==0.21.0",
        "prompt_toolkit==3.0.48",
        "psutil==6.0.0",
        "pure_eval==0.2.3",
        "pyarrow==16.1.0",
        "pycparser==2.22",
        "Pygments==2.18.0",
        "pyparsing==3.1.4",
        "python-box==6.0.2",
        "python-dateutil==2.9.0.post0",
        "python-json-logger==2.0.7",
        "pytz==2024.2",
        "pywin32==306",
        "pywinpty==2.0.13",
        "PyYAML==6.0.2",
        "pyzmq==26.2.0",
        "referencing==0.35.1",
        "requests==2.32.3",
        "rfc3339-validator==0.1.4",
        "rfc3986-validator==0.1.1",
        "rich==13.9.1",
        "rpds-py==0.20.0",
        "scikit-learn==1.5.2",
        "scipy==1.14.1",
        "seaborn==0.13.2",
        "Send2Trash==1.8.3",
        "setuptools==75.1.0",
        "six==1.16.0",
        "skimpy==0.0.15",
        "sniffio==1.3.1",
        "soupsieve==2.6",
        "stack-data==0.6.3",
        "tenacity==9.0.0",
        "terminado==0.18.1",
        "threadpoolctl==3.5.0",
        "tinycss2==1.3.0",
        "tornado==6.4.1",
        "traitlets==5.14.3",
        "typeguard==4.2.1",
        "types-python-dateutil==2.9.0.20240906",
        "types-PyYAML==6.0.12.20240917",
        "typing_extensions==4.12.2",
        "tzdata==2024.2",
        "uri-template==1.3.0",
        "urllib3==2.2.3",
        "wcwidth==0.2.13",
        "webcolors==24.8.0",
        "webencodings==0.5.1",
        "websocket-client==1.8.0",
        "Werkzeug==3.0.4",
        "xgboost==2.1.1",
    ],
    
    # Optional metadata like license, classifiers, and keywords
    classifiers=[
        "Programming Language :: Python :: 3",  # Python version
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",
    ],
    
    python_requires='>=3.6',  # Specify Python version compatibility
    
    # Additional URLs (e.g., for bug reports, documentation)
    project_urls={
        "Bug Tracker": "https://github.com/ayushbhavsar21/Credit_Card/issues",
    },
)
