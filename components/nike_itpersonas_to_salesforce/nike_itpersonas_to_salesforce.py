
import typing
from typing import List, Dict
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class NikeITPersonasToSalesforceIn(BaseModel):
    pass


class NikeITPersonasToSalesforceOut(BaseModel):
    personas_data: List[Dict[str, str]]


class NikeITPersonasToSalesforce(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: NikeITPersonasToSalesforceIn, callbacks: typing.Any
    ) -> NikeITPersonasToSalesforceOut:
        personas_data = []

        # Fetch list of Nike IT Department personas
        personas_list = await self.fetch_nike_it_personas(callbacks)

        # Iterate through personas, extracting their name and email address
        for persona in personas_list:
            name, email = self.extract_name_and_email(persona)
            personas_data.append({"name": name, "email": email})

        out = NikeITPersonasToSalesforceOut(personas_data=personas_data)
        return out

    async def fetch_nike_it_personas(self, callbacks) -> List:
        # Implement method to fetch the list of Nike IT Department personas
        pass

    def extract_name_and_email(self, persona) -> (str, str):
        # Implement method to extract name and email address from persona
        pass

load_dotenv()
nike_it_personas_to_salesforce_app = FastAPI()


@nike_it_personas_to_salesforce_app.post("/transform/")
async def transform(
    args: NikeITPersonasToSalesforceIn,
) -> NikeITPersonasToSalesforceOut:
    nike_it_personas_to_salesforce = NikeITPersonasToSalesforce()
    return await nike_it_personas_to_salesforce.transform(args, callbacks=None)

