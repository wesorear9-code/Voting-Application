import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QSplitter,
    QVBoxLayout, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QTableWidget, QTableWidgetItem,
    QPushButton, QHeaderView
)

class VotingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ballot and Vote Tally Application")
        self.setGeometry(100, 100, 1000, 600)

        # 1. Create the main splitter (Horizontal)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # 2. Create the Left Side (Form)
        form_widget = self.create_form_widget()
        splitter.addWidget(form_widget)
        
        # 3. Create the Right Side (Tally)
        tally_widget = self.create_tally_widget()
        splitter.addWidget(tally_widget)

        # Set initial sizes for the split sections (e.g., 1/3 for form, 2/3 for tally)
        splitter.setSizes([300, 700]) 

        # Set the splitter as the central widget
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)
        main_layout.addWidget(splitter)
        self.setCentralWidget(central_widget)

    def create_form_widget(self):
        """Creates the widget for name and ballot information entry."""
        container = QWidget()
        layout = QVBoxLayout(container)
        
        # Add a title
        title = QLabel("<h2>Voter and Ballot Information</h2>")
        layout.addWidget(title)
        
        # Use QFormLayout for the label:input alignment
        form_layout = QFormLayout()
        
        # Voter Info
        self.name_input = QLineEdit()
        form_layout.addRow("Voter Name:", self.name_input)
        
        self.id_input = QLineEdit()
        form_layout.addRow("Voter ID:", self.id_input)
        
        self.candidate_input = QLineEdit()
        form_layout.addRow("Selected Candidate:", self.candidate_input)

        # Add the form layout to the container's main VBox
        layout.addLayout(form_layout)

        # Add a submit button
        self.submit_button = QPushButton("Submit Vote")
        # Connect to your submission logic here: self.submit_button.clicked.connect(self.submit_vote)
        layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.submit)
        # Add a stretch to push form elements to the top
        layout.addStretch(1) 
        
        return container


    def submit(self):
        pass



    def create_tally_widget(self):
        """Creates the widget for the vote breakdown/tally."""
        container = QWidget()
        layout = QVBoxLayout(container)
        
        # Add a title
        title = QLabel("<h2>Vote Breakdown Tally</h2>")
        layout.addWidget(title)

        # Create the QTableWidget for the tally
        self.tally_table = QTableWidget()
        self.tally_table.setColumnCount(2)
        self.tally_table.setHorizontalHeaderLabels(["Candidate/Item", "Total Votes"])

        # Set the table to stretch columns to fill the space
        header = self.tally_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        
        # Example data (you would update this dynamically)
        self.populate_tally_table([
            ("Candidate A", 150),
            ("Candidate B", 120),
            ("Item X - Yes", 400),
            ("Item X - No", 150),
        ])

        layout.addWidget(self.tally_table)
        self.update_button = QPushButton("Update Tally")
        layout.addWidget(self.update_button)
        self.update_button.clicked.connect(self.update)
        
        return container


    def update(self):
        pass

    def populate_tally_table(self, data):
        """Fills the table with vote tally data."""
        self.tally_table.setRowCount(len(data))
        for row, (item, votes) in enumerate(data):
            self.tally_table.setItem(row, 0, QTableWidgetItem(item))
            self.tally_table.setItem(row, 1, QTableWidgetItem(str(votes)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VotingApp()
    window.show()
    sys.exit(app.exec())
