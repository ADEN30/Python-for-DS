import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    """
    Génère un identifiant aléatoire de 15 caractères composé de lettres minuscules.
    
    Returns:
        str: Une chaîne aléatoire de 15 lettres minuscules.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))

@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id)

    def __post_init__(self):
        """
        Initialise le champ 'login' après la création de l'instance.
        
        Le login est construit en concaténant le prénom et le nom en minuscules séparés par un point.
        """
        self.login = f"{self.name.lower()}.{self.surname.lower()}"


student = Student(name = "Edward", surname = "agle")
print(student)