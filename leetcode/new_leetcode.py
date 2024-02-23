import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def extract_problem_description(problem_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    title_class = "text-title-large"
    description_class = "elfjS"

    driver.get(problem_url)

    title = driver.find_element(By.CLASS_NAME, title_class)
    problem_description = driver.find_element(By.CLASS_NAME, description_class)

    return title.text, problem_description.text

def create_new_problem(title, description):
    if os.getcwd().split("/")[-1] != "leetcode":
        print("Please run this script from the leetcode directory")
        return

    title = title.replace(" ", "-")
    title = title.replace(".", "").lower()

    if os.path.exists(title):
        print("Problem already exists")
        return
    else:
        os.mkdir(title)
        os.chdir(title)
        with open("README.md", "w") as f:
            description = description.replace("Example", "## Example")
            description = description.replace("Constraints", "## Constraints")
            f.write(f"# {title}\n\n")
            f.write(description)
            f.write("\n\nCopyright ©️ 2024 LeetCode All rights reserved")
        os.chdir("..")

problem_url = sys.argv[1]
problem_url = problem_url.replace("description/", "")
title, description = extract_problem_description(problem_url)
print(title, description)
create_new_problem(title, description)
