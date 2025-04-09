# (WIP) What Is Proschedio?
Proschedio is for achieving Infrastructure as Code (IaC) using a declarative approach in `Python`. It allows 
you to define your infrastructure in a simple and intuitive way, making it easy to manage and deploy your resources.

## Motivation
The motivation behind Proschedio was that this was just a docker compose project that can be deployed by a single command `docker-compose up -d`. And to achieve it, I had to write many ugly shell scripts that were not cross-platform compatible. So I decided to move to `Python` and use `asyncio` to make it more efficient and easy to manage. I also wanted to make it easy to add support for different providers, so I designed the project in a way that allows for easy extensibility.

## Features
working on dividing the project into three modules Resource, Action, and Schedule. The Resource module is responsible for managing the resources, the Action module is responsible for managing the actions that can be performed on the resources, and the Schedule module is responsible for managing the scheduling of the actions.

- **Resource**: The Resource module is responsible for managing the resources. It allows you to create, delete, and manage your resources in a simple and intuitive way.
- **Action**: The Action module is responsible for managing the actions that can be performed on the resources. It allows you to define the actions that can be performed on the resources and manage them in a simple and intuitive way.
- **Schedule**: The Schedule module is responsible for managing the scheduling of the actions. It allows you to define the schedule for the actions and manage them in a simple and intuitive way.

## Supported Providers
- Vultr
- ~~iwinv~~ (no api support yet)
- ~~AWS~~ (coming soon)
- ~~Azure~~ (coming soon)
- ~~GCP~~ (coming soon)

## Example Usage (Currently unavailable this example due to entirely refactoring the code)
```python
import asyncio
from proschedio import (Resource, Action, Schedule)

Resource.register("vultr")

async def main():

    server_instance = await Resource.instance(
        provider=Provider("vultr"),
        plan="vc2-1c-1gb",
        region="ewr",
        hostname="test-create-and-delete",
        properties={
            "label": "test-proschedio",
            "tags": "test-proschedio",
            "backups": "disabled",
            "ddos_protection": "disabled",
            "enable_ipv6": "disabled",
        }
    )
    .create()

    await Resource.server_instance.delete()

if __name__ == "__main__":
    asyncio.run(main())
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

3. Put your API keys in a `.env` file in the root directory of your project.

You have to set up your environment variables for the providers you want to use. For example, for Vultr, you need to set the `PROVIDER_API_KEY` environment variable. * **It would be replaced with the .toml file in the future** *

variables from a `.env` file at the root of the project directory. Create a `.env` file in the root directory of your project and add your API keys there.

in `.env` file:

```bash
PROVIDER_API_KEY=your_provider_api_key
```

## Loadmap
### Plugin System
- [ ] Add support for a plugin system to allow for easy extensibility

### Support for More Providers
- [ ] Add support for iwinv
- [ ] Add support for AWS
- [ ] Add support for Azure
- [ ] Add support for GCP

### Support for Features
- [ ] fetch products, regions, and plans from the provider
- [ ] Retry mechanism
- [ ] Add support for scheduling jobs for each provider's resources
- [ ] Add More features for orchestrating resources