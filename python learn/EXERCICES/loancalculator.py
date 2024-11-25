import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QWidget, QGraphicsColorizeEffect, QMessageBox, QHeaderView
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loan Calculator")
        self.setGeometry(100, 100, 1200, 800)
        self.init_ui()
        self.show()

    def init_ui(self):
        main_layout = QVBoxLayout()

        head = QLabel("LOAN CALCULATOR")
        head.setFont(QFont('Times', 15, QFont.Bold))
        head.setAlignment(Qt.AlignCenter)
        color = QGraphicsColorizeEffect()
        color.setColor(Qt.darkBlue)
        head.setGraphicsEffect(color)
        main_layout.addWidget(head)

        form_layout = QVBoxLayout()
        form_layout.addLayout(self.create_form_row("Loan amount (DH)", self, "amount"))
        form_layout.addLayout(self.create_form_row("Loan term (months)", self, "term"))
        form_layout.addLayout(self.create_form_row("Loan interest", self, "rate"))
        form_layout.addLayout(self.create_form_row("New Loan Interest", self, "rate2"))
        form_layout.addLayout(self.create_form_row("Month to New Interest", self, "term2"))

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.create_button("Calculate payment", self.calculate_action))
        button_layout.addWidget(self.create_button("Reset", self.reset_action))
        form_layout.addLayout(button_layout)

        payment_layout = QHBoxLayout()
        payment_layout.addWidget(self.wrap_layout_in_widget(self.create_label("Monthly payment:", self, "m_payment")))
        payment_layout.addWidget(self.wrap_layout_in_widget(self.create_label("Yearly payment:", self, "y_payment")))
        payment_layout.addWidget(self.wrap_layout_in_widget(self.create_label("Total payment:", self, "t_payment")))  # New line
        form_layout.addLayout(payment_layout)

        main_layout.addLayout(form_layout)

        self.amortization_table = self.create_table()
        self.amortization_table2 = self.create_table()
        main_layout.addWidget(self.amortization_table)
        main_layout.addWidget(self.amortization_table2)

        graph_button_layout = QHBoxLayout()
        graph_button_layout.addWidget(self.create_button("Show Amortization Table", self.show_amortization_table))
        graph_button_layout.addWidget(self.create_button("Show New Rate Table", self.show_amortization_table2))
        graph_button_layout.addWidget(self.create_button("Show Graph 1", self.show_graph))
        graph_button_layout.addWidget(self.create_button("Show Graph 2", self.show_graph_with_rate_increase))
        main_layout.addLayout(graph_button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def wrap_layout_in_widget(self, layout):
        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def create_form_row(self, label_text, parent, attr_name):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("border: 2px solid black; background: rgba(70,70,70,35);")
        label.setFont(QFont('Times', 9))
        layout.addWidget(label)

        line_edit = QLineEdit(parent)
        line_edit.setAlignment(Qt.AlignCenter)
        line_edit.setFont(QFont('Times', 9))
        if "term" in attr_name or "amount" in attr_name:
            line_edit.setValidator(QIntValidator())
        setattr(self, attr_name, line_edit)
        layout.addWidget(line_edit)
        return layout

    def create_button(self, text, func):
        button = QPushButton(text)
        button.clicked.connect(func)
        return button

    def create_label(self, text, parent, attr_name):
        layout = QVBoxLayout()
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("border: 2px solid black; background: rgba(70,70,70,35);")
        label.setFont(QFont('Times', 9))
        layout.addWidget(label)

        dynamic_label = QLabel(parent)
        dynamic_label.setAlignment(Qt.AlignCenter)
        dynamic_label.setStyleSheet("border: 3px solid black; background: white;")
        dynamic_label.setFont(QFont('Times', 11))
        setattr(self, attr_name, dynamic_label)
        layout.addWidget(dynamic_label)
        return layout

    def create_table(self):
        table = QTableWidget(self)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Période", "Paiement", "Intérêts", 'Principal', "Solde restant"])
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.hide()
        return table

    def calculate_action(self):
        try:
            loan_interest_rate = float(self.rate.text())
            loan_amount = int(self.amount.text())
            loan_term = int(self.term.text())
            rate_increase = float(self.rate2.text())
            increase_month = int(self.term2.text())

            if loan_interest_rate == 0 or loan_amount == 0 or loan_term == 0:
                raise ValueError

            loan_interest = loan_interest_rate / 100
            monthly_payment = (loan_amount * loan_interest / 12) / (1 - (1 + loan_interest / 12) ** -loan_term)

            self.m_payment.setText(f"{monthly_payment:.2f} DH")
            yearly_payment = monthly_payment * 12
            self.y_payment.setText(f"{yearly_payment:.2f} DH")

            # Calculate total payment
            total_payment = monthly_payment * loan_term
            self.t_payment.setText(f"{total_payment:.2f} DH")  # Display total payment

            self.populate_table(self.amortization_table, loan_amount, loan_term, loan_interest, monthly_payment)
            self.populate_new_rate_table(loan_amount, loan_term, loan_interest, rate_increase, increase_month)
        except ValueError:
            QMessageBox.critical(self, "Alert!", "Please fill all fields with valid values")

    def populate_table(self, table, loan_amount, loan_term, loan_interest, monthly_payment):
        table.setRowCount(loan_term)
        remaining_balance = loan_amount
        for period in range(loan_term):
            interest_payment = remaining_balance * (loan_interest / 12)
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment
            table.setItem(period, 0, QTableWidgetItem(str(period + 1)))
            table.setItem(period, 1, QTableWidgetItem(f"{monthly_payment:.2f}"))
            table.setItem(period, 2, QTableWidgetItem(f"{interest_payment:.2f}"))
            table.setItem(period, 3, QTableWidgetItem(f"{principal_payment:.2f}"))
            table.setItem(period, 4, QTableWidgetItem(f"{remaining_balance:.2f}"))

    def populate_new_rate_table(self, loan_amount, loan_term, loan_interest, rate_increase, increase_month):
        table = self.amortization_table2
        table.setRowCount(loan_term)
        remaining_balance = loan_amount
        monthly_payment = (loan_amount * loan_interest / 12) / (1 - (1 + loan_interest / 12) ** -loan_term)
        new_interest = loan_interest + (rate_increase / 100)

        for period in range(loan_term):
            if period + 1 == increase_month:
                loan_interest = new_interest
                monthly_payment = (remaining_balance * loan_interest / 12) / (1 - (1 + loan_interest / 12) ** -(loan_term - period))

            interest_payment = remaining_balance * (loan_interest / 12)
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment
            table.setItem(period, 0, QTableWidgetItem(str(period + 1)))
            table.setItem(period, 1, QTableWidgetItem(f"{monthly_payment:.2f}"))
            table.setItem(period, 2, QTableWidgetItem(f"{interest_payment:.2f}"))
            table.setItem(period, 3, QTableWidgetItem(f"{principal_payment:.2f}"))
            table.setItem(period, 4, QTableWidgetItem(f"{remaining_balance:.2f}"))

    def reset_action(self):
        self.amount.setText("")
        self.rate.setText("")
        self.term.setText("")
        self.rate2.setText("")
        self.term2.setText("")
        self.m_payment.setText("")
        self.y_payment.setText("")
        self.t_payment.setText("")  # Reset total payment
        self.amortization_table.clearContents()
        self.amortization_table.hide()
        self.amortization_table2.clearContents()
        self.amortization_table2.hide()

    def show_amortization_table(self):
        self.amortization_table.show()

    def show_amortization_table2(self):
        self.amortization_table2.show()

    def show_graph(self):
        try:
            amount = int(self.amount.text())
            rate = float(self.rate.text()) / 100
            term = int(self.term.text())
            monthly_payment = (amount * rate / 12) / (1 - (1 + rate / 12) ** -term)
            balances = []
            remaining_balance = amount
            for _ in range(term):
                interest_payment = remaining_balance * rate / 12
                principal_payment = monthly_payment - interest_payment
                remaining_balance -= principal_payment
                balances.append(remaining_balance)

            plt.plot(balances)
            plt.xlabel('Month')
            plt.ylabel('Remaining Balance (DH)')
            plt.title('Amortization Over Time')
            plt.show()
        except ValueError:
            QMessageBox.critical(self, "Alert!", "Please fill all fields with valid values")

    def show_graph_with_rate_increase(self):
        try:
            amount = int(self.amount.text())
            rate = float(self.rate.text()) / 100
            term = int(self.term.text())
            new_rate = float(self.rate2.text()) / 100
            increase_month = int(self.term2.text())

            monthly_payment = (amount * rate / 12) / (1 - (1 + rate / 12) ** -term)
            balances = []
            remaining_balance = amount

            for month in range(1, term + 1):
                if month == increase_month:
                    rate = new_rate
                    monthly_payment = (remaining_balance * rate / 12) / (1 - (1 + rate / 12) ** -(term - month + 1))

                interest_payment = remaining_balance * rate / 12
                principal_payment = monthly_payment - interest_payment
                remaining_balance -= principal_payment
                balances.append(remaining_balance)

            plt.plot(balances)
            plt.xlabel('Month')
            plt.ylabel('Remaining Balance (DH)')
            plt.title('Amortization with Rate Increase')
            plt.show()
        except ValueError:
            QMessageBox.critical(self, "Alert!", "Please fill all fields with valid values")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
"""
      
print(f"Nom: {self.nom}, Age: {self.age}")
        print("Matières et Notes:")
        for matiere, note in self.matiere_notes.items():
            print(f"- {matiere}: {note}")
"""