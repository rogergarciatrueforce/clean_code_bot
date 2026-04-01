```python
"""Module for data processing and logging."""

from typing import List, Optional

class DataProcessor:
    """Responsible for data calculation and filtering."""

    def __init__(self, threshold: float = 10.0, multiplier: float = 1.15):
        """
        Initializes the DataProcessor.

        Args:
            threshold: The minimum value for data to be processed.
            multiplier: The multiplier applied to processed data.
        """
        self.threshold = threshold
        self.multiplier = multiplier

    def calculate(self, data: List[float]) -> List[float]:
        """
        Calculates and filters the data based on the threshold.

        Args:
            data: The list of numbers to be processed.

        Returns:
            The list of processed numbers.
        """
        return [x * self.multiplier for x in data if x > self.threshold]


class Logger:
    """Responsible for logging user interactions."""

    def log_user_interaction(self, user_id: str) -> None:
        """
        Logs the user interaction to a file.

        Args:
            user_id: The ID of the user.
        """
        with open("log.txt", "a") as f:
            f.write(f"{user_id} processed data\n")
        print(f"Saving data for user: {user_id}")


def process_data(user_id: str, data: List[float]) -> Optional[List[float]]:
    """
    Processes the data and logs the user interaction if valid.

    Args:
        user_id: The ID of the user.
        data: The list of numbers to be processed.

    Returns:
        The list of processed numbers or None if the user ID is empty.
    """
    if not user_id:
        return None

    data_processor = DataProcessor()
    logger = Logger()

    result = data_processor.calculate(data)
    logger.log_user_interaction(user_id)
    return result
```