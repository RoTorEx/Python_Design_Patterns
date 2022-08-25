"""Single Responsibility Principle (SRC or SOC)."""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    """Keeping and deleting records is the main and only responsibility of the journal,
     therefore the principle of sole responsibility is not violated."""

    def save(self, filename):  # !Break SRP with extra methods
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):  # !Break SRP with extra methods
        pass

    def load_from_web(self, uri):  # !Break SRP with extra methods
        pass

    """Let's move the above code into a separate log management class.
     Reorganize the code for separation of concerns."""


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


"""Antipattren is the creation of omnipotent objects that do and can do anything."""

j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r"journal.txt"
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
