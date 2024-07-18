*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary
Library    ../../libraries/helpers.py
Resource    ../../resources/basicRequests.robot
Library    Process

*** Variables ***

*** Test Cases ***
Get_Analytics_LOAD_LEVEL_INFORMATION_DATES
    [Tags]    Get    
    ${params}    Get Endpoint From Dict    event=LOAD_LEVEL_INFORMATION    ana_req={"startTs": "2023-06-01T00:00:00.000Z", "endTs": "2023-06-30T00:00:00.000Z"}
    
    ${resp}    Get Request Analytics   ${params}
    
    ${status_code}=    Convert To String    ${resp.status_code}
    Should Be Equal    ${status_code}    200
    Length Should Be    ${resp.json()["sliceLoadLevelInfos"]}    2


Get_Analytics_LOAD_LEVEL_INFORMATION_DATES_No_Content
    [Tags]    Get
    ${params}    Get Endpoint From Dict     event=LOAD_LEVEL_INFORMATION    ana_req={"startTs": "2023-06-03T00:00:00.000Z", "endTs": "2023-06-15T00:00:00.000Z"}
    
    ${resp}    Get Request Analytics   ${params}    
    
    ${status_code}=    Convert To String    ${resp.status_code}
    Should Be Equal    ${status_code}    204

Get_Analytics_LOAD_LEVEL_INFORMATION_Snssais
    [Tags]    Get    
    ${params}    Get Endpoint From Dict    event=LOAD_LEVEL_INFORMATION    ana_req={"startTs": "2023-06-01T00:00:00.000Z", "endTs": "2023-06-30T00:00:00.000Z"}    event_filter={"snssais":[{"sst":102,"sd":"abcdef"}, "anySlice":true]}
    
    ${resp}    Get Request Analytics   ${params}
    
    ${status_code}=    Convert To String    ${resp.status_code}
    ${status}    Check Result    ${resp}
    Length Should Be    ${resp.json()["sliceLoadLevelInfos"]}    1

Get_Analytics_LOAD_LEVEL_INFORMATION_AnySlice_False
    [Tags]    Get    
    ${params}    Get Endpoint From Dict    event=LOAD_LEVEL_INFORMATION    ana_req={"startTs": "2023-06-01T00:00:00.000Z", "endTs": "2023-06-30T00:00:00.000Z"}    event_filter={"anySlice":false}
    
    Run Keyword And Expect Error    HTTPError: 500*    Get Request Analytics   ${params}


get_Analytics_NSI_LOAD_LEVEL_DATES