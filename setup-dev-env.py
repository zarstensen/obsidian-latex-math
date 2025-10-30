import os
import subprocess
import venv

venv_bin_folder = "Scripts" if os.name == "nt" else "bin"

print("Creating virtual environment")

venv_dir = os.path.join(os.getcwd(), ".venv")
builder = venv.EnvBuilder(with_pip=True)
builder.create(venv_dir)

print("Installing venv dependencies")

pip_executable = os.path.join(venv_dir, venv_bin_folder, "pip")
subprocess.check_call([pip_executable, "install", "-r", "requirements.txt", "-r", "requirements-dev.txt"])
