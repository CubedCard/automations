import requests

def get_problem_description(problem_id):
    url = f"https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    query = '''
    {
        problem(problemId: ''' + str(problem_id) + ''') {
            question {
                questionId
                title
                titleSlug
                content
            }
        }
    }
    '''
    data = {'operationName': None, 'variables': {}, 'query': query}
    response = requests.post(url, headers=headers, json=data)
    with open("response.html", "w") as file:
        file.write(response.text)
    if response.status_code == 200:
        json_data = response.json()
        question = json_data['data']['problem']['question']
        return {
            "title": question['title'],
            "content": question['content']
        }
    else:
        print("Error occurred while fetching the problem description.")
        return None

if __name__ == "__main__":
    problem_id = input("Enter the problem ID: ")
    description = get_problem_description(problem_id)
    if description:
        print("Title:", description['title'])
        print("Description:")
        print(description['content'])

