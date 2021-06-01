
function get_selected(id){
    return document.querySelector('#%'.replace('%', id)).value;
}

function hideTandem(id){
    $('#' + id + ', label[for=' + id + ']').hide();
    $('#' + id ).prop('selectedIndex',0);
    $('#' + id ).val('');
}

function showTandem(id){
    $('#' + id + ', label[for=' + id + ']').show();
}

function show_div(id){
    document.getElementById(id).style.display = '';
}
function hide_div(id){
    document.getElementById(id).style.display = 'none';
    let allElems = `#${id} input, #${id} select, #${id} textarea`;
    let hideElems = document.querySelectorAll(allElems);

    hideElems.forEach((item) => {
        item.value = '';
    })
}


function onBanChanged(value) {

    selected_value = get_selected('id_banOnEntry');
    switch (selected_value){
        case '1':
            showTandem("id_banned_country");
            hideTandem("id_banOnEntryAnother")
            break;
        case '4':
            hideTandem("id_banned_country");
            showTandem("id_banOnEntryAnother")
            break;
        default:
            hideTandem("id_banned_country");
            hideTandem("id_banOnEntryAnother")
    }
}
function onGenderChanged(value) {
    if (get_selected('id_gender') == 3) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_gender_another");
    } else {
        hideTandem("id_gender_another")
    }
}

function onIndividual_countryChanged(value) {
    if (get_selected('id_individual_country') == 4) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_countryAnother");
    } else {
        hideTandem("id_countryAnother")
    }
}

function onCountryFromChanged(value) {
    if (get_selected('id_countryFrom') == 4) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_countryFromAnother");
    } else {
        hideTandem("id_countryFromAnother")
    }
}

function onWayArrivalChanged(value) {
    if (get_selected('id_wayOfArrival') == 5) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_wayOfArrivalAnother");
    } else {
        hideTandem("id_wayOfArrivalAnother")
    }
}

function onOwnershipChanged(value) {
    console.log(get_selected('id_ownership') )
    if (get_selected('id_ownership') == 4) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_is_tnk_member");
        showTandem("id_country_from");
    } else {
        hideTandem("id_is_tnk_member");
        hideTandem("id_country_from");
    }
    onTnkChanged();
}
function showCompanyForm(){
    showTandem("id_company_name")
    showTandem("id_address")
    showTandem("id_ownership")
    showTandem("id_branch")
    showTandem("id_product_type")
    showTandem("id_company_experience")
    showTandem("id_emp_count")
    showTandem("id_additional")
    showTandem("id_country_from")
    showTandem("id_is_tnk_member")
}

function hideCompanyForm(){
    hideTandem("id_company_name")
    hideTandem("id_address")
    hideTandem("id_ownership")
    hideTandem("id_branch")
    hideTandem("id_product_type")
    hideTandem("id_company_experience")
    hideTandem("id_emp_count")
    hideTandem("id_additional")
    hideTandem("id_country_from")
    hideTandem("id_is_tnk_member")
}

function showIntruderIndividualForm(){
    showTandem("id_entrepreneur_name")
    showTandem("id_entrepreneur_age")
    showTandem("id_entrepreneur_gender")
    showTandem("id_entrepreneur_address")
    showTandem("id_entrepreneur_workPurpose")
    showTandem("id_entrepreneur_emp_count")
    showTandem("id_entrepreneur_doAgreement")
    showTandem("id_entrepreneur_payWay")
    showTandem("id_entrepreneur_hireWay")
}

function hideIntruderIndividualForm(){
    hideTandem("id_entrepreneur_name")
    hideTandem("id_entrepreneur_age")
    hideTandem("id_entrepreneur_gender")
    hideTandem("id_entrepreneur_address")
    hideTandem("id_entrepreneur_workPurpose")
    hideTandem("id_entrepreneur_emp_count")
    hideTandem("id_entrepreneur_doAgreement")
    hideTandem("id_entrepreneur_payWay")
    hideTandem("id_entrepreneur_hireWay")
}

function onHireWayChanged(value){
    if (document.getElementById("id_entrepreneur_hireWay_6").checked == true){
        showTandem("id_entrepreneur_hireWayAnother")
    }else{
        hideTandem("id_entrepreneur_hireWayAnother")
    }
}
function onIntruderChanged(value) {

    if (document.getElementById("id_intruder_0").checked == true){
        showTandem("id_government_agency_name")
    }else{
        hideTandem("id_government_agency_name")
    }

    if (document.getElementById("id_intruder_1").checked == true){
        showTandem("id_local_agency_name")
    }else{
        hideTandem("id_local_agency_name")
    }

    if (document.getElementById("id_intruder_2").checked == true){
        showTandem("id_police_agency_name")
    }else{
        hideTandem("id_police_agency_name")
    }

    if (document.getElementById("id_intruder_3").checked == true){
        showTandem("id_control_agency_name")
    }else{
        hideTandem("id_control_agency_name")
    }

    if (document.getElementById("id_intruder_4").checked == true){
        show_div('div_company')
    }else{
        hide_div('div_company')
    }

    if (document.getElementById("id_intruder_5").checked == true){
        show_div('div_entrepreneur')
    }else{
        hide_div('div_entrepreneur')
    }
}


function showIndivualForm(){
    showTandem("id_name");
    showTandem("id_gender");
    showTandem("id_contacts");
    showTandem("id_education");
    showTandem("id_country");
    showTandem("id_city_name");
    showTandem("id_countryFrom");
    showTandem("id_city_name_from");
    showTandem("id_wayOfArrival");
    showTandem("id_wayOfFindingWork");
    showTandem("id_hasRegistration");
    showTandem("id_tradeUnionMembership");
    showTandem("id_experience");
    showTandem("id_hasAgreement");
    showTandem("id_agreementLang");
    showTandem("id_understoodTheContents");
    showTandem("id_workBookStatus");
    showTandem("id_workingDayDuration");
    showTandem("id_hasOverResponsibilities");
    showTandem("id_wayOfGettingSalary");
}

function hideIndivualForm(){
    hideTandem("id_name");
    hideTandem("id_gender");
    hideTandem("id_contacts");
    hideTandem("id_education");
    hideTandem("id_country");
    hideTandem("id_city_name");
    hideTandem("id_countryFrom");
    hideTandem("id_city_name_from");
    hideTandem("id_wayOfArrival");
    hideTandem("id_wayOfFindingWork");
    hideTandem("id_hasRegistration");
    hideTandem("id_tradeUnionMembership");
    hideTandem("id_experience");
    hideTandem("id_hasAgreement");
    hideTandem("id_agreementLang");
    hideTandem("id_understoodTheContents");
    hideTandem("id_workBookStatus");
    hideTandem("id_workingDayDuration");
    hideTandem("id_hasOverResponsibilities");
    hideTandem("id_wayOfGettingSalary");
}

function hideGroupForm(){
    hideTandem("id_amount")
    hideTandem("id_groupType")
    hideTandem("id_workDescription")
    hideTandem("id_membership")
}

function showGroupForm(){
    showTandem("id_amount")
    showTandem("id_groupType")
    showTandem("id_workDescription")
    showTandem("id_membership")
}

function onVictimChanged(value) {

    switch (get_selected('id_victim')) {
        case '1':
            show_div('div_individual')
            hide_div('div_group')
            break;
        case '2':
            hide_div('div_individual')
            show_div('div_group')
            break;
        default:
            hide_div('div_individual')
            hide_div('div_group')
            break

    }
}

function onAgreementChanged(value) {

    switch (get_selected('id_hasAgreement')){
        case 'YES':
           showTandem("id_agreementDetailYes");
           hideTandem("id_agreementDetailNo");
           break;
        case 'NO':
            hideTandem("id_agreementDetailYes");
            showTandem("id_agreementDetailNo");
            break;
        default:
            hideTandem("id_agreementDetailYes");
            hideTandem("id_agreementDetailNo");
            break;
    }
}
function onEntrepreneurAnonimChanged(value) {
    if (value == 'YES') {
        hideTandem("id_entrepreneur_name")
    } else {
        showTandem("id_entrepreneur_name")
    }
}
function onTnkChanged(value) {
    if (get_selected('id_is_tnk_member') == 'YES') {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_tnk_name")
    } else {
        hideTandem("id_tnk_name")
    }
}

function onChangesInSalaryChanged(value) {
    if (get_selected('id_changesInSalary') == 5) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_changesInSalary_another")
    } else {
        hideTandem("id_changesInSalary_another")
    }
}
function onViolationTypeChanged(value) {
    if (get_selected('id_violationType') == 7) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_violationType_another")
    } else {
        hideTandem("id_violationType_another")
    }
}
function onVictim_SituationChanged(value) {
    if (get_selected('id_victim_situation') == 4) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_victim_situation_another")
    } else {
        hideTandem("id_victim_situation_another")
    }
}

function onAnonimChanged(value) {
    if (get_selected('id_is_anonim') == 'NO') {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_name")
    } else {
        hideTandem("id_name")
    }
}

function onVictimTradeUnionMembershipChanged(value) {
    if (get_selected('id_tradeUnionMembership') != 1) {
        // document.getElementById("id_source_url").readOnly=true;
        hideTandem("id_tradeUnionSituation")
        hideTandem("id_tradeUnionCount")
    } else {
        showTandem("id_tradeUnionSituation")
        showTandem("id_tradeUnionCount")
    }
}
function onPersonGroupUnionMembershipChanged(value) {
    if (value == 2) {
        // document.getElementById("id_source_url").readOnly=true;
        hideTandem("id_tradeUnionSituation")
        hideTandem("id_tradeUnionCount")
    } else {
        showTandem("id_tradeUnionSituation")
        showTandem("id_tradeUnionCount")
    }
}

function onTradeUnionSituationChanged(value) {
    if (get_selected('id_tradeUnionSituation') == 4) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_tradeUnionSituation_another")
    } else {
        hideTandem("id_tradeUnionSituation_another")
    }
}
function onRights_StateChanged(value) {
    if (get_selected('id_rights_state') == 4) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_rights_state_another")
    } else {
        hideTandem("id_rights_state_another")
    }
}
function onWayFindingChanged(value) {
    if (get_selected('id_wayOfFindingWork') == 8) {
        // document.getElementById("id_source_url").readOnly=true;
        showTandem("id_wayOfFindingWorkAnother")
    } else {
        hideTandem("id_wayOfFindingWorkAnother")
    }
}



function onSourceChanged(value) {
    if (document.getElementById("id_source_1").checked == true){
        show_div("div_media")
    } else {
        hide_div("div_media")
    }
}

function onRightChanged(value) {
    if (document.getElementById("id_violated_right_13").checked == true){
        showTandem("id_violatedRightAnother");
    } else {
        hideTandem("id_violatedRightAnother")
    }
}

onSourceChanged()
onVictimChanged()
// hide_div('div_company')
// hide_div('div_entrepreneur')
onIntruderChanged()
onRights_StateChanged()
onVictim_SituationChanged()
onViolationTypeChanged()
onChangesInSalaryChanged()
onBanChanged()
onGenderChanged()
onIndividual_countryChanged()
onCountryFromChanged()
onWayArrivalChanged()
onVictimTradeUnionMembershipChanged()
onAgreementChanged()
onWayFindingChanged()
onAnonimChanged()
onRightChanged()
onOwnershipChanged()
onTradeUnionSituationChanged()
// hideTandem("id_banOnEntryAnother")
// hideTandem("id_source_url")
// hideTandem("id_source_content")
//hideTandem("id_violatedRightAnother")
// hideTandem("id_gender_another")
// hideTandem("id_countryAnother")
// hideTandem("id_countryFromAnother")
// hideTandem("id_wayOfArrivalAnother")
// hideTandem("id_wayOfFindingWorkAnother")
// hideTandem("id_agreementDetailYes")
// hideTandem("id_agreementDetailNo")
//hideTandem("id_tnk_name")

// hideTandem("id_government_agency_name")
// hideTandem("id_police_agency_name")
// hideTandem("id_local_agency_name")
// hideTandem("id_control_agency_name")
//hideTandem("id_entrepreneur_hireWayAnother")
// hideTandem("id_violationType_another")
// hideTandem("id_changesInSalary_another")
// hideTandem("id_tradeUnionSituation_another")
// hideTandem("id_victim_situation_another")
//hideCompanyForm()
// hideIndivualForm()
// hideGroupForm()
//hideIntruderIndividualForm()
