import pytest
import logging
import json  # Import json

# Import the specific function
from vultr.apis.applications import list_applications

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_applications(vultr_client):  # Use vultr_client fixture for consistency
    """
    Tests the list_applications function by calling the API
    and asserting the response structure and types based on OpenAPI spec.
    """
    try:
        # Call the function providing cursor=None explicitly
        response_dict = await list_applications(
            type="all",
            per_page=5,  # Request a small number for testing
            cursor=None  # Provide cursor explicitly
        )
        # Check status code
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        # Access the actual data from the 'data' key
        result = response_dict.get("data", {})

        logger.info(f"\nResponse Data:\n{result}")  # Use f-string

        # Assert top-level keys exist
        assert "applications" in result, "Response should contain 'applications' key"
        assert "meta" in result, "Response should contain 'meta' key"

        # Assert data types
        assert isinstance(result["applications"], list), "'applications' should be a list"
        assert isinstance(result["meta"], dict), "'meta' should be a dictionary"

        # Assert meta structure
        assert "total" in result["meta"], "'meta' should contain 'total' key"
        assert "links" in result["meta"], "'meta' should contain 'links' key"
        assert isinstance(result["meta"]["total"], int), "'meta.total' should be an integer"
        assert isinstance(result["meta"]["links"], dict), "'meta.links' should be a dictionary"

        # Optionally, assert application structure if list is not empty
        if result["applications"]:
            first_app = result["applications"][0]
            assert "id" in first_app, "Application object should have 'id'"
            assert isinstance(first_app["id"], int), "'id' should be an integer"
            assert "name" in first_app, "Application object should have 'name'"
            assert isinstance(first_app["name"], str), "'name' should be a string"
            assert "type" in first_app, "Application object should have 'type'"
            assert isinstance(first_app["type"], str), "'type' should be a string"
            # Add more assertions for expected fields like short_name, vendor, image_id if needed

    except Exception as e:
        logger.error(f"Error during test_list_applications: {e}", exc_info=True)  # Use f-string
        pytest.fail(f"Test failed with error: {e}")  # Use f-string


@pytest.mark.asyncio
async def test_list_applications_pagination(vultr_client):
    """
    Tests the pagination functionality (cursor) of the list_applications endpoint.
    """
    try:
        # 1. Get the first page (per_page=1)
        first_page_response_dict = await list_applications(
            type="all",
            per_page=1,
            cursor=None
        )
        assert first_page_response_dict.get("status") == 200, "First page request failed"
        first_page_data = first_page_response_dict.get("data", {})
        logger.info(f"\nFirst page data:\n{first_page_data}")

        assert "applications" in first_page_data
        assert "meta" in first_page_data and "links" in first_page_data["meta"]

        first_app_id = first_page_data["applications"][0]["id"] if first_page_data["applications"] else None
        next_cursor = first_page_data["meta"]["links"].get("next")

        # Only proceed if there's a next page cursor and at least one app on the first page
        if not next_cursor or first_app_id is None:
            pytest.skip("Not enough applications to test pagination (need at least 2).")

        # 2. Get the next page using the cursor
        logger.info(f"Requesting next page with cursor: {next_cursor}")
        second_page_response_dict = await list_applications(
            type="all",
            per_page=1,
            cursor=next_cursor
        )
        assert second_page_response_dict.get("status") == 200, f"Second page request failed with cursor {next_cursor}"
        second_page_data = second_page_response_dict.get("data", {})
        logger.info(f"\nSecond page data:\n{second_page_data}")

        assert "applications" in second_page_data, "Second page should contain 'applications' key"
        assert isinstance(second_page_data["applications"], list), "Second page 'applications' should be a list"

        # 3. Verify the second page has data and it's different from the first
        assert len(second_page_data["applications"]) > 0, "Second page should contain at least one application"
        second_app_id = second_page_data["applications"][0]["id"]
        assert first_app_id != second_app_id, "Application ID on the second page should be different from the first page"

        # (Optional) 4. Test previous page navigation
        prev_cursor = second_page_data.get("meta", {}).get("links", {}).get("prev")
        if prev_cursor:
            logger.info(f"Requesting previous page with cursor: {prev_cursor}")
            prev_page_response_dict = await list_applications(
                type="all",
                per_page=1,
                cursor=prev_cursor
            )
            assert prev_page_response_dict.get("status") == 200, f"Previous page request failed with cursor {prev_cursor}"
            prev_page_data = prev_page_response_dict.get("data", {})
            logger.info(f"\nPrevious page data:\n{prev_page_data}")
            assert "applications" in prev_page_data and len(prev_page_data["applications"]) > 0
            prev_app_id = prev_page_data["applications"][0]["id"]
            assert prev_app_id == first_app_id, "Previous page should contain the same application as the first page"

    except Exception as e:
        logger.error(f"Error during test_list_applications_pagination: {e}", exc_info=True)
        pytest.fail(f"Pagination test failed with error: {e}")