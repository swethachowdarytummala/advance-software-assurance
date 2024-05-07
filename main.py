class Organ:
    def __init__(self, name, donor=None, recipient=None):
        self.name = name
        self.donor = donor
        self.recipient = recipient

    def assign_donor(self, donor):
        self.donor = donor

    def assign_recipient(self, recipient):
        self.recipient = recipient

    def __str__(self):
        return f"Organ: {self.name}, Donor: {self.donor}, Recipient: {self.recipient}"

class OrganManagementSystem:
    def __init__(self):
        self.organ_inventory = {}

    def add_organ(self, name):
        if name not in self.organ_inventory:
            self.organ_inventory[name] = Organ(name)
            return True
        return False

    def remove_organ(self, name):
        if name in self.organ_inventory:
            del self.organ_inventory[name]
            return True
        return False

    def assign_donor(self, organ_name, donor):
        if organ_name in self.organ_inventory:
            self.organ_inventory[organ_name].assign_donor(donor)
            return True
        return False

    def assign_recipient(self, organ_name, recipient):
        if organ_name in self.organ_inventory:
            self.organ_inventory[organ_name].assign_recipient(recipient)
            return True
        return False

    def list_organs(self):
        return [str(organ) for organ in self.organ_inventory.values()]

    def search_organ(self, organ_name):
        if organ_name in self.organ_inventory:
            return str(self.organ_inventory[organ_name])
        return f"Organ '{organ_name}' not found."

    def check_compatibility(self, organ_name):
        if organ_name in self.organ_inventory:
            organ = self.organ_inventory[organ_name]
            return organ.donor == organ.recipient
        return False

    def list_donors(self):
        donors = {}
        for organ in self.organ_inventory.values():
            if organ.donor:
                if organ.donor in donors:
                    donors[organ.donor].append(organ.name)
                else:
                    donors[organ.donor] = [organ.name]
        return donors

    def list_recipients(self):
        recipients = {}
        for organ in self.organ_inventory.values():
            if organ.recipient:
                if organ.recipient in recipients:
                    recipients[organ.recipient].append(organ.name)
                else:
                    recipients[organ.recipient] = [organ.name]
        return recipients

# Example usage:
if __name__ == "__main__":
    organ_system = OrganManagementSystem()
    organ_system.add_organ("Heart")
    organ_system.add_organ("Kidney")
    organ_system.assign_donor("Heart", "John")
    organ_system.assign_recipient("Heart", "Alice")
    print(organ_system.list_organs())
    print(organ_system.search_organ("Heart"))
    print(organ_system.check_compatibility("Heart"))
    print(organ_system.list_donors())
    print(organ_system.list_recipients())

