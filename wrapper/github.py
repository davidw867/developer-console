from core.commands import run_command
from core.validators.github import GitHubValidator
from core.enums.github_resource import GitHubResource

class GitHubWrapper:
      """
      Wrapper methods for the GitHub CLI.
      """

    @staticmethod
    def _run_gh_command(args):
        """Private Run Github Commands"""
        command = ["gh"]
        command.extend(args)
        return run_command(command)

    @staticmethod
    def is_authenticated():
        """checks if the current github user is authenticated"""
        return _run_gh_command(["auth", "status"])

    @staticmethod
    def login():
        """Logs the user in to GitHub"""
        return _run_gh_command(["auth", "login"])

    @staticmethod
    def create_repository(repo_name, is_private):
        """Creates a repository"""

        GitHubValidator.repository_name(repo_name)
        GitHubValidator.private_flag(is_private)   
        args  = ["repo", "create", repo_name]

        if is_private:
         args.append("--private")
        else:
         args.append("--public")

        return _run_gh_command(args)

     @staticmethod
     def delete_repository(repo_name):
         """Deletes a single repository"""
        
         GitHubValidator.repository_name(repo_name)
         args = ["repo", "delete", repo_name]
    
         return _run_gh_command(args)

     @staticmethod
     def query(gh_resource: GitHubResource,
               resource_id: str | None = None):
         """Pulls a list of GitHub Resources"""
         GitHubValidator.gh_resource(gh_resource)
         match gh_resource:

             case GitHubResource.WORKFLOWS:

                  args = [
                          "workflow",
                          "list",
                          "--json",
                          "name,id,path,state"]

             case GitHubResource.RELEASES:

                  args = [
                          "release",
                          "list",
                          "--json",
                          "name,tagName,isDraft,isLatest,publishedAt,url"]

             case GitHubResource.ISSUES:

                  args = [
                          "issue",
                          "list",
                          "--json",
                          "number,title,state,author,url,createdAt"]

             case GitHubResource.PULL_REQUESTS:

                  args = [
                          "pr",
                          "list",
                          "--json",
                          "number,title,state,author,url,createdAt"]

             case GitHubResource.REPOSITORIES:

                  args = [
                          "repo",
                          "list",
                          "--json",
                          "name,visibility,isPrivate,description,url"]

             case GitHubResource.WORKFLOWRUNS:

                  args = [
                          "run",
                          "list",
                          "--json",
                          "databaseId,workflowName,status,conclusion,event,createdAt,url"]

              case GitHubResource.GISTS:

                   GitHubValidator.gist_id(resource_id)
                   args = [
                           "gist",
                           "view",
                           resource_id,
                           "--json",
                           "id,description,public,createdAt,updatedAt,files,url"]

              case GitHubResource.LABLES:

                   args = [
                           "label",
                           "list",
                           "--json",
                           "name,color,description"]


              case GitHubResource.SECRETS:

                   args = [
                           "secret",
                           "list",
                           "--json",
                           "name,updatedAt,visibility"]


              case GitHubResource.PROJECTS:

                   args = [
                           "project",
                           "list",
                           "--json",
                           "id,title,shortDescription,url"]


              case GitHubResource.ORGANIZATIONS

                   args = [
                           "org",
                           "list",
                           "--json",
                           "login,name,url"]
              case:
                   raise ValueError("enum value outside of bounds")

            return _run_gh_command(args)

     @staticmethod
     def clone_repository(repo_name, owner_name):
          """Clones a single repository"""
          GithubValadator.repo_name(repo_name)
          GithubValidator.owner_name(owner_name)
          args = ["repo", "clone",f"{owner_name0}/{repo_name}"]

          return _run_gh_command(args)
