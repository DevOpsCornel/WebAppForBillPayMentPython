from flatmates_bill.flat import Bill, Flatmate
from flatmates_bill.report import PdfReport

a = input("Hey user, enter the bill amount")
the_bill = Bill(amount=120, period="April 2021")
john = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print("john pays:", john.pays(bill=the_bill, flatmate2=mary))
print("mary pays:", mary.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)
