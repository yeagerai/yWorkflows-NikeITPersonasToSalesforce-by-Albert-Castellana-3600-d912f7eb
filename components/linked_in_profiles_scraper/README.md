
# LinkedInProfilesScraper

Queries LinkedIn to find profiles of employees in the specified company and department. Filters by company and department, returning a list of profile URLs.

## Initial generation prompt
description: Queries LinkedIn to find profiles of employees in the Nike IT department.
  Filters by company and department, returning a list of profile URLs.
inputs:
- company: str
- department: str
name: LinkedInProfilesScraper
outputs:
- profile_urls: List[str]


## Transformer breakdown
- Load input company and department
- Query LinkedIn
- Filter results by company and department
- Extract profile URLs
- Return list of profile URLs

## Parameters
[]

        