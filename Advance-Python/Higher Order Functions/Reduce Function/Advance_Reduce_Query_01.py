'''
Scenario 1: Website Traffic Analysis (Calculating Average Page View Duration)

Story:
You are working as a data scientist at a digital marketing agency. Your task is to analyze the performance of multiple web pages on the company's website. Each page has a list of users who visited the page, and you are tasked with calculating the average page view duration for the entire website.

Problem:
You are given a list of dictionaries, each representing a webpage with the following attributes:
- page_name: The name of the webpage (e.g., "Home", "Products").
- page_views: The total number of page views for that page.
- total_duration: The total time spent by all users on that page (in seconds).

Objective:
- Calculate the average page view duration for each page.
- Then compute the overall average page view duration for the entire website.

Formulae:
1. To calculate the average page view duration for each page:

    average_page_view_duration = lambda total_duration, page_views: total_duration / page_views
    
    Where:
    - `total_duration` is the total time spent by all users on that page.
    - `page_views` is the number of times the page was viewed.

2. To calculate the overall average page view duration for the entire website:
    - Compute the average for each page using the above formula.
    - Sum the average page durations across all pages and divide by the number of pages to get the overall average:
    \[
    \text{Overall Average Page View Duration} = \frac{\sum (\text{Average Page View Duration of each page})}{\text{Number of Pages}}
    \]
    
Hint:
- Use the `reduce()` function to compute the sum of all individual average durations across all pages.
- After obtaining the sum of average durations, divide it by the total number of pages to get the final result.

'''

website_data = [
    {"page_name": "Home", "page_views": 1500, "total_duration": 45000},
    {"page_name": "Products", "page_views": 1200, "total_duration": 36000},
    {"page_name": "Contact", "page_views": 850, "total_duration": 17000},
    {"page_name": "About Us", "page_views": 500, "total_duration": 12000},
    {"page_name": "Blog", "page_views": 2000, "total_duration": 55000},
    {"page_name": "FAQ", "page_views": 750, "total_duration": 18000},
    {"page_name": "Services", "page_views": 950, "total_duration": 21000},
    {"page_name": "Careers", "page_views": 650, "total_duration": 14000},
    {"page_name": "Privacy Policy", "page_views": 400, "total_duration": 8000},
    {"page_name": "Terms of Service", "page_views": 450, "total_duration": 9000},
    {"page_name": "Help Center", "page_views": 1100, "total_duration": 26000},
    {"page_name": "Support", "page_views": 700, "total_duration": 14000},
    {"page_name": "News", "page_views": 1300, "total_duration": 31000},
    {"page_name": "Events", "page_views": 800, "total_duration": 16000},
    {"page_name": "Store", "page_views": 1600, "total_duration": 48000},
    {"page_name": "Features", "page_views": 900, "total_duration": 22000},
    {"page_name": "Community", "page_views": 950, "total_duration": 19000},
    {"page_name": "Partners", "page_views": 500, "total_duration": 10000},
    {"page_name": "Newsletter", "page_views": 450, "total_duration": 9500} 
]

from functools import reduce
# reduce is used for optimization purposes only 

Average_Website_Traffic = reduce(lambda _,data: _+(data['total_duration']/data["page_views"]),website_data,0)
print(f"""

    Average Website Traffic: {round(Average_Website_Traffic,3)} 
    Overall Website Traffic: {round(Average_Website_Traffic/len(website_data),3)} 
""")
