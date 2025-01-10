import re
import pyperclip

def generate_branch_name(title: str, number: str) -> str:
    """
    Generates a branch name in the format 'feature/sif-<number>-<sanitized-title>'.
    """
    sanitized_title = re.sub(r'[^a-zA-Z0-9-]', '', title.replace(" ", "-")).lower()
    sanitized_title = re.sub(r'-+', '-', sanitized_title)
    return f"feature/sif-{number}-{sanitized_title}"

def main():
    try:
        title = input("Enter title: ").strip()
        number = input("Enter number: ").strip()

        if not title or not number:
            raise ValueError("Both title and number must be provided.")
        
        branch_name = generate_branch_name(title, number)
        print(f"Generated branch name: {branch_name}")

        try:
            pyperclip.copy(branch_name)
            print("Branch name copied to clipboard.")
        except pyperclip.PyperclipException:
            print("Unable to copy to clipboard. Please copy manually.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
