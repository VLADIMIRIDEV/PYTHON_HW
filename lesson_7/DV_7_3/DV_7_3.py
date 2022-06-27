import shutil


def copy_files_dir(name):
	shutil.copytree(f'my_projects/{name}/templates', f'my_projects/templates', dirs_exist_ok=True)


if __name__ == '__main__':
	copy_files_dir('authapp')
	copy_files_dir('mainapp')