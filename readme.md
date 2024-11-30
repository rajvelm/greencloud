ram shankar
13:38
https://phoenixnap.com/kb/install-ansible-on-windows
keep
Pinned
ram shankar
14:07
https://www.virtualbox.org/wiki/Downloads
keep
Pinned
ram shankar
14:12
https://andreypicado.com/ansible-runner-ansible-from-python-code/
keep
Pinned
You
14:25
Traceback (most recent call last):
  File "C:\Users\Socgen\PycharmProjects\PythonProject\Hello\HelloWorld.py", line 1, in <module>
    import ansible_runner
  File "C:\Users\Socgen\PycharmProjects\PythonProject\Hello\.venv\Lib\site-packages\ansible_runner\__init__.py", line 1, in <module>
    from .utils.importlib_compat import importlib_metadata
  File "C:\Users\Socgen\PycharmProjects\PythonProject\Hello\.venv\Lib\site-packages\ansible_runner\utils\__init__.py", line 9, in <module>
    import f
File "C:\Users\Socgen\PycharmProjects\PythonProject\Hello\.venv\Lib\site-packages\ansible_runner\utils\__init__.py", line 9, in <module>
    import fcntl
ModuleNotFoundError: No module named 'fcntl'
ram shankar
14:31
pip install waitress
keep
Pinned
ram shankar
14:36
pip install ansible-runner
keep
Pinned
ram shankar
14:43
1. Run as admin the powershell
keep
Pinned
2. Follow steps to install WSL and ansible
keep
Pinned
https://phoenixnap.com/kb/install-ansible-on-windows
keep
Pinned
You
14:44
3. sudo apt install python3-ansible-runner
keep
Pinned
ram shankar
14:45
4. created a greencloud folder under /home/socgen
keep
Pinned
5. created a sample ansible inventory file inventory.yml in /home/socgen/greencloud
keep
Pinned
ram shankar
14:46
6. Created a sample ansible runner python file
keep
Pinned
You
14:46
python HelloWorld.py
import ansible_runner

r = ansible_runner.run(
    inventory='/home/socgen/greencloud/inventory.yml',
    module='ping',
    host_pattern='all'
)
python HelloWorld.py
ram shankar
15:06
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
yxk-spoy-nno
