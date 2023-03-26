from diagrams import Diagram

from diagrams.azure.general import Helpsupport
from diagrams.azure.compute import AppServices
from diagrams.azure.database import SQL

from pathlib import Path
diagrams_folder = Path.cwd() / 'diagrams'
diagrams_folder.mkdir(parents=True, exist_ok=True)

azure_diagram =  diagrams_folder / 'azure_web_service'

with Diagram(str(azure_diagram), show=False):
    Helpsupport("HelpDesk") >> AppServices("web portal") >> SQL("userdb")