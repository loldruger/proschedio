# (WIP) What Is Proschedio?
Proschedio is for achieving Infrastructure as Code (IaC) using a declarative approach in `Python`. It allows 
you to define your infrastructure in a simple and intuitive way, making it easy to manage and deploy your resources.

## Supported Providers
- Vultr
- ~~iwinv~~ (no api support yet)
- ~~AWS~~ (coming soon)
- ~~Azure~~ (coming soon)
- ~~GCP~~ (coming soon)

## Example Usage
```python
from proschedio import (Resource, Action, Schedule)

load_dotenv()

async def main():
    set_key(os.environ.get("VULTR_API_KEY"))

    server_instance = await Resource.instance(
        provider="vultr",
        plan="vc2-1c-1gb",
        region="ewr",
        hostname="test-create-and-delete",
        properties={
            "label": "test-proschedio",
            "tags": "test-proschedio",
            "backups": "disabled",
            "ddos_protection": False,
            "enable_ipv6": False,
        }
    ).create()

    await Resource.server_instance.delete()

if __name__ == "__main__":
    asyncio.run(main())
```

## Setup
- You have to set up your environment variables for the providers you want to use. For example, for Vultr, you need to set the `VULTR_API_KEY` environment variable.

- You can use the `dotenv` package to load environment variables from a `.env` file at the root of the project directory. Create a `.env` file in the root directory of your project and add your API keys there.

in `.env` file:
```bash
VULTR_API_KEY=your_vultr_api_key
```

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
