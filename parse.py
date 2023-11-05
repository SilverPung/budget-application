import argparse
import sys
class Parser:
    def __init__(self) -> None:
        self.parser=argparse.ArgumentParser()
        self.action_group=self.parser.add_mutually_exclusive_group(required=True)
        self.action_group.add_argument(
            '--add-expense',
            dest='action',
            action='store_const',
            const='add_expense',
            help='Dodawanie wydatku'
        )
        self.action_group.add_argument(
            '--add-income',
            dest='action',
            action='store_const',
            const='add_income',
            help='Dodawanie przychodu'
        )
        self.action_group.add_argument(
            '--delete',
            dest='action',
            action='store_const',
            const='delete',
            help='Usuwanie danych'
        )
        self.action_group.add_argument(
            '--stats',
            dest='action',
            action='store_const',
            const='stats',
            help='statysytki'
        )
        self.action_group.add_argument(
            '--list',
            dest='action',
            action='store_const',
            const='list',
            help='listowanie'
        )
        self.add_group = self.parser.add_argument_group('Add Arguments')
        self.add_group.add_argument(
            '--name',
            type=str,
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )
        self.add_group.add_argument(
            '--category',
            type=str,
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )
        self.add_group.add_argument(
            '--date',
            type=str,
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )
        self.add_group.add_argument(
            '--value',
            type=str,
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )
        self.delete_group = self.parser.add_argument_group('Usuwanie')
        self.delete_group.add_argument(
           '--id',
           type=int,
           required='--delete' in sys.argv 
        )
    def parse_args(self):
        return self.parser.parse_args()
    