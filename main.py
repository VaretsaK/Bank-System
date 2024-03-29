from abc import ABC, abstractmethod


class AbstractCustomer(ABC):
    """
    An abstract base class to define the interface for a customer.
    """

    @abstractmethod
    def get_info(self) -> str:
        """
        Abstract method to get customer's information.
        Returns:
            str: Information about the customer.
        """
        ...

    @abstractmethod
    def email(self) -> str:
        """
        Abstract method to get the customer's email address.
        Returns:
            str: The email address of the customer.
        """
        ...


class AbstractBankAccount(ABC):
    """
    An abstract base class to define the interface for a bank account.
    """

    @abstractmethod
    def top_up(self, value: int) -> str:
        """
        Abstract method to top up the bank account.
        Args:
            value (int): The amount to add to the account balance.
        Returns:
            str: Confirmation message of the top_up.
        """
        ...

    @abstractmethod
    def withdraw(self, value: int) -> str:
        """
        Abstract method to withdraw from the bank account.
        Args:
            value (int): The amount to withdraw from the account balance.
        Returns:
            str: Confirmation message of the withdrawal.
        """
        ...

    @abstractmethod
    def get_account_number(self) -> int:
        """
        Abstract method to get the account number.
        Returns:
            int: The account number.
        """
        ...


class Customer(AbstractCustomer):
    """
    Concrete implementation of AbstractCustomer. Represents a customer of the bank.
    """

    __customer_counter = 0

    def __init__(self, name: str, email: str) -> None:
        """
        Initializes a new Customer instance.
        Args:
            name (str): The name of the customer.
            email (str): The email address of the customer.
        """

        Customer.__customer_counter += 1

        self.__name = name
        self.__email = email
        self.__customer_id = Customer.__customer_counter

    def get_info(self) -> str:
        """
        Get information about the customer.
        Returns:
            str: A string containing the customer's name, email, and customer ID.
        """
        return f"Customer: {self.__name} \nEmail: {self.__email} \nCustomer ID: {self.__customer_id}"

    @property
    def email(self) -> str:
        """
        Property to get the email of the customer.
        Returns:
            str: The email of the customer.
        """
        return self.__email

    @email.setter
    def email(self, new_email: str) -> None:
        """
        Setter to update the customer's email.
        Args:
            new_email (str): The new email address for the customer.
        """
        self.__email = new_email


class BankAccount(AbstractBankAccount):
    """
    Concrete implementation of AbstractBankAccount. Represents a bank account.
    """

    __account_counter = 0

    def __init__(self, owner: Customer) -> None:
        """
        Initializes a new BankAccount instance.
        Args:
            owner (Customer): The owner of the bank account.
        """

        BankAccount.__account_counter += 1

        self.owner = owner
        self.__balance = 0
        self.__account_number = BankAccount.__account_counter
        self.__account_initiation = True

    def top_up(self, value: int) -> str:
        if value <= 0:
            raise ValueError("Top ups should be positive amount.")
        self.__balance += value
        self.__account_initiation = False
        return f"You have topped up {value} USD. Current balance: {self.__balance} USD"

    def withdraw(self, value: int) -> str:
        if self.__balance < value:
            raise ValueError("Insufficient balance.")
        self.__balance -= value
        return f"You have withdrawn {value} USD. Remaining balance: {self.__balance} USD"

    def get_account_number(self) -> str:
        return f"Account number: {self.__account_number}"

    def get_account_owner_info(self) -> str:
        return self.owner.get_info()

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, value: int):
        if value <= 0:
            raise ValueError("Balance should be above 0.")
        if self.__account_initiation:
            self.__balance = value
            self.__account_initiation = False


def main() -> None:
    """
    Main function to demonstrate the usage of the Customer and BankAccount classes.
    """
    customer1 = Customer("Davide Blane", "dave@mail.com")
    customer3 = Customer("Mark", "mark@mail.ua")
    cust1_account = BankAccount(customer1)
    cust3_account = BankAccount(customer3)
    print(cust1_account.get_account_owner_info())
    print(cust3_account.get_account_number())
    print(cust3_account.get_account_owner_info())
    cust3_account.balance = 222
    print(cust3_account.balance)
    cust3_account.balance = 2202
    print(cust3_account.balance)


if __name__ == "__main__":
    main()
