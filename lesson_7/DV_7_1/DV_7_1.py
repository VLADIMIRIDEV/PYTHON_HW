import os

k_folder = 'my_project'
v_folder = ['settings', 'mainapp', 'adminapp', 'authapp']
folder_structure = {k_folder: v_folder}

directory = [os.makedirs(os.path.join(k_folder, val))
			 for val in v_folder
			 if not os.path.exists(os.path.join(k_folder, val))]

