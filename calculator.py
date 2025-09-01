"""Deshnetar Calculator - Chada Calculator System
Enterprise-level implementation of transportation chadabazi calculation with user input.
"""

import logging
from abc import ABC, abstractmethod
from typing import List

# -----------------------------------------------------------------------------
# Logging Configuration
# -----------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Custom Exceptions
# -----------------------------------------------------------------------------
class FareCalculationError(Exception):
    """Custom exception raised for invalid fare calculations."""
    pass

# -----------------------------------------------------------------------------
# Base Class
# -----------------------------------------------------------------------------
class Transportation(ABC):
    """Abstract base class for all transportation services."""

    def __init__(self, base_fare: float, service_name: str) -> None:
        if base_fare < 0:
            raise FareCalculationError("Base fare cannot be negative.")

        self._base_fare: float = base_fare
        self._service_name: str = service_name

    @property
    def base_fare(self) -> float:
        return self._base_fare

    @property
    def service_name(self) -> str:
        return self._service_name

    @abstractmethod
    def calculate_fare(self, multiplier: float = 1.0, extra_percentage: float = 0.0) -> float:
        """
        Abstract method to calculate fare.

        Args:
            multiplier: Scaling factor for base fare.
            extra_percentage: Extra percentage-based charges.

        Returns:
            float: Final fare.
        """
        pass

    def get_service_info(self) -> str:
        """Return service information string."""
        return f"{self._service_name}, Base Fare: {int(self._base_fare)}"

# -----------------------------------------------------------------------------
# Implementations
# -----------------------------------------------------------------------------
class Bus(Transportation):
    """Bus transportation service."""

    def __init__(self) -> None:
        super().__init__(base_fare=100.0, service_name="City Bus")

    def calculate_fare(self, multiplier: float = 1.0, extra_percentage: float = 0.0) -> float:
        if multiplier < 0 or extra_percentage < 0:
            raise FareCalculationError("Invalid parameters for fare calculation.")

        base = self._base_fare * multiplier
        return base * (1 + extra_percentage / 100)


class Auto(Transportation):
    """Auto rickshaw transportation service."""

    PRIORITY_CHARGE_RATE: float = 0.10
    SINGARA_COKE_COST: float = 15.0

    def __init__(self) -> None:
        super().__init__(base_fare=80.0, service_name="Auto Stand")

    def calculate_fare(self, multiplier: float = 1.0, extra_percentage: float = 0.0) -> float:
        if multiplier < 0 or extra_percentage < 0:
            raise FareCalculationError("Invalid parameters for fare calculation.")

        base = self._base_fare * multiplier * (1 + extra_percentage / 100)
        priority_charge = base * self.PRIORITY_CHARGE_RATE

        return base + priority_charge + self.SINGARA_COKE_COST

    def get_service_info(self) -> str:
        base_info = super().get_service_info()
        return (
            f"{base_info}\nIncludes: {int(self.PRIORITY_CHARGE_RATE*100)}% priority charge"
            f" + singara coke cost ({self.SINGARA_COKE_COST})"
        )

# -----------------------------------------------------------------------------
# Service Layer
# -----------------------------------------------------------------------------
def calculate_all_fares(vehicles: List[Transportation]) -> None:
    """Demonstrate polymorphic fare calculation for all vehicles."""
    logger.info("=== Polymorphic Chada Calculation ===")
    for vehicle in vehicles:
        try:
            fare = vehicle.calculate_fare()
            logger.info("%s Fare: %.2f", vehicle.service_name, fare)
        except FareCalculationError as e:
            logger.error("Error calculating fare for %s: %s", vehicle.service_name, e)

# -----------------------------------------------------------------------------
# Main Execution with User Input
# -----------------------------------------------------------------------------
def main() -> None:
    """Entry point for the Deshnetar Calculator system."""
    logger.info("=== Deshnetar Calculator ===")

    options = {"1": Bus(), "2": Auto()}

    print("Choose transportation:")
    print("1. Bus")
    print("2. Auto")
    choice = input("Enter your choice (1/2): ").strip()

    if choice not in options:
        logger.error("Invalid choice. Exiting.")
        return

    try:
        multiplier = float(input("Enter multiplier (default=1): ") or 1)
        extra_percentage = float(input("Enter extra percentage (default=0): ") or 0)
    except ValueError:
        logger.error("Invalid numeric input. Exiting.")
        return

    vehicle = options[choice]

    try:
        fare = vehicle.calculate_fare(multiplier, extra_percentage)
        print("\n=== Fare Calculation Result ===")
        print(vehicle.get_service_info())
        print(f"Final Fare: {fare:.2f}")
    except FareCalculationError as e:
        logger.error("%s", e)


if __name__ == "__main__":
    main()
