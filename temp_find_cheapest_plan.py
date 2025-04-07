
import asyncio
import os
import json
import sys
from dotenv import load_dotenv

# Assuming API functions and set_key are importable
# Adjust imports based on actual project structure if needed
try:
    from vultr.apis.plans_metal import list_metal_plans
    from vultr import set_key
except ImportError:
    print("Error: Could not import Vultr API functions. Make sure src directory is in PYTHONPATH or script is run from project root.")
    sys.exit(1)

async def find_cheapest():
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get('VULTR_API_KEY')

    if not api_key:
        print("Error: VULTR_API_KEY not found in environment variables.")
        return

    # Set the API key for the API functions
    set_key(api_key)

    print("Fetching bare metal plans...")
    try:
        response_dict = await list_metal_plans(per_page=None, cursor=None)
    except Exception as e:
        print(f"Error calling list_metal_plans: {e}")
        return

    status = response_dict.get("status")
    data = response_dict.get("data")

    if status != 200:
        print(f"Error: API returned status {status}")
        print(f"Response data: {data}")
        return

    plans = data.get("plans_metal", [])

    if not plans:
        print("No bare metal plans found.")
        return

    cheapest_plan = None
    min_cost = float('inf')

    for plan in plans:
        cost = plan.get("monthly_cost")
        if cost is not None and cost < min_cost:
            min_cost = cost
            cheapest_plan = plan

    if cheapest_plan:
        print("\n--- Cheapest Bare Metal Plan ---")
        print(f"ID: {cheapest_plan.get('id')}")
        print(f"Monthly Cost: ${cheapest_plan.get('monthly_cost')}")
        print(f"CPU Count: {cheapest_plan.get('cpu_count')}")
        print(f"RAM: {cheapest_plan.get('ram')} MB")
        print(f"Disk: {cheapest_plan.get('disk')} GB (Count: {cheapest_plan.get('disk_count')})")
        print(f"Locations: {cheapest_plan.get('locations')}")
    else:
        print("Could not determine the cheapest plan.")

if __name__ == "__main__":
    asyncio.run(find_cheapest())
