from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QStackedWidget
import random

# Define the application and window
app = QApplication([])
window = QWidget()
window.setWindowTitle('Lottery predictor by Natasha')
window.move(-50, 0)
window.resize(900, 700)

# Create a stacked widget to switch between pages
stacked_widget = QStackedWidget()

# Create the first page (input page)
input_page = QWidget()
input_layout = QVBoxLayout()
title = QLabel('Enter your name:')
name = QLineEdit()
button = QPushButton('Generate Lottery')
input_layout.addWidget(title, alignment=Qt.AlignCenter)
input_layout.addWidget(name, alignment=Qt.AlignCenter)
input_layout.addWidget(button, alignment=Qt.AlignCenter)
input_page.setLayout(input_layout)

# Create the second page (result page)
result_page = QWidget()
result_layout = QVBoxLayout()
result_page.setLayout(result_layout)

# Add pages to the stacked widget
stacked_widget.addWidget(input_page)  # First page (input form)
stacked_widget.addWidget(result_page)  # Second page (result)

# Set the stacked widget as the window's layout
window.setLayout(QVBoxLayout())
window.layout().addWidget(stacked_widget)

# Function to generate lottery and show the result
def generate():
    # Generate a random 5-digit lottery number
    generated_lottery_number = str(random.randint(10000, 99999))  # This will always be 98988 or 98989
    lucky_number = '75697'  # Define a lucky number for comparison

    # Clear the result page
    for i in reversed(range(result_layout.count())):
        widget = result_layout.itemAt(i).widget()
        if widget is not None:
            widget.deleteLater()

    # Display the generated lottery number
    generated_lottery = QLabel(f'Generated Lottery Number: {generated_lottery_number}')
    result_layout.addWidget(generated_lottery, alignment=Qt.AlignCenter)

    # Check if user's name matches the lottery number (as an example condition)
    if name.text() and generated_lottery_number == lucky_number:  # Example condition
        result = QLabel('Congratulations, you win!')
    else:
        result = QLabel('Better luck next time!')

    # Display the result
    result_layout.addWidget(result, alignment=Qt.AlignCenter)

    # Switch to the result page
    stacked_widget.setCurrentWidget(result_page)

# Connect the button click to the generate function
button.clicked.connect(generate)

# Show the window and start the event loop
window.show()
app.exec_()
