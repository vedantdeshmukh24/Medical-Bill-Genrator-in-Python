from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Patient:
    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address

class MedicalService:
    def __init__(self, code, description, cost):
        self.code = code
        self.description = description
        self.cost = cost

class MedicalBill:
    def __init__(self, patient, services):
        self.patient = patient
        self.services = services

    def generate_bill(self, filename):
        total_cost = sum(service.cost for service in self.services)

        # Create PDF
        pdf_filename = filename + ".pdf"
        pdf_canvas = canvas.Canvas(pdf_filename, pagesize=letter)

        # Write to PDF
        pdf_canvas.drawString(100, 800, "Medical Bill")
        pdf_canvas.drawString(100, 780, "Patient Information:")
        pdf_canvas.drawString(120, 760, f"Name: {self.patient.name}")
        pdf_canvas.drawString(120, 740, f"Date of Birth: {self.patient.dob}")
        pdf_canvas.drawString(120, 720, f"Address: {self.patient.address}")
        pdf_canvas.drawString(100, 700, "Services Provided:")
        
        y_position = 680
        for service in self.services:
            pdf_canvas.drawString(120, y_position, f"Code: {service.code}, Description: {service.description}, Cost: {service.cost:.2f}")
            y_position -= 20
        
        pdf_canvas.drawString(100, y_position, f"Total Cost: {total_cost:.2f}")

        # Save PDF
        pdf_canvas.save()
        print(f"Bill generated successfully: {pdf_filename}")

# Function to display menu
def display_menu():
    print("1. Consultation - 150.00")
    print("2. X-ray - 75.00")

# Get patient information from the user
patient_name = input("Enter patient name: ")
patient_dob = input("Enter patient date of birth (YYYY-MM-DD): ")
patient_address = input("Enter patient address: ")

# Create patient object
patient_info = Patient(patient_name, patient_dob, patient_address)

# Create a list of services
bill_services = []

while True:
    display_menu()
    choice = input("Enter the service number (0 to finish): ")

    if choice == "0":
        break
    elif choice == "1":
        bill_services.append(MedicalService("S001", "Consultation", 150.00))
    elif choice == "2":
        bill_services.append(MedicalService("S002", "X-ray", 75.00))
    else:
        print("Invalid choice. Please enter a valid service number.")

# Create a medical bill object
medical_bill = MedicalBill(patient_info, bill_services)

# Generate and print the medical bill
bill_filename = input("Enter the bill filename (without extension): ")
medical_bill.generate_bill(bill_filename)
