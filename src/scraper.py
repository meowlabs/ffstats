from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self):
        pass

    def get_teams(self):
        url = "https://www.pro-football-reference.com/teams/"
        f = requests.get(url)
        contents = f.text

        soup = BeautifulSoup(contents, "html.parser")

        teams = []
        for link in soup.find(id="teams_active").find_all("a"):
            href = link.get("href")
            if href.startswith("/teams"):
                teams.append({ "url": href, "name": link.text })
        
        return teams
