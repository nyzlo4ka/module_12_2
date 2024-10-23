import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TournamentTest.all_results = {}

    def setUp(self):
        self.run1 = runner_and_tournament.Runner('Усэйн', 10)
        self.run2 = runner_and_tournament.Runner('Андрей', 9)
        self.run3 = runner_and_tournament.Runner('Ник', 3)

    def test_tournament1(self):
        res1 = runner_and_tournament.Tournament(90, self.run1, self.run3)
        TournamentTest.all_results = res1.start()
        self.assertTrue(TournamentTest.all_results[2] == 'Ник')

    def test_tournament2(self):
        res2 = runner_and_tournament.Tournament(90, self.run2, self.run3)
        TournamentTest.all_results = res2.start()
        self.assertTrue(TournamentTest.all_results[2] == 'Ник')

    def test_tournament3(self):
        res3 = runner_and_tournament.Tournament(90, self.run1, self.run2, self.run3)
        TournamentTest.all_results = res3.start()
        self.assertTrue(TournamentTest.all_results[3] == 'Ник')

    def tearDown(self):
        for k, v in TournamentTest.all_results.items():
            print(f'{k}: {v}, ', end='')
        print()

# 1: Усэйн, 2: Ник,
# 1: Андрей, 2: Ник,
# 1: Усэйн, 2: Андрей, 3: Ник,
