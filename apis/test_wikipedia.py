"""
Python file used to test the methods from the class
Wikipedia using pytest.
"""

from .wikipedia import Wikipedia
import urllib.request

wiki = Wikipedia()

def test_get_api_request(monkeypatch):
    """
    Test function to test the method "get_api_request"
    """
    assert wiki.get_api_request("48.856614", "2.3522219", "+paris") == "Siège de Paris (383)" or "Siège de Paris (1370)"
    assert wiki.get_api_request("48.636063", "-1.511457", "+mont+saint+michel") == "Maison Blanche (Le Mont-Saint-Michel)"

    result = "Maison Blanche (Le Mont-Saint-Michel)"

    def mockreturn(result):
        return result
    monkeypatch.setattr("apis.wikipedia.Wikipedia.get_api_request", result)
    assert wiki.get_api_request == result

def test_return_place_info(monkeypatch):
    """
    Test function to test the method "return_place_info"
    """
    assert wiki.return_place_info("Siège de Paris (1370)") == "Le siège de Paris de 1370, est une tentative de siège par les troupes anglaises de Robert Knolles lors de sa chevauchée de 1370.</br><a href='https://fr.wikipedia.org/wiki/Si%C3%A8ge_de_Paris_(1370)' style='color:white;'>[En savoir plus sur Wikipedia]</a>"
    assert wiki.return_place_info("Maison Blanche (Le Mont-Saint-Michel)") == "La Maison blanche est un monument situé au Mont-Saint-Michel, en France.</br><a href='https://fr.wikipedia.org/wiki/Maison_Blanche_(Le_Mont-Saint-Michel)' style='color:white;'>[En savoir plus sur Wikipedia]</a>"

    result = "La Maison blanche est un monument situé au Mont-Saint-Michel, en France.</br><a href='https://fr.wikipedia.org/wiki/Maison_Blanche_(Le_Mont-Saint-Michel)' style='color:white;'>[En savoir plus sur Wikipedia]</a>"

    def mockreturn():
        return result
    monkeypatch.setattr("apis.wikipedia.Wikipedia.return_place_info", result)
    assert wiki.return_place_info == result