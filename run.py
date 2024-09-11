import subprocess
import argparse
import os

def run_command(command, capture_output=False):
    try:
        result = subprocess.run(
            command, shell=True, check=True,
            text=True, capture_output=capture_output
        )
        if capture_output:
            return result.stdout
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e}")
        exit(1)

def build():
    print("Building the project...")
    # Simulate building step (e.g., compiling assets or building executables)
    run_command("echo 'Build step completed'")

def test():
    print("Running tests...")
    # Execute tests
    run_command("pytest")

def deploy(repo_name):
    print("Creating a new GitHub repository and deploying...")
    
    # Check if the repository is already initialized
    if not os.path.exists('.git'):
        run_command("git init")

    # Add and commit changes
    run_command("git add .")
    run_command("git commit -m 'Initial commit'")

    # Create repository on GitHub
    run_command(f"gh repo create {repo_name} --public --source=. --remote=origin")

    # Push to GitHub
    run_command("git push origin main")

def main():
    parser = argparse.ArgumentParser(description="Build, test, and deploy a Python program.")
    parser.add_argument('--repo', type=str, help='Name of the GitHub repository to deploy to.')
    args = parser.parse_args()

    if not args.repo:
        args.repo = input('Enter the name of the GitHub repository to deploy to: ')

    build()
    test()
    deploy(args.repo)

if __name__ == "__main__":
    main()
