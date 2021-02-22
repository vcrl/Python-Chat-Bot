"""
Python file used to test the methods from the class
Parser using pytest.
"""

from .parser import Parser

parser = Parser()

def test_parse_input():
    """
    Test function to test the method "parse_input"
    """
    assert parser.parse_input("où est Paris ?")[0] == "paris"
    assert parser.parse_input("Salut GrandPy, dis moi où est Lille ?")[0] == "lille"
    assert parser.parse_input("Bonjour, tu peux me donner l'adresse de OpenClassrooms ?")[0] == "openclassrooms"