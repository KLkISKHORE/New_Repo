if file in list_of_files:
    contents = repo.get_contents(file)
    repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
else:
    repo.create_file(file, "committing files", content, branch="master")
#new_repo = user.create_repo(repository_name)