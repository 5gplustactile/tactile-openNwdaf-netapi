*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary
Library    ../../libraries/Data_Management/bodyRequestEvents.py
Resource    ../../resources/basicRequests.robot
Library    Process

*** Variables ***
${base_url}    http://localhost:8080
${bad_id}    123456789012345
${LOCATION_EVENT_SUBSCRIPTION}    ^/nnwdaf-datamanagement/v1/subscriptions/[0-9a-zA-Z]+

*** Test Cases ***
Post_Subscription
    [Tags]    Posts
    ${body}=    Create Event Data Subscription Body
    ${resp}=    Post Request NWDAF    /nnwdaf-datamanagement/v1/subscriptions    json=${body}
    
    ${id}=    Get Subscription Id    ${resp}
    Set Global Variable    ${id}
    #Validations
    ${status_code}=    Convert To String    ${resp.status_code}
    Should Be Equal    ${status_code}    201
    
    Should Not Be Empty    ${id}

Post_Subscription_Already_Stored
    [Tags]    Posts
    ${body}=    Create Event Data Subscription Body
    Run Keyword And Expect Error    HTTPError: 400*   Post Request NWDAF    /nnwdaf-datamanagement/v1/subscriptions    json=${body}


Post_Subscription_Not_Mandatory_Attributes
    [Tags]    Posts
    ${body}=    Create Bad Event Data Subscription Body

    Run Keyword And Expect Error    HTTPError: 400*   Post Request NWDAF    /nnwdaf-datamanagement/v1/subscriptions    json=${body}


Update_Subscription
    [Tags]    Put
    ${body}=    Create Event Data Subscription Body    
    ...    http://127.0.0.1/notificationURI2
    ${resp}=    Update Request NWDAF    /nnwdaf-datamanagement/v1/subscriptions/${id}    json=${body}

    ${status_code}=    Convert to String    ${resp.status_code}
    Should Be Equal    ${status_code}    200

Update_Subscription_Id_Not_Found
    [Tags]    Put
    ${body}=    Create Event Data Subscription Body    
    ...    http://127.0.0.1/notificationURI2
    Run Keyword And Expect Error    HTTPError: 404*    Update Request NWDAF    /nnwdaf-datamanagement/v1/subscriptions/${bad_id}   json=${body}


Delete_Subscription_Id_Not_Found
    [Tags]    Put  
    Run Keyword And Expect Error    HTTPError: 404*    Delete Request NWDAF    /nnwdaf-datamanagement/v1/subscriptions/${bad_id}


Delete_Subscription
    [Tags]    Delete
    ${resp}=    Delete Request NWDAF    /nnwdaf-datamanagement/v1/subscriptions/${id}

    #Validations
    ${status_code}=    Convert to String    ${resp.status_code}
    Should Be Equal    ${status_code}    204


    