import os
import subprocess

def main(project_name):
    if project_name == 'list':
        print(" | ".join(os.listdir("/home/matty/workspace/")))
        return None


    project_directory = f"/home/matty/workspace/{project_name}"

    if not os.path.exists(project_directory):
        print(f'project {project_name} is new.  Create it?([y]es/no):')
        should_create_input = input().strip()
        if should_create_input != 'yes' and should_create_input != 'y':
            print('exiting...')
            return None

    if not os.path.exists(project_directory):
        print("createing  project directory...")
        os.mkdir(project_directory)

    os.chdir(project_directory)


    if not os.path.exists('env'):
        print("\ncreateing virtualenv...")
        subprocess.run(["virtualenv", "env", '-p', 'python3'])
        print("\ninstalling coverage.py...")
        subprocess.run(['./env/bin/pip', 'install', 'coverage'])

    if not os.path.exists('.git'):
        print("\ncreateing git...")
        cp = subprocess.run(["git", "init"])


if __name__ == '__main__':
    import plac; plac.call(main)
