import subprocess
import argparse

def init_repo():
    """Initialize a new Git repository."""
    subprocess.run(["git", "init"])

def check_status():
    """Check the status of the Git repository."""
    subprocess.run(["git", "status"])

def add_files(files):
    """Add files to the staging area."""
    subprocess.run(["git", "add"] + files)

def commit_changes(message):
    """Commit changes with a message."""
    subprocess.run(["git", "commit", "-m", message])

def push_changes(remote, branch):
    """Push changes to the specified remote and branch."""
    subprocess.run(["git", "push", remote, branch])

def pull_changes(remote, branch):
    """Pull changes from the specified remote and branch."""
    subprocess.run(["git", "pull", remote, branch])

def merge_branch(branch):
    """Merge the specified branch into the current branch."""
    subprocess.run(["git", "merge", branch])

def main():
    parser = argparse.ArgumentParser(description="A custom CLI for Git operations")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("init", help="Initialize a new Git repository")

    subparsers.add_parser("status", help="Show the working tree status")

    add_parser = subparsers.add_parser("add", help="Add file contents to the index")
    add_parser.add_argument("files", nargs="+", help="Files to add")

    commit_parser = subparsers.add_parser("commit", help="Record changes to the repository")
    commit_parser.add_argument("-m", "--message", required=True, help="Commit message")

    push_parser = subparsers.add_parser("push", help="Update remote refs along with associated objects")
    push_parser.add_argument("remote", help="Name of the remote to push to")
    push_parser.add_argument("branch", help="Branch to push to")

    pull_parser = subparsers.add_parser("pull", help="Fetch from and integrate with another repository")
    pull_parser.add_argument("remote", help="Name of the remote to pull from")
    pull_parser.add_argument("branch", help="Branch to pull from")

    merge_parser = subparsers.add_parser("merge", help="Join two or more development histories together")
    merge_parser.add_argument("branch", help="Branch to merge into the current branch")

    args = parser.parse_args()

    if args.command == "init":
        init_repo()
    elif args.command == "status":
        check_status()
    elif args.command == "add":
        add_files(args.files)
    elif args.command == "commit":
        commit_changes(args.message)
    elif args.command == "push":
        push_changes(args.remote, args.branch)
    elif args.command == "pull":
        pull_changes(args.remote, args.branch)
    elif args.command == "merge":
        merge_branch(args.branch)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
