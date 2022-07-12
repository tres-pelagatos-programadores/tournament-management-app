from abc import ABC, abstractmethod


class RegisterTournamentCommand:

        def __init__(self, tournament: Tournament):
            self.tournament = tournament
        
        # TODO - Define the torunament object in the domain model


class RegisterTournamentPort(ABC):
    
        @abstractmethod
        def execute(command: RegisterTournamentCommand):
            pass