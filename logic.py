import csv
from gui import *

#still too lazy to write it out every time
FILE = "votes.csv"

class Logic:
    def __init__(self, ui: Ui_MainWindow) -> None:
        """
        initialize the logic
        :param ui: the ui window
        """
        self.ui = ui
        self.connect_buttons()
    def clear_all(self) -> None:
        """
        clear the id input, results, and hides the results
        occurs after every vote and resets to the default button
        """
        self.ui.enter_id.clear()
        self.ui.results.clear()
        self.ui.john.setChecked(True)
        self.ui.sarah.setChecked(False)
    def connect_buttons(self) -> None:
        """
        connects the buttons
        """
        self.ui.vote_button.clicked.connect(self.submit_vote)
        self.ui.result_button.clicked.connect(self.show_results)

    def has_voted(selfself, voter_id: str) -> bool:
        """
        check if the given id voted
        :param voter_id: id of the voter
        :return: true if voted else false
        """
        try:
            with open(FILE, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == voter_id:
                        return True
        except FileNotFoundError:
            return False
        return False
    def submit_vote(self) -> None:
        """
        submit a vote
        prevents double voting
        """
        voter_id = self.ui.enter_id.text().strip()
        if not voter_id:
            self.ui.results.setText("Please enter an ID")
            return
        if self.has_voted(voter_id):
            self.ui.results.setText("You have already voted")
            return
        if self.ui.john.isChecked():
            candidate = "John"
        else:
            candidate = "Sarah"
        with open(FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([voter_id, candidate])
        self.clear_all()
        self.ui.results.setText("Vote submitted")
    def show_results(self) -> None:
        """
        shows the results
        """
        john_votes = 0
        sarah_votes = 0

        try:
            with open(FILE, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[1] == "John":
                        john_votes += 1
                    elif row[1] == "Sarah":
                        sarah_votes += 1
        except FileNotFoundError:
            self.ui.results.setText("No votes yet")
            return
        self.ui.results.setText(f"John: {john_votes} votes, Sarah: {sarah_votes} votes")