import os

# Directory Path
path = "./ansible-test"
path_group = path + "/development/group_vars"
path_host = path + "/development/host_vars"
path_role = path + "/role/common"

path_task = path + "/role/common/tasks"
path_file = path + "/role/common/files"
path_template = path + "/role/common/templates"

# Check if directory already exists
if not os.path.exists(path):
    # Create directory
    try:
        os.makedirs(path_group)
        os.makedirs(path_host)
        os.makedirs(path_role)
        os.makedirs(path_task)
        os.makedirs(path_file)
        os.makedirs(path_template)
        print("Directory created successfully")

        # Cria um arquivo vazio
        hosts_arquivo = os.path.join(path + "/development/", "hosts")
        with open(hosts_arquivo, "w"):
            pass

        group_arquivo = os.path.join(path_group, "group1.yml")
        with open(group_arquivo, "w"):
            pass

        host_arquivo = os.path.join(path_host, "hostname1.yml")
        with open(host_arquivo, "w"):
            pass

        task_arquivo = os.path.join(path_task, "main.yml")
        with open(task_arquivo, "w"):
            pass

        nomes_arquivos = ["site.yml", "README.md", ".gitignore"]
        for nome in nomes_arquivos:
            path_full = os.path.join(path, nome)
            with open(path_full, "w"):
                pass  # Arquivos vazios

        print("Vários arquivos vazios criados com sucesso!")

    except OSError as error:
        print(error)
else:
    print("Directory already exists")