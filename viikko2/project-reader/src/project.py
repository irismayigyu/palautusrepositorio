class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license= license
        self.authors= authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.license or '-'}"
            f"\nAuthors: \n{self.authors or '-'}"
            f"\nDependencies: \n{self.dependencies}"
            f"\nDevelopment dependencies: \n{self.dev_dependencies}"
        )
