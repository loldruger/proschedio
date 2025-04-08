# What Is Proschedio? (WIP)
Proschedio is for achieving Infrastructure as Code (IaC) using a declarative approach in `Python`. It allows you to define your infrastructure in a simple and intuitive way, making it easy to manage and deploy your resources.

## Development Environment Setup
To set up the development environment, follow these steps:
1. Install the required dependencies for Ubuntu:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

2. Create a virtual environment and install the package:
```
uv venv
uv pip install .
uv pip install .[dev]
```
