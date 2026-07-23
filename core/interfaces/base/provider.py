from ABC import abstractmethod

class Provider(ABC):
      """
          base provider interface.
         "What responsibility does this provider have?"
      """

      @property
      @abstractmethod
      def name(self) -> str:
          """Human-readable provider name."""

      @property
      @abstractmethod
      def is_available(self) -> bool:
          """Whether this provider is currently usable.""" 
