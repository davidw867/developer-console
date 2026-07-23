from abc import abstractmethod
from pathlib import Path
from  ..core.models.git.repository import Repository
from ..base.provider import Provider


class GitProvider(Provider):
    """Contract for local Git operations."""

    @abstractmethod
    def clone_repository(self, url: str, destination: Path) -> None:
        """Clone a repository into the destination directory."""

    @abstractmethod
    def get_status(self, repository_path: Path) -> str:
        """Return the repository's current Git status."""

    @abstractmethod
    def pull(self, repository_path: Path) -> None:
        """Pull changes from the configured remote."""

    @abstractmethod
    def push(self, repository_path: Path) -> None:
        """Push committed changes to the configured remote."""

    @abstractmethod
    def commit(self, repository_path: Path, message: str) -> None:
        """Commit staged changes using the supplied message."""

    @abstractmethod
    def list_branches(self, repository_path: Path) -> tuple[str, ...]:
        """Return the repository's available branch names."""

    @abstractmethod
    def checkout(self, repository_path: Path, message: str) -> str
        """ 
