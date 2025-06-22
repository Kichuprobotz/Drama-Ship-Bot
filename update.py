import sys
from os import environ, path
from subprocess import run

UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/Kichuprobotz/Drama-Ship-Bot.git").strip()
if not UPSTREAM_REPO:
    UPSTREAM_REPO = "https://github.com/Kichuprobotz/Drama-Ship-Bot.git"

UPSTREAM_BRANCH = environ.get("UPSTREAM_BRANCH", "main").strip()
if not UPSTREAM_BRANCH:
    UPSTREAM_BRANCH = "main"

# Remove old .git folder if exists
if path.exists(".git"):
    run(["rm", "-rf", ".git"], check=False)

# Initialize new git repo and pull updates
update = run(
    f"""git init -q && \
        git config --global user.email "bp704166@gmail.com" && \
        git config --global user.name "IronmanHUB4VF" && \
        git add . && \
        git commit -sm "update" -q && \
        git remote add origin {UPSTREAM_REPO} && \
        git fetch origin -q && \
        git reset --hard origin/{UPSTREAM_BRANCH} -q""",
    shell=True,
)

if update.returncode == 0:
    print("✅ Successfully updated from UPSTREAM_REPO.")
else:
    print("❌ Failed to update. Check if UPSTREAM_REPO and UPSTREAM_BRANCH are correct.")
    sys.exit(1)
