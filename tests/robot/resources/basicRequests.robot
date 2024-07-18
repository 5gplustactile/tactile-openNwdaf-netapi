*** Settings ***

Library    RequestsLibrary
Library    String
Library    Collections

*** Variables ***
${base_url}    http://localhost:8080

*** Keywords ***

Post Request NWDAF
    [Arguments]    ${endpoint}    ${json}=${None}

    Create Session    apisession    ${base_url}

    ${resp}=    POST On Session    apisession    ${endpoint}    json=${json}

    RETURN    ${resp}

Update Request NWDAF
    [Arguments]    ${endpoint}    ${json}=${None}

    Create Session    apisession    ${base_url}

    ${resp}=    PUT On Session    apisession    ${endpoint}    json=${json}

    RETURN    ${resp}

Delete Request NWDAF
    [Arguments]    ${endpoint}

    Create Session    apisession    ${base_url}

    ${resp}=    Delete On Session    apisession    ${endpoint}

    RETURN    ${resp}

Get Subscription Id
    [Arguments]    ${resp}

    ${event_url}=    Split String    ${resp.headers['Location']}    /
    ${id}=    Get From List    ${event_url}    4
    RETURN    ${id}

Get Request Analytics
    [Arguments]    ${endpoint}

    Create Session    apisession    ${base_url}

    ${resp}=    GET On Session    apisession    ${endpoint}

    RETURN    ${resp}