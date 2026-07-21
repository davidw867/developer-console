import re

class GitHubValidator:
"""
Validation methods for GitHub CLI operations.
"""

    @staticmethod
    def _identifier(value: str):
      """Validate that value
         is a non-empty string."""
      if not isinstance(value, str):
        raise TypeError("value must be a string")

      if not value.strip():
        raise ValueError("value can not be empty")

    @staticmethod
    def _workflow_identifier(value: str):
      """Valadate that value is a non-empty string
         contains a file naming 
         convention or is an int"""
      GitHubValidator._identifier(value)
      if value.endswith((".yml", ".yaml")):
        return

      if value.isdigit() and int(value) > 0:
        return

      raise ValueError("workflow must be a positive  integer or a '.yml'/' .yaml' workflow file.")
      
    @staticmethod
    def owner_name(owner_name):
      """validate that owner_name is 
         a non-empty string"""
       GitHubValidator._identifier(owner_name)

    @staticmethod
    def repository_name(repo_name):
      """Validate that repo_name is
         a non-empty string."""
       GitHubValidator._identifier(repo_name)

    @staticmethod
    def private_flag(is_private):
      """Validate that is_private is a boolean."""

       if not isinstance(is_private, bool):
         raise TypeError("is_private must be a bool.") 

    @staticmethod
    def workflow_identifier(workflow_id):
      """validate that  workflow is 
         a not-empty string"""
       GitHubValidator._workflow_identifier(workflow_id)

    @staticmethod
    def gist_id(gist_id):
      """Validate that gist_id
         is a non-empty hexadecimal string."""
       GitHubValidator._identifier(gist_id)

       if not re.fullmatch(r"[0-9a-fA-F]+", gist_id):
         raise ValueError("gist_id must be a hexadecimal string.")
