class Procedure:

    def __init__(self, ProcedureName, ProcedureDate, practitioner, charge, PatientID):
        self.__procedurename = ProcedureName
        self.__proceduredate = ProcedureDate
        self.__practitioner = practitioner
        self.__charges = charge
        self.__ID = PatientID

    def get_ProcedureName(self):
        return self.__procedurename

    def get_ProcedureDate(self):
        return self.__proceduredate
    
    def get_practitioner(self):
        return self.__practitioner
    
    def get_charge(self):
        return self.__charges

    def get_PatientID(self):
        return self.__ID