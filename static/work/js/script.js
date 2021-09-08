function process_dict(dict){
    for (var key in dict){
        if (field_dict[key] == false){
            showTandem(key);
        }else{
            hideTandem(key);
        }
    }
}

function get_selected(id){
    return document.querySelector('#%'.replace('%', id)).value;
}

function hideTandem(id){
    console.log(id, ' :::: ' + $('#' + id ).val());

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

function process_dict(dict){
    for (var key in dict){
        if (dict[key] == false){
            showTandem(key);
        }else{
            hideTandem(key);
        }
    }
}

function process_div(dict){
    for (var key in dict){
        if (dict[key] == false){
            show_div(key);
        }else{
            hide_div(key);
        }
    }
}

function onSourceChanged(value) {
    var checkBox = document.getElementById("id_source_2");
    if (checkBox.checked == true){
        show_source()
    } else {
        hide_source()
    }

    if (document.getElementById("id_source_9").checked){
        showTandem('id_source_another');
    }else {
        hideTandem('id_source_another');
    }

}

function onIntruderChanged(value) {
    if (document.getElementById("id_intruder_5").checked == true){
        showTandem('id_intruderAnother');
    } else {
        hideTandem('id_intruderAnother');
    }


    if (document.getElementById("id_intruder_0").checked == true){
        showTandem('id_government_agency_name');
    } else {
        hideTandem('id_government_agency_name');
    }

    if (document.getElementById("id_intruder_1").checked == true){
        showTandem('id_local_agency_name');
    } else {
        hideTandem('id_local_agency_name');
    }

    if (document.getElementById("id_intruder_2").checked == true){
        showTandem('id_police_agency_name');
    } else {
        hideTandem('id_police_agency_name');
    }

    if (document.getElementById("id_intruder_3").checked == true){
        show_div('idEmployerCompanyDiv');
    } else {
        hide_div('idEmployerCompanyDiv');
    }


}

function ownership(){
    let x = document.getElementById('company_ownership_type');
    if(x.options[4].selected === true){
        document.getElementById("company_country").style.display = "block";
        document.getElementById("company_is_tnk_member").style.display = "block";
    }
    else{
        document.getElementById("company_country").style.display = "none";
        document.getElementById("company_is_tnk_member").style.display = "none";
    }
}

function onTradeUnionCrimeChanged(value){
    if (get_selected('id_tradeUnionCrime') == 3){
        showTandem('id_tradeUnionCrimeAnother');
    }else{
        hideTandem('id_tradeUnionCrimeAnother');
    }
}
function onMeetingsRightChanged(value){
    if (get_selected('id_meetingsRight') == 4){
        showTandem('id_meetingsRightAnother');
    }else{
        hideTandem('id_meetingsRightAnother');
    }
}
function onCreateOrganizationRightChanged(value){
    if (get_selected('id_createOrganizationRight') == 7){
        showTandem('id_createOrganizationRightAnother');
    }else{
        hideTandem('id_createOrganizationRightAnother');
    }
}
function onTradeUnionBuildingsRightChanged(value){
    if (get_selected('id_tradeUnionBuildingsRight') == 3){
        showTandem('id_tradeUnionBuildingsRightAnother');
    }else{
        hideTandem('id_tradeUnionBuildingsRightAnother');
    }
}
function onTradeUnionRightChanged(value){

    field_dict = {
        'id_tradeUnionCrime':true,
        'id_meetingsRight':true,
        'id_tradeUnionBuildingsRight':true,
        'id_tradeUnionRightAnother':true,
    }

    switch (get_selected('id_tradeUnionRight')){
        case '1':
            field_dict['id_tradeUnionCrime'] = false;
            break;
        case '3':
            field_dict['id_meetingsRight'] = false;
            break;
        case '6':
            field_dict['id_tradeUnionBuildingsRight'] = false;
            break;
        case '7':
            field_dict['id_tradeUnionRightAnother'] = false;
            break;
    }

    process_dict(field_dict);
}
function onGroupOfRightsChanged(value = 'start'){

    field_dict = {
        'id_tradeUnionRight': true,
        'id_сonvention87': true,
        'id_сonvention98': true,
        'id_сonvention135': true,
        'id_consultationRight': true,
        'id_principleOfNonDiscrimination': true,
        'id_childLabor': true,
        'id_prohibitionOfForcedLabor': true,
    }

    value === 'start' ? '' : hideRights();
    switch (get_selected('id_groupOfRights')){
        case '1':
            field_dict['id_tradeUnionRight'] = false;
            break;
        case '2':
            field_dict['id_сonvention87'] = false;
            break;
        case '3':
            field_dict['id_сonvention98'] = false;
            break;
        case '4':
            field_dict['id_сonvention135'] = false;
            break;
        case '5':
            field_dict['id_consultationRight'] = false;
            break;
        case '6':
            field_dict['id_principleOfNonDiscrimination'] = false;
            break;
        case '7':
            field_dict['id_childLabor'] = false;
            break;
        case '8':
            field_dict['id_prohibitionOfForcedLabor'] = false;
            break;
    }

    process_dict(field_dict);

}
function onConvention87Changed(value){
    field_dict = {
        'id_createOrganizationRight':true,
        'id_createTradeUnionRight':true,
        'id_electionsRight':true,
        'id_tradeUnionActivityRight':true,
        'id_createStrikeRight':true,
    }
    switch (get_selected('id_сonvention87')){
        case '1':
            field_dict['id_createOrganizationRight'] = false;
            break;
        case '2':
            field_dict['id_createTradeUnionRight'] = false;
            break;
        case '4':
            field_dict['id_electionsRight'] = false;
            break;
        case '5':
            field_dict['id_tradeUnionActivityRight'] = false;
            break;
        case '7':
            field_dict['id_createStrikeRight'] = false;
            break;
    }

    process_dict(field_dict);

}
function onConvention98Changed(value){
    // hideRights();

    field_dict={
        'id_antiTradeUnionDiscrimination':true,
        'id_conversationRight':true
    }
    switch (get_selected('id_сonvention98')){
        case '1':
            field_dict['id_antiTradeUnionDiscrimination'] = false;
            break;
        case '2':
            field_dict['id_conversationRight'] = false;
            break;
    }

    process_dict(field_dict);

}
function onPrincipleOfNonDiscriminationChanged(value){
    // hideRights();
    field_dict={
        'id_discriminatiOnVariousGrounds':true,
        'id_discriminationInVariousAreas':true,
        'id_publicPolicyDiscrimination':true,
    }
    switch (get_selected('id_principleOfNonDiscrimination')){
        case '1':
            field_dict['id_discriminatiOnVariousGrounds'] = false;
            break;
        case '2':
            field_dict['id_discriminationInVariousAreas'] = false;
            break;
        case '3':
            field_dict['id_publicPolicyDiscrimination'] = false;
            break;

    }
    process_dict(field_dict);

}
function onVictimChanged(value){
    // hideRights();

    div_dict={
        'idTradeUnionForm':true,
        'idIndividualFormDiv':true,
        'idPersonGroupFormDiv':true,
    }
    switch (get_selected('id_victim')){
        case '1':
            div_dict['idTradeUnionForm'] = false;
            break;
        case '2':
            div_dict['idIndividualFormDiv'] = false;
            break;
        case '3':
            div_dict['idPersonGroupFormDiv'] = false;
            break;
    }

    process_div(div_dict);

}
function onProhibitionOfForcedLaborChanged(value){
    // hideRights();

    field_dict={
        'id_useOfForcedLabor':true,
        'id_governmentCoercion':true,
        'id_violationsUsingCompulsoryLabor':true,
        'id_failureSystemicMeasures':true,
    }
    switch (value){
        case '1':
            field_dict['id_useOfForcedLabor'] = false;
            break;
        case '2':
            field_dict['id_governmentCoercion'] = false;
            break;
        case '3':
            field_dict['id_violationsUsingCompulsoryLabor'] = false;
            break;
        case '4':
            field_dict['id_failureSystemicMeasures'] = false;
            break;

    }

    process_dict(field_dict);

}
function onCreateTradeUnionRightChanged(value){
    if (get_selected('id_createTradeUnionRight') == 5){
        showTandem('id_createTradeUnionRightAnother');
    }else{
        hideTandem('id_createTradeUnionRightAnother');
    }
}
function onElectionsRightChanged(value){
    if (get_selected('id_electionsRight') == 3){
        showTandem('id_electionsRightAnother');
    }else{
        hideTandem('id_electionsRightAnother');
    }
}
function onTradeUnionActivityRightChanged(value){
    if (get_selected('id_tradeUnionActivityRight') == 4){
        showTandem('id_tradeUnionActivityRightAnother');
    }else{
        hideTandem('id_tradeUnionActivityRightAnother');
    }
}
function onСreateStrikeRightChanged(value){
    if (get_selected('id_createStrikeRight') == 10){
        showTandem('id_createStrikeRightAnother');
    }else{
        hideTandem('id_createStrikeRightAnother');
    }
}
function onAntiTradeUnionDiscriminationChanged(value){
    if (get_selected('id_antiTradeUnionDiscrimination') == 5){
        showTandem('id_antiTradeUnionDiscriminationAnother');
    }else{
        hideTandem('id_antiTradeUnionDiscriminationAnother');
    }
}
function onIndAnonimChanged(value){
    for (i = 0; i < 10; i++) {
        var el = document.getElementById('id_form-'+i+'-is_anonim')
        if (el){
            if (el.value == 'NO'){
                showTandem("id_form-"+i+"-name");
            }else {
                hideTandem("id_form-"+i+"-name");
            }
        }
    }
}
function onIndTradeUnionMemberChanged(value){

}
function onTnkChanged(value){
    switch (get_selected('id_is_tnk_member')){
        case 'YES':
            showTandem('id_tnk_name');
            break;
        case 'NO':
            hideTandem('id_tnk_name');
            break;
    }
}
function onHasAgreementChanged(value){
    // if (get_selected('id_has_agreement') == 'NO'){
    //     hideTandem('id_agreementDetail');
    // }else{
    //     showTandem('id_agreementDetail');
    // }

    for (i = 0; i < 10; i++) {
        var el = document.getElementById('id_form-'+i+'-has_agreement')
        if (el){
            if (el.value == 'YES'){
                showTandem("id_form-"+i+"-agreementDetail");
            }else {
                hideTandem("id_form-"+i+"-agreementDetail");
            }
        }
    }
}
function onDiscriminationInVariousAreasChanged(value){
    if (get_selected('id_discriminationInVariousAreas') == 10){
        showTandem('id_discriminationInVariousAreasAnother');
    }else{
        hideTandem('id_discriminationInVariousAreasAnother');
    }
}
function onConversationRightChanged(value){
    if (get_selected('id_conversationRight') == 8){
        showTandem('id_conversationRightAnother');
    }else{
        hideTandem('id_conversationRightAnother');
    }
}
function onConvention135Changed(value){
    if (get_selected('id_сonvention135') == 4){
        showTandem('id_сonvention135Another');
    }else{
        hideTandem('id_сonvention135Another');
    }
}
function onConsultationRightChanged(value){

    field_dict={
        'id_consultationRightAnother':true,
        'id_convention182':true,
    }
    if (get_selected('id_consultationRight') == 4){
        field_dict['id_consultationRightAnother'] = false;
    }else{
        field_dict['id_convention182'] = false;
    }

    process_dict(field_dict);
}
function onChildLaborChanged(value){

    field_dict={
        'id_сonvention138':true,
        'id_convention182':true,
    }

    switch (get_selected('id_childLabor')) {
        case '1':
            field_dict['id_сonvention138'] = false;
            break;
        case '2':
            field_dict['id_convention182'] = false;
            break;
    }
    process_dict(field_dict);

}
function onGroupTypeChanged(value){
    if (get_selected('id_type') == 4){
        showTandem('id_type_another');
    }else{
        hideTandem('id_type_another');
    }
}
function onGroupMembershipChanged(value){
    if (get_selected('id_membership') == 5){
        showTandem('id_membership_another');
    }else{
        hideTandem('id_membership_another');
    }
}
function onOwnershipChanged(value){

    field_dict={
        'id_country_from':true,
        'id_is_tnk_member':true,
        'id_tnk_name':true,
    }

    if (get_selected('id_ownership') == 3){
        field_dict['id_country_from'] = false;
        field_dict['id_is_tnk_member'] = false;
    }
    process_dict(field_dict);

}
function onRights_stateChanged(value){
    if (get_selected('id_rights_state') == 4){
        showTandem('id_rights_state_another');
    }else{
        hideTandem('id_rights_state_another');
    }
}
function onVictim_situationChanged(value){
    if (get_selected('id_victim_situation') == 4){
        showTandem('id_victim_situation_another');
    }else{
        hideTandem('id_victim_situation_another');
    }
}
function onTradeUnionSituationChanged(value){
    if (get_selected('id_tradeUnionSituation') == 4){
        showTandem('id_tradeUnionSituation_another');
    }else{
        hideTandem('id_tradeUnionSituation_another');
    }
}
function onTradeUnionActivitiesChanged(value){
    if (get_selected('id_trade_union_activities') == 19){
        showTandem('id_trade_union_activities_another');
    }else{
        hideTandem('id_trade_union_activities_another');
    }
}
function hideRights(){
    for (key in fields){
        hideTandem('id_'+fields[key]);
    }
}
function hide_source(){
    hideTandem('id_source_url');
    hideTandem('id_source_content');
}
function show_source(){
    showTandem('id_source_url');
    showTandem('id_source_content');
}

// hide_div('idTradeUnionDiv');
// hideTandem('id_source_another');
// hide_source();

//hideRights()

var fields = ['tradeUnionRight',
    'tradeUnionRightAnother',
    'tradeUnionCrime',
    'tradeUnionCrimeAnother',
    'meetingsRight',
    'meetingsRightAnother',
    'tradeUnionBuildingsRight',
    'tradeUnionBuildingsRightAnother',
    'сonvention87',
    'createOrganizationRight',
    'createOrganizationRightAnother',
    'createTradeUnionRight',
    'createTradeUnionRightAnother',
    'electionsRight',
    'electionsRightAnother',
    'tradeUnionActivityRight',
    'tradeUnionActivityRightAnother',
    'сonvention98',
    'conversationRight',
    'conversationRightAnother',
    'createStrikeRight',
    'createStrikeRightAnother',
    'antiTradeUnionDiscrimination',
    'antiTradeUnionDiscriminationAnother',
    'сonvention135',
    'сonvention135Another',
    'consultationRight',
    'consultationRightAnother',
    'principleOfNonDiscrimination',
    'discriminationInVariousAreas',
    'discriminationInVariousAreasAnother',
    'discriminatiOnVariousGrounds',
    'publicPolicyDiscrimination',
    'childLabor',
    'сonvention138',
    'convention182',
    'prohibitionOfForcedLabor',
    'useOfForcedLabor',
    'governmentCoercion',
    'violationsUsingCompulsoryLabor',
    'failureSystemicMeasures',
]

onIndAnonimChanged();
onTnkChanged();
onGroupOfRightsChanged();
onTradeUnionActivitiesChanged();
onTradeUnionRightChanged();
onConvention87Changed();
onConvention98Changed();
onConsultationRightChanged();
onAntiTradeUnionDiscriminationChanged();
onTradeUnionSituationChanged();
onVictim_situationChanged();
onRights_stateChanged();
onOwnershipChanged();
onGroupMembershipChanged();
onGroupTypeChanged();
onChildLaborChanged();
onConvention135Changed();
onConversationRightChanged();
onDiscriminationInVariousAreasChanged();
onHasAgreementChanged();
onСreateStrikeRightChanged();
onTradeUnionActivityRightChanged();
onElectionsRightChanged();
onCreateTradeUnionRightChanged();
onProhibitionOfForcedLaborChanged();
onVictimChanged();
onPrincipleOfNonDiscriminationChanged();
onTradeUnionBuildingsRightChanged();
onCreateOrganizationRightChanged();
onMeetingsRightChanged();
onTradeUnionCrimeChanged();
onIntruderChanged();
onSourceChanged();



// hide_div('idTradeUnionForm');
// hide_div('idIndividualFormDiv');
// hide_div('idPersonGroupFormDiv');
// hideTandem('id_name');
// hideTandem('id_agreementDetail');
// hideTandem('id_type_another');
// hideTandem('id_membership_another');
// hideTandem('id_intruderAnother');
// hideTandem('id_country_from');
// hideTandem('id_is_tnk_member');
// hideTandem('id_tnk_name');
// hideTandem('id_control_agency_name');
// hideTandem('id_intruderAnother');
// hideTandem('id_government_agency_name');
// hideTandem('id_local_agency_name');
// hideTandem('id_police_agency_name');
// hide_div('idTradeUnionDiv');
// hide_div('idEmployerCompanyDiv');
// hideTandem('id_rights_state_another');
// hideTandem('id_victim_situation_another');
// hideTandem('id_tradeUnionSituation_another');