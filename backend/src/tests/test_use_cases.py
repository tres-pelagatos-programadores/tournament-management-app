import sys
sys.path.append("..")
import unittest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from controller.tournament_controller import process_create_tournament_request, get_tournament_by_id
from view.tournament_use_cases import find_tournament_by_id, create_tournament
from main import app
from datetime import date

Base = declarative_base()
class Panel(Base):
    __tablename__ = 'Panels'

    id = Column(Integer, primary_key=True)
    category = Column(Integer, nullable=False)
    platform = Column(String, nullable=False)
    region = Column(String, nullable=False)

    def __init__(self, category, platform, region):
        self.category = category
        self.platform = platform
        self.region = region


class Test(unittest.TestCase):

    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()

    def setUp(self):
        Base.metadata.create_all(self.engine)
        self.session.add(Panel(1, 'ion torrent', 'start'))
        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_create_tournament(self):
        with app.app_context():
            requested_data = {
                "name": "nuevo torneo",
                "players": [],
                "start_date": date.today()
            }
            create_tournament(requested_data)
            new_tourney_search = find_tournament_by_id(2)
            self.assertIsNotNone(new_tourney_search)

    def test_find_tournament(self):
        with app.app_context():
            found_tournament = find_tournament_by_id(1)
            not_found_tournament = find_tournament_by_id(3)
            self.assertIsNotNone(found_tournament)
            self.assertIsNone(not_found_tournament)

if __name__ == '__main__':
    unittest.main()
