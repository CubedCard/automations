import sys
import os
import requests
from bs4 import BeautifulSoup as bs

def extract_problem_description(problem_url):
    title_slug = problem_url.split("/")[-1]

    data = {
        "operationName": "questionData",
        "variables": {"titleSlug": title_slug},
        "query": """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            title
            content
          }
        }
        """
    }

    response = requests.post('https://leetcode.com/graphql', json=data).json()

    question_data = response['data']['question']
    title = question_data['title']
    soup = bs(question_data['content'], 'lxml')
    problem_description = soup.get_text()

    return title, problem_description

def create_new_problem(title, description):
    title = title.replace(" ", "-")
    title = title.replace(".", "").lower()

    if os.path.exists(title):
        print("Problem already exists")
        return
    else:
        os.mkdir(title)
        os.chdir(title)
        with open("README.md", "w", encoding="utf-8") as f:
            description = description.replace("Example", "## Example")
            description = description.replace("Constraints", "## Constraints")
            f.write(f"# {title}\n\n")
            f.write(description)
            f.write("\n\nCopyright ????? 2024 LeetCode All rights reserved")
        os.chdir("..")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <problem_url>")
        sys.exit(1)

    problem_url = sys.argv[1]
    title, description = extract_problem_description(problem_url)
    create_new_problem(title, description)