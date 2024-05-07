import unittest
from main import Organ, OrganManagementSystem

class TestOrganManagementSystem(unittest.TestCase):
    def setUp(self):
        self.organ_system = OrganManagementSystem()

    def test_add_organ(self):
        self.assertTrue(self.organ_system.add_organ("Heart"))
        self.assertIn("Heart", self.organ_system.organ_inventory)

    def test_remove_organ(self):
        self.organ_system.add_organ("Heart")
        self.assertTrue(self.organ_system.remove_organ("Heart"))
        self.assertNotIn("Heart", self.organ_system.organ_inventory)

    def test_assign_donor(self):
        self.organ_system.add_organ("Heart")
        self.assertTrue(self.organ_system.assign_donor("Heart", "John"))
        self.assertEqual(self.organ_system.organ_inventory["Heart"].donor, "John")

    def test_assign_recipient(self):
        self.organ_system.add_organ("Heart")
        self.assertTrue(self.organ_system.assign_recipient("Heart", "Alice"))
        self.assertEqual(self.organ_system.organ_inventory["Heart"].recipient, "Alice")

    def test_list_organs(self):
        self.organ_system.add_organ("Heart")
        self.organ_system.add_organ("Kidney")
        self.organ_system.assign_donor("Heart", "John")
        self.organ_system.assign_recipient("Heart", "Alice")
        expected_output = ['Organ: Heart, Donor: John, Recipient: Alice', 'Organ: Kidney, Donor: None, Recipient: None']
        self.assertEqual(self.organ_system.list_organs(), expected_output)

if __name__ == "__main__":
    unittest.main()

