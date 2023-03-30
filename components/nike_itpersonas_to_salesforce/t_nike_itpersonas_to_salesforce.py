
import pytest
import typing
from typing import List, Dict
from fastapi.testclient import TestClient
from pydantic import BaseModel

from yeager_workflow import (
    NikeITPersonasToSalesforce,
    NikeITPersonasToSalesforceIn,
    NikeITPersonasToSalesforceOut,
)

# Sample data for testing
input_data = [{"name": "John Doe", "email": "john.doe@nike.com"}]

expected_output_data = [{"name": "John Doe", "email": "john.doe@nike.com"}]

# Test cases with input and expected output data
test_data = [
    (input_data, expected_output_data),
    # Add more test cases if needed
]

@pytest.mark.parametrize("mocked_input, expected_output", test_data)
def test_transform(mocked_input: List[Dict[str, str]], expected_output: List[Dict[str, str]]):
    # Initialize the component
    component = NikeITPersonasToSalesforce()

    # Mock the fetch_nike_it_personas method to return the mocked_input data
    async def fetch_nike_it_personas_mock(callbacks) -> List:
        return mocked_input

    component.fetch_nike_it_personas = fetch_nike_it_personas_mock

    # Mock the extract_name_and_email method to return the name and email fields
    def extract_name_and_email_mock(persona) -> (str, str):
        return persona["name"], persona["email"]

    component.extract_name_and_email = extract_name_and_email_mock

    # Call the component's transform() method with mocked input data
    response = component.transform(NikeITPersonasToSalesforceIn(), callbacks=None)

    # Assert that the output matches the expected output data
    assert response.personas_data == expected_output

