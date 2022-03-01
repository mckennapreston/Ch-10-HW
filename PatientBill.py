from functools import total_ordering
import PatientClass as a
import ProcedureClass as b

def main():

    MyPatient = a.Patient(1, "Matt Jones", "123 Main St. Waco, TX 76706", "254-555-7415", "TRUE")

    MyProcedure1 = b.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
    MyProcedure2 = b.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    MyProcedure3 = b.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)

    TotalCharges = 0

    print('*** Patient Bill ***')
    print('Name: ', MyPatient.get_name())
    print('Address: ', MyPatient.get_address())
    print('Phone: ', MyPatient.get_phone())
    print()

    print('Procedure: ', MyProcedure1.get_ProcedureName())
    print('Date: ', MyProcedure1.get_ProcedureDate())
    print('Practitioner: ', MyProcedure1.get_practitioner())
    print('Charge: $', format(MyProcedure1.get_charge(), '.2f'))
    print()

    print('Procedure: ', MyProcedure2.get_ProcedureName())
    print('Date: ', MyProcedure2.get_ProcedureDate())
    print('Practitioner: ', MyProcedure2.get_practitioner())
    print('Charge: $', format(MyProcedure2.get_charge(), '.2f'))
    print()

    if MyPatient.get_PatientID() == MyProcedure1.get_PatientID():
        TotalCharges += MyProcedure1.get_charge()
    
    if MyPatient.get_PatientID() == MyProcedure2.get_PatientID():
        TotalCharges += MyProcedure2.get_charge()

    if MyPatient.get_PatientID() == MyProcedure3.get_PatientID():
        TotalCharges += MyProcedure3.get_charge()

    if MyPatient.get_veteran_status() == "TRUE":
        TotalCharges *= .60

    print()
    print("Total Charges: $", format(TotalCharges,'.2f'))

main()