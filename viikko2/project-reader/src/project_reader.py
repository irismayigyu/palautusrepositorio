from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        new=toml.loads(content)
        #print(new)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        name = new.get("tool", {}).get("poetry", {}).get("name", "default")
        description = new.get("tool", {}).get("poetry", {}).get("description", "default")
        license = new.get("tool", {}).get("poetry", {}).get("license", "default")

        authors = new.get("tool", {}).get("poetry", {}).get("authors", [])
        authors = "\n".join(["- "+author for author in authors])

        dependencies1 = new.get("tool", {}).get("poetry", {}).get("dependencies", [])

        print(dependencies1)
        dependencies = "\n".join(["- "+ i for i in dependencies1])
        

        dev_dependencies = new.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", [])
        dev_dependencies = "\n".join(["- "+ i for i in dev_dependencies])

        return Project(f"{name}", f"{description}", f"{license}", f"{authors}", f"{dependencies}", f"{dev_dependencies}")
