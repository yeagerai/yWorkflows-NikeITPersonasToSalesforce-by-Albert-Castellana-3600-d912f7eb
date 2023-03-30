
# NikeITPersonasToSalesforce

This workflow fetches the list of Nike IT Department personas, extracting their name and email address, and stores the data in a list of dictionaries. As there are no inputs, the processing will happen automatically when triggered.


## Initial generation prompt
description: "IOs - Inputs: N/A\nOutputs:\n- personas_data: A list of dictionaries\
  \ containing the name and email address of each\n    Nike IT department persona.\n"
name: NikeITPersonasToSalesforce


## Transformer breakdown
- Initialize empty list to store persona data
- Fetch list of Nike IT Department personas
- Iterate through personas, extracting their name and email address
- Append extracted name and email address to personas_data list as a dictionary

## Parameters
[]

        