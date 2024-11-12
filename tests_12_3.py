import unittest
from module_12_2 import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):

        runner = Runner('Ivan')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Masha')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('Igor')
        runner2 = Runner('Yulia')

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.part_1 = Runner('Усэйн', speed=4)
        self.part_2 = Runner('Андрей', speed=10)
        self.part_3 = Runner('Ник', speed=2)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        self.tournament_1 = Tournament(90, self.part_1, self.part_3)
        self.all_results = self.tournament_1.start()
        last_runner_name = self.all_results[
            max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.part_2, self.part_3)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[
            max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):

        self.tournament_3 = Tournament(15, self.part_1, self.part_2, self.part_3)

        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[
            max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results


if __name__ == "__main__":
    unittest.main()
