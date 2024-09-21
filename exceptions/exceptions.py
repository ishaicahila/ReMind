
class baseException(Exception):
    TERMINATE: bool
    ERROR_STR : str

class json_decoding_error(baseException):
    TERMINATE = False
    ERROR_STR = "something went wrong while decoding the response from the engine to json"

class date_parsing_error(baseException):
    TERMINATE = False
    ERROR_STR = "something went wrong while parsing the date and time to datetime format"

class failiure_while_inserting_to_db(baseException):
    TERMINATE = False
    ERROR_STR = "something went wrong while trying to insert the remiinder to the database"
