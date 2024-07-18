*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary
Library    ../../libraries/Events_Subscription/bodyRequestsTransfer.py
Resource    ../../resources/basicRequests.robot
Resource    test_events.robot
Library    Process


*** Variables ***
${base_url}    http://localhost:8080
${bad_id}    123456789012345

*** Test Cases ***
Post_Tranfer
    [Tags]    Posts
    ${body}=    Create Transfer Event Subscription
    ${resp}=    Post Request NWDAF    /nnwdaf-eventssubscription/v1/transfers    json=${body}

    ${id}=    Get Subscription Id    ${resp}
    Set Global Variable    ${id}

    #Validaciones
    ${status_code}=    Convert To String    ${resp.status_code}
    Should Be Equal    ${status_code}    201

    Should Not Be Empty    ${id}

Post_Transfer_TRANSFER
    [Tags]    Posts
    ${body}=    Create Transfer Event Subscription    
    ...    transReqType="TRANSFER"
    ${resp}=    Post Request NWDAF    /nnwdaf-eventssubscription/v1/transfers    json=${body}

    #Validaciones
    ${status_code}=    Convert To String    ${resp.status_code}
    Should Be Equal    ${status_code}    204


Post_Transfer_Not_Mandatory_Attributes
    [Tags]    Posts
    ${body}    Create Bad Transfer Event Subscription 

    Run Keyword And Expect Error    HTTPError: 400*   Post Request NWDAF    //nnwdaf-eventssubscription/v1/transfers    json=${body}



Update_Transfer
    [Tags]    Update
    ${body}=    Create Transfer Event Subscription    
    ...    NF_LOAD_LEVEL
    
    ${resp}=    Update Request NWDAF    /nnwdaf-eventssubscription/v1/transfers/${id}    json=${body}

    ${status_code}=    Convert to String    ${resp.status_code}
    Should Be Equal    ${status_code}    200


Update_Transfer_TRANSFER
    [Tags]    Update
    ${body}=    Create Transfer Event Subscription    
    ...    transReqType="TRANSFER"
    ${resp}=    Update Request NWDAF    /nnwdaf-eventssubscription/v1/transfers/${id}    json=${body}

    #Validaciones
    ${status_code}=    Convert To String    ${resp.status_code}
    Should Be Equal    ${status_code}    204

Update_Transfer_Not_Mandatory_Attributes
    [Tags]    Posts
    ${body}    Create Bad Transfer Event Subscription 

    Run Keyword And Expect Error    HTTPError: 400*   Update Request NWDAF    /nnwdaf-eventssubscription/v1/transfers/${id}    json=${body}

Update_Transfer_Id_Not_Found
    [Tags]    Put
    ${body}=    Create Transfer Event Subscription
    Run Keyword And Expect Error    HTTPError: 404*    Update Request NWDAF    /nnwdaf-eventssubscription/v1/transfers/${bad_id}   json=${body}


Delete_Transfer_Id_Not_Found
    [Tags]    Put  
    Run Keyword And Expect Error    HTTPError: 404*    Delete Request NWDAF    /nnwdaf-eventssubscription/v1/transfers/${bad_id}

Delete_Transfer
    [Tags]    Delete
    ${resp}=    Delete Request NWDAF    /nnwdaf-eventssubscription/v1/transfers/${id}

    #Validations
    ${status_code}=    Convert to String    ${resp.status_code}
    Should Be Equal    ${status_code}    204

