
##################################################################
# Mocked returns for patched functions that access web resources #
##################################################################


GET_POLICE_STATION_API_MOCK = {
    "displayFieldName": "NAME",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "FACILITYID": "Facility Identifier",
        "NAME": "Name of Facility",
        "OWNER": "Owner Name",
        "OWNTYPE": "Owner Type",
        "SUBTYPEFIELD": "Subtype Field",
        "FEATURECODE": "Feature Code",
        "FULLADDR": "Full Address",
        "AGENCYURL": "Website",
        "OPERDAYS": "Operational Days",
        "OPERHOURS": "Operational Hours",
        "CONTACT": "Contact Name",
        "PHONE": "Phone",
        "EMAIL": "Email"
    },
    "features": [
        {
            "attributes": {
                "OBJECTID": 1,
                "FACILITYID": None,
                "NAME": "Brookline Public Safety HQ",
                "OWNER": "Town of Brookline",
                "OWNTYPE": None,
                "SUBTYPEFIELD": None,
                "FEATURECODE": None,
                "FULLADDR": "350 Washington St, Brookline, MA 02445",
                "AGENCYURL": "http://www.brooklinepolice.com/",
                "OPERDAYS": "Other",
                "OPERHOURS": "Other",
                "CONTACT": None,
                "PHONE": "617-730-2222",
                "EMAIL": None
            },
            "geometry": {
                "x": -71.121409303637222,
                "y": 42.333789044263746
            }
        }
    ]
}

NO_RESULTS_GET_POLICE_STATION_API_MOCK = {
    "displayFieldName": "NAME",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "FACILITYID": "Facility Identifier",
        "NAME": "Name of Facility",
        "OWNER": "Owner Name",
        "OWNTYPE": "Owner Type",
        "SUBTYPEFIELD": "Subtype Field",
        "FEATURECODE": "Feature Code",
        "FULLADDR": "Full Address",
        "AGENCYURL": "Website",
        "OPERDAYS": "Operational Days",
        "OPERHOURS": "Operational Hours",
        "CONTACT": "Contact Name",
        "PHONE": "Phone",
        "EMAIL": "Email"
    },
    "features": []
}


GET_TRASH_PICKUP_API_MOCK = {
    "displayFieldName": "DISTRICTID",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "DISTRICTID": "District ID",
        "NAME": "District Name",
        "AGENCY": "Agency",
        "AGENCYURL": "Website",
        "CONTACT": "Contact Name",
        "PHONE": "Phone",
        "EMAIL": "Email",
        "SUBTYPEFIELD": "Subtype Field",
        "SCHEDULE": "Schedule",
        "DESCRIPT": "Additional Information",
        "MONDAY": "Monday",
        "TUESDAY": "Tuesday",
        "WEDNESDAY": "Wednesday",
        "THURSDAY": "Thursday",
        "FRIDAY": "Friday",
        "SATURDAY": "Saturday",
        "SUNDAY": "Sunday",
        "GlobalID": "GlobalID"
    },
    "features": [
        {
            "attributes": {
                "OBJECTID": 2,
                "DISTRICTID": "1",
                "NAME": "Wednesday Trash",
                "AGENCY": "Town of Brookline",
                "AGENCYURL": "http://ma-brookline.civicplus.com/820/Trash-Recycling-Information",
                "CONTACT": "Brookline Public Works",
                "PHONE": "null",
                "EMAIL": "null",
                "SUBTYPEFIELD": 0,
                "SCHEDULE": "Weekly",
                "DESCRIPT": "http://ma-brookline.civicplus.com/834/Holiday-Schedule-Christmas-Tree-Pick-Up",
                "MONDAY": "No",
                "TUESDAY": "No",
                "WEDNESDAY": "Yes",
                "THURSDAY": "No",
                "FRIDAY": "No",
                "SATURDAY": "No",
                "SUNDAY": "No",
                "GlobalID": "{20538BBF-EB83-4CCD-B1E8-93EF36554413}"
            }
        }
    ]
}

NO_RESPONSE_TRASH_PICKUP_API_MOCK = {
    "displayFieldName": "DISTRICTID",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "DISTRICTID": "District ID",
        "NAME": "District Name",
        "AGENCY": "Agency",
        "AGENCYURL": "Website",
        "CONTACT": "Contact Name",
        "PHONE": "Phone",
        "EMAIL": "Email",
        "SUBTYPEFIELD": "Subtype Field",
        "SCHEDULE": "Schedule",
        "DESCRIPT": "Additional Information",
        "MONDAY": "Monday",
        "TUESDAY": "Tuesday",
        "WEDNESDAY": "Wednesday",
        "THURSDAY": "Thursday",
        "FRIDAY": "Friday",
        "SATURDAY": "Saturday",
        "SUNDAY": "Sunday",
        "GlobalID": "GlobalID"
    },
    "features": []
}