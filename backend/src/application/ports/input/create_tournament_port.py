from abc import ABC, abstractmethod


class CreateTournamentCommand:

        def __init__(self, tournament: Tournament):
            self.tournament = tournament
        
        # TODO - Define the torunament object in the domain model


class RegisterTournamentPort(ABC):

        class CreateTournamentCommand:

            def __init__(self, tournament: Tournament):
                self.tournament = tournament
            
            # TODO - Define the torunament object in the domain model

        @abstractmethod
        def execute(command: CreateTournamentCommand):
            pass