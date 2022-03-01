class Patient:

    def __init__(self, PatientID, name, address, phone, veteran_status):
        self.__PatientID = PatientID
        self.__name =  name
        self.__address = address
        self.__PhoneNumber = phone
        self.__veteranstatus = veteran_status

    def get_PatientID(self):
        return self.__PatientID

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__PhoneNumber

    def get_veteran_status(self):
        return self.__veteranstatus