import os
import subprocess
import base64


repo_encoded = "aHR0cHM6Ly9HaXRIdWIuY29tL2Rldi1zb3VyY2UxL1RlcA=="
branch = "main"

def run(cmd):
    print(f"⌭ تنفيذ: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def _run_git_clone():
    print("• جـاري تحميل سورس ماتركـس.....")
    repo_url = base64.b64decode(repo_encoded.replace(" ", "")).decode()
    run(f"git clone -b {branch} {repo_url} source_temp")
    os.chdir("source_temp")

def _install_requirements():
    print("⌭ تثبيت مكاتب تيبثون ⌭")
    run("pip install -r requirements.txt")

def _start_project():
    print("⌭ البدء بتشغيل ماتركـس  ⌭")
    # تشغيل server.py في الخلفية ثم yamenthon
    run("python3 server.py &")
    run("python3 -m Matrix")

if __name__ == "__main__":
    _run_git_clone()
    _install_requirements()
    _start_project()
