from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

from pathlib import Path
diagrams_folder = Path.cwd() / 'diagrams'
diagrams_folder.mkdir(parents=True, exist_ok=True)

aws_diagram =  diagrams_folder / 'aws_web_service'
print(aws_diagram)

with Diagram(str(aws_diagram), show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")

