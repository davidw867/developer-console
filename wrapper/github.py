from core.commands import run_command
from core.validators.github import GitHubValidator

class GitHubWrapper:
    """
    Wrapper methods for the GitHub CLI.
    """

    def _run_gh_command(args):
        command = ["gh"]
        command.extend(args)
        return run_command(command)

    def is_authenticated():
        return _run_gh_command(["auth", "status"])

    def login():
        return _run_gh_command(["auth", "login"])

    @staticmethod
    def create_repository(repo_name, is_private):
        """creates a repository"""

        GitHubValidator.repository_name(repo_name)
        GitHubValidator.private_flag(is_private)   
        args  = ["repo", "create", repo_name]

        if is_private:
         args.append("--private")
        else:
         args.append("--public")

        return _run_gh_command(arg)

     @staticmethod
     def delete_repository(repo_name):
         """Deletes a single repository"""
        
         GitHubValidator.repository_name(repo_name)
         args = ["repo", "delete", repo_name]
    
         return _run_gh_command(args)

     def query(gh_resource: GitHubResource,
               resource_id: str | None = None):

         match gh_resource:

             case GitHubResource.WORKFLOW:

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

             case GitHubResource.PULLREQUESTS:

                  args = [
                          "pr",
                          "list",
                          "--json",
                          "number,title,state,author,url,createdAt"]

             case GitHubResource.REPOSITORY:

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


     def clone_repository(repo_name, owner):
   
          args = ["repo", "clone",f"{owner}/{repo_name}"]
    
          return _run_gh_command(args)


