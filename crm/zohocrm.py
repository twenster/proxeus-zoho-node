import json

# Record
from zcrmsdk.src.com.zoho.crm.api.record import *
from zcrmsdk.src.com.zoho.crm.api import HeaderMap, ParameterMap

"""
Source
    get_record() : https://pydigger.com/pypi/zcrmsdk ## SDK Sample code
    search_record() : https://www.zoho.com/crm/developer/docs/api/v2/search-records.html
"""
class Record(object):

    def __init__(self):
        pass

    @staticmethod
    def get_records():
        #try:
        # Module to request
        module_api_name = "Leads"

        # Fields to be retrieved
        param_instance = ParameterMap()
        param_instance.add(GetRecordsParam.fields, 'Full_Name')
        
        header_instance = HeaderMap()
        #header_instance.add(GetRecordsHeader.if_modified_since, datetime.now())

        # Request the Zoho SDK
        response = RecordOperations().get_records(module_api_name, param_instance, header_instance)

        response_dict = {}

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ResponseWrapper instance is received.
                if isinstance(response_object, ResponseWrapper):
                    # Get the list of obtained Record instances
                    record_list = response_object.get_data()

                    for record in record_list:

                        # Get the ID of each Record
                        print("Record ID: " + str(record.get_id()))
                        response_dict["id"] = str(record.get_id())

                        # Get the createdBy User instance of each Record
                        created_by = record.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Record Created By - Name: " + created_by.get_name())
                            response_dict["Created_By_Name"] = created_by.get_name()

                            # Get the ID of the created_by User
                            print("Record Created By - ID: " + str(created_by.get_id()))
                            response_dict["Created_By_ID"] = str(created_by.get_id())

                            # Get the Email of the created_by User
                            print("Record Created By - Email: " + created_by.get_email())
                            response_dict["Created_By_Email"] = created_by.get_email()

                        # Get the CreatedTime of each Record
                        print("Record CreatedTime: " + str(record.get_created_time()))
                        response_dict["Created_Time"] = str(record.get_created_time())

                        if record.get_modified_time() is not None:
                            # Get the ModifiedTime of each Record
                            print("Record ModifiedTime: " + str(record.get_modified_time()))
                            response_dict["Modified_Time"] = str(record.get_modified_time())

                        # Get the modified_by User instance of each Record
                        modified_by = record.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modified_by User
                            print("Record Modified By - Name: " + modified_by.get_name())
                            response_dict["Modified_By_Name"] = modified_by.get_name()

                            # Get the ID of the modified_by User
                            print("Record Modified By - ID: " + str(modified_by.get_id()))
                            response_dict["Modified_By_ID"] = str(modified_by.get_id())

                            # Get the Email of the modified_by User
                            print("Record Modified By - Email: " + modified_by.get_email())
                            response_dict["Modified_By_Email"] = modified_by.get_email()

                        # Get the list of obtained Tag instance of each Record
                        tags = record.get_tag()

                        if tags is not None:
                            for tag in tags:
                                # Get the Name of each Tag
                                print("Record Tag Name: " + tag.get_name())
                                response_dict["Tag_Name"] = tag.get_name()

                                # Get the Id of each Tag
                                print("Record Tag ID: " + tag.get_id())
                                response_dict["Tag_ID"] = tag.get_id()

                        # To get particular field value
                        #print("Record Field Value: " + str(record.get_key_value('Full_Name')))
                        #response_dict["Full_Name"] = str(record.get_key_value('Full_Name'))

                        print('Record KeyValues: ')

                        for key, value in record.get_key_values().items():
                            print(key + " : " + str(value))
                            response_dict[key] = str(value)

                        return response_dict

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):
                    # Get the Status
                    print("Status: " + response_object.get_status().get_value())

                    # Get the Code
                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())
                return {"error": "No error"}
            else:
                return {"error": "No CRM match"}
        else:
            return {"error": "No response"}
        #except Exception as e:
        #    print(e)

    @staticmethod
    def search_records(request, zcrm_module, zcrm_search_fields):
        #try:
        # Building criteria
        criteria = []
        if ("Email" in zcrm_search_fields) and (zcrm_search_fields["Email"] != ""):
            criteria.append("(Email:contains:"+zcrm_search_fields["Email"]+")")

        if ("Last_Name" in zcrm_search_fields) and (zcrm_search_fields["Last_Name"] != ""):
            criteria.append("(Last_Name:contains:"+zcrm_search_fields["Last_Name"]+")")

        if ("First_Name" in zcrm_search_fields) and (zcrm_search_fields["First_Name"] != ""):
            criteria.append("(First_Name:contains:"+zcrm_search_fields["First_Name"]+")")

        if ("Company" in zcrm_search_fields or "Account_Name" in zcrm_search_fields):

            if ("Company" in zcrm_search_fields) and (zcrm_search_fields["Company"] != ""):
                criteria.append(")Company:contains:"+zcrm_search_fields["Company"]+")")
                
            if ("Account_Name" in zcrm_search_fields) and (zcrm_search_fields["Account_Name"] != ""):
                criteria.append(")Account_Name:contains:"+zcrm_search_fields["Account_Name"]+")")

        criteriaStr = " and ".join(criteria)
        print("Criteria: "+criteriaStr)

        param_instance = ParameterMap()
        param_instance.add(SearchRecordsParam.criteria, criteriaStr)

        
        header_instance = HeaderMap()
        #header_instance.add(GetRecordsHeader.if_modified_since, datetime.now())

        response = RecordOperations().get_records(zcrm_module, param_instance)
        
        response_dict = {}

        if response is not None:
            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ResponseWrapper instance is received.
                if isinstance(response_object, ResponseWrapper):
                    # Get the list of obtained Record instances
                    record_list = response_object.get_data()

                    for record in record_list:
                        for key, value in record.get_key_values().items():
                            print(key + " : " + str(value))
                            response_dict[key] = str(value)

                    return response_dict

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):
                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

                return {"error": "No error"}

            else:
                return {"error": "No CRM match"}

        else:
            return {"error": "No response"}
