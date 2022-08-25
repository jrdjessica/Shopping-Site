"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return (
            f"<Customer: {self.first_name}, {self.last_name}, {self.email}, {self.password}>"
        )


def read_customer_form_file(filepath):
    """Read customer type data and populate dictionary of customers.

    Dictionary will be {email: Customer(...), email: Customer(...)}
    """

    customer_data = {}

    with open(filepath) as file:
        line = file.rstrip()
        line = line.split('|')
        f_name = line[0]
        l_name = line[1]
        email = line[2]
        password = line[3]

        customer_data['email'] = Customer(f_name, l_name, email, password)

    return customer_data


def get_by_email(email):
    return customer_data[email]


customer_data = read_customer_form_file('customers.txt')
