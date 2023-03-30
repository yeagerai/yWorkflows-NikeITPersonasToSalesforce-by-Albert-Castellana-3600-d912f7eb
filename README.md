
# NikeITPersonasToSalesforce

This workflow collects personas from the Nike IT department, including their names and emails, and sends this information to Salesforce.

1. The workflow starts by querying LinkedIn profiles, filtering by the company "Nike" and the IT department.
2. For each LinkedIn profile, it extracts the name and email address of the individual.
3. The extracted name and email data is formatted into Salesforce-compatible objects.
4. Finally, these objects are sent to a Salesforce account using the Salesforce API, and are inserted as new Leads.

## Initial generation prompt
a workflow that collects personas from Nike (company) in the IT department, collects the name and email if possible for each of them, and sends it to salesforce

## Authors: 
- yWorkflows
- Albert Castellana#3600
        