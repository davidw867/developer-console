from wrapper.github import GitHubWrapper
from core.enums.github_resource import GitHubResource

# TODO (Future Service Features)
# - Authentication caching
# - Current user information
# - Repository cache
# - Retry logic
# - Rate limit handling
# - Logging
# - Telemetry
# - Permission checks


class GitHubService:
      """
         Provides business logic for GitHub operations.

         The service layer coordinates
         validation, authentication, caching, 
         and wrapper calls.
      """

    @staticmethod
    def is_authenticated():
        """Checks if the current github user is authenticated"""

        return GitHubWrapper.is_authenticated()

    @staticmethod
    def login():
        """Logs the user into githib."""

        return GitHubWrapper.login()

    @staticmethod
    def create_repository(repo_name: str, is_private: bool):
        """Creates a repository"""

        return GitHubWrapper.create_repository(repo_name, is_private)

    @staticmethod
    def delete_repository(repo_name: str, confirmed_delete: bool):
        """
           Confirms that the user wants to delete their
           repository. allows for a single repository to
           be deleted at a time
        """

        if not isinstance(confirmed_delete, bool):
          raise TypeError("confirm_delete must be a bool.")

        if not confirmed_delete:
          return "Deletion was cancelled."

        return GitHubWrapper.delete_repository(repo_name)

    @staticmethod
    def query(gh_resource: GitHubResource, 
              resource_id: str | None = None):
        """
           Pulls a list of github resources.
        """

        return GitHubWrapper.query(gh_resource, resource_id)

    @staticmethod
    def clone_repository(repo_name: str, owner_name: str):
        """
           Clones a single repository.
        """

        return GitHubWrapper.clone_repository(repo_name, owner_name)
