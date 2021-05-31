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
    var checkBox = document.getElementById("id_intruder_5");
    if (checkBox.checked == true){
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
        console.log(x.options[4]);
    }
    else{
        document.getElementById("company_country").style.display = "none";
        document.getElementById("company_is_tnk_member").style.display = "none";
        console.log(x.options[4]);
    }
}

function onTradeUnionCrimeChanged(value){
    if (value == 3){
        showTandem('id_tradeUnionCrimeAnother');
    }else{
        hideTandem('id_tradeUnionCrimeAnother');
    }
}
function onMeetingsRightChanged(value){
    if (value == 4){
        showTandem('id_meetingsRightAnother');
    }else{
        hideTandem('id_meetingsRightAnother');
    }
}
function onCreateOrganizationRightChanged(value){
    if (value == 1){

    }
    if (value == 7){
        showTandem('id_createOrganizationRightAnother');
    }else{
        hideTandem('id_createOrganizationRightAnother');
    }
}
function onTradeUnionBuildingsRightChanged(value){
    if (value == 3){
        showTandem('id_tradeUnionBuildingsRightAnother');
    }else{
        hideTandem('id_tradeUnionBuildingsRightAnother');
    }
}
function onTradeUnionRightChanged(value){

    switch (value){
        case '1':
            showTandem('id_tradeUnionCrime');
            hideTandem('id_tradeUnionRightAnother');
            hideTandem('id_tradeUnionCrimeAnother');
            hideTandem('id_tradeUnionBuildingsRight');
            hideTandem('id_meetingsRight');
            break;
        case '3':
            hideTandem('id_tradeUnionCrime');
            hideTandem('id_tradeUnionRightAnother');
            hideTandem('id_tradeUnionCrimeAnother');
            hideTandem('id_tradeUnionBuildingsRight');
            showTandem('id_meetingsRight');
            break;
        case '7':
            showTandem('id_tradeUnionCrime');
            hideTandem('id_tradeUnionRightAnother');
            hideTandem('id_tradeUnionCrimeAnother');
            hideTandem('id_tradeUnionBuildingsRight');
            hideTandem('id_meetingsRight');
            break;
        case '6':
            hideTandem('id_tradeUnionCrime');
            hideTandem('id_tradeUnionRightAnother');
            hideTandem('id_tradeUnionCrimeAnother');
            showTandem('id_tradeUnionBuildingsRight');
            hideTandem('id_meetingsRight');
            break;
    }
}
function onGroupOfRightsChanged(value){
    hideRights();
    switch (value){
        case '1':
            showTandem('id_tradeUnionRight');
            break;
        case '2':
            showTandem('id_сonvention87');
            break;
        case '3':
            showTandem('id_сonvention98');
            break;
        case '4':
            showTandem('id_сonvention135');
            break;
        case '5':
            showTandem('id_consultationRight');
            break;
        case '6':
            showTandem('id_principleOfNonDiscrimination');
            break;
        case '7':
            showTandem('id_childLabor');
            break;
        case '8':
            showTandem('id_prohibitionOfForcedLabor');
            break;
    }
}
function onConvention87Changed(value){
   // hideRights();
    switch (value){
        case '1':
            showTandem('id_createOrganizationRight');
            hideTandem('id_createTradeUnionRight');
            hideTandem('id_electionsRight');
            hideTandem('id_tradeUnionActivityRight');
            hideTandem('id_createStrikeRight');
            break;
        case '2':
            hideTandem('id_createOrganizationRight');
            showTandem('id_createTradeUnionRight');
            hideTandem('id_electionsRight');
            hideTandem('id_tradeUnionActivityRight');
            hideTandem('id_createStrikeRight');
            break;
        case '4':
            hideTandem('id_createOrganizationRight');
            hideTandem('id_createTradeUnionRight');
            showTandem('id_electionsRight');
            hideTandem('id_tradeUnionActivityRight');
            hideTandem('id_createStrikeRight');
            break;
        case '5':
            hideTandem('id_createOrganizationRight');
            hideTandem('id_createTradeUnionRight');
            hideTandem('id_electionsRight');
            showTandem('id_tradeUnionActivityRight');
            hideTandem('id_createStrikeRight');
            break;
        case '7':
            hideTandem('id_createOrganizationRight');
            hideTandem('id_createTradeUnionRight');
            hideTandem('id_electionsRight');
            hideTandem('id_tradeUnionActivityRight');
            showTandem('id_createStrikeRight');
            break;
    }
}

function onConvention98Changed(value){
   // hideRights();
    switch (value){
        case '1':
            showTandem('id_antiTradeUnionDiscrimination');
            hideTandem('id_conversationRight');
            break;
        case '2':
            showTandem('id_conversationRight');
            hideTandem('id_antiTradeUnionDiscrimination');
            break;

    }
}
function onPrincipleOfNonDiscriminationChanged(value){
   // hideRights();
    switch (value){
        case '1':
            showTandem('id_discriminatiOnVariousGrounds');
            hideTandem('id_discriminationInVariousAreas');
            hideTandem('id_publicPolicyDiscrimination');
            break;
        case '2':
            hideTandem('id_discriminatiOnVariousGrounds');
            showTandem('id_discriminationInVariousAreas');
            hideTandem('id_publicPolicyDiscrimination');
            break;
        case '3':
            hideTandem('id_discriminatiOnVariousGrounds');
            hideTandem('id_discriminationInVariousAreas');
            showTandem('id_publicPolicyDiscrimination');
            break;

    }
}
function onVictimChanged(value){
   // hideRights();
    switch (value){
        case '1':
            showTandem('idTradeUnionForm');
            hide_div('idIndividualFormDiv');
            hide_div('idPersonGroupFormDiv');
            break;
        case '2':
            hide_div('idTradeUnionForm');
            showTandem('idIndividualFormDiv');
            hide_div('idPersonGroupFormDiv');
            break;
        case '3':
            hide_div('idTradeUnionForm');
            hide_div('idIndividualFormDiv');
            showTandem('idPersonGroupFormDiv');
            break;
        default:
             hide_div('idTradeUnionForm');
            hide_div('idIndividualFormDiv');
            hide_div('idPersonGroupFormDiv');
            break;

    }
}
function onProhibitionOfForcedLaborChanged(value){
   // hideRights();
    switch (value){
        case '1':
            showTandem('id_useOfForcedLabor');
            hideTandem('id_governmentCoercion');
            hideTandem('id_violationsUsingCompulsoryLabor');
            hideTandem('id_failureSystemicMeasures');
            break;
        case '2':
            hideTandem('id_useOfForcedLabor');
            showTandem('id_governmentCoercion');
            hideTandem('id_violationsUsingCompulsoryLabor');
            hideTandem('id_failureSystemicMeasures');
            break;
        case '3':
            hideTandem('id_useOfForcedLabor');
            hideTandem('id_governmentCoercion');
            showTandem('id_violationsUsingCompulsoryLabor');
            hideTandem('id_failureSystemicMeasures');
            break;
        case '4':
            hideTandem('id_useOfForcedLabor');
            hideTandem('id_governmentCoercion');
            hideTandem('id_violationsUsingCompulsoryLabor');
            showTandem('id_failureSystemicMeasures');
            break;

    }
}
function onCreateTradeUnionRightChanged(value){
    if (value == 5){
        showTandem('id_createTradeUnionRightAnother');
    }else{
        hideTandem('id_createTradeUnionRightAnother');
    }
}
function onElectionsRightChanged(value){
    if (value == 3){
        showTandem('id_electionsRightAnother');
    }else{
        hideTandem('id_electionsRightAnother');
    }
}
function onTradeUnionActivityRightChanged(value){
    if (value == 4){
        showTandem('id_tradeUnionActivityRightAnother');
    }else{
        hideTandem('id_tradeUnionActivityRightAnother');
    }
}
function onСreateStrikeRightChanged(value){
    if (value == 10){
        showTandem('id_createStrikeRightAnother');
    }else{
        hideTandem('id_createStrikeRightAnother');
    }
}
function onAntiTradeUnionDiscriminationChanged(value){
    if (value == 5){
        showTandem('id_antiTradeUnionDiscriminationAnother');
    }else{
        hideTandem('id_antiTradeUnionDiscriminationAnother');
    }
}
function onIndAnonimChanged(value){
    if (value == 'YES'){
        hideTandem('id_name');
    }else{
        showTandem('id_name');
    }
}
function onTnkChanged(value){
    if (value == 'NO'){
        hideTandem('id_tnk_name');
    }else{
        showTandem('id_tnk_name');
    }
}
function onHasAgreementChanged(value){
    if (value == 'NO'){
        hideTandem('id_agreementDetail');
    }else{
        showTandem('id_agreementDetail');
    }
}
function onDiscriminationInVariousAreasChanged(value){
    if (value == 10){
        showTandem('id_discriminationInVariousAreasAnother');
    }else{
        hideTandem('id_discriminationInVariousAreasAnother');
    }
}
function onConversationRightChanged(value){
    if (value == 8){
        showTandem('id_conversationRightAnother');
    }else{
        hideTandem('id_conversationRightAnother');
    }
}
function onConvention135Changed(value){
    if (value == 4){
        showTandem('id_сonvention135Another');
    }else{
        hideTandem('id_сonvention135Another');
    }
}
function onConsultationRightChanged(value){
    if (value == 4){
        showTandem('id_consultationRightAnother');
        hideTandem('id_convention182');
    }else{
        showTandem('id_convention182');
        hideTandem('id_consultationRightAnother');
    }
}
function onChildLaborChanged(value){
    if (value == 1){
        showTandem('id_сonvention138');
        hideTandem('id_convention182');
    }else{
        showTandem('id_convention182');
        hideTandem('id_сonvention138');
    }
}
function onGroupTypeChanged(value){
    if (value == 4){
        showTandem('id_type_another');
    }else{
        hideTandem('id_type_another');
    }
}
function onGroupMembershipChanged(value){
    if (value == 5){
        showTandem('id_membership_another');
    }else{
        hideTandem('id_membership_another');
    }
}
function onOwnershipChanged(value){
    if (value == 3){
        showTandem('id_country_from');
        showTandem('id_is_tnk_member');
    }else{
        hideTandem('id_country_from');
        hideTandem('id_is_tnk_member');
        hideTandem('id_tnk_name');
    }
}
function onRights_stateChanged(value){
    if (value == 4){
        showTandem('id_rights_state_another');
    }else{
        hideTandem('id_rights_state_another');
    }
}
function onVictim_situationChanged(value){
    if (value == 4){
        showTandem('id_victim_situation_another');
    }else{
        hideTandem('id_victim_situation_another');
    }
}

function onTradeUnionSituationChanged(value){
    if (value == 4){
        showTandem('id_tradeUnionSituation_another');
    }else{
        hideTandem('id_tradeUnionSituation_another');
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

hide_div('idTradeUnionDiv');
hideTandem('id_source_another');
hide_source();

// hideRights()

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

hideRights();
hide_div('idTradeUnionForm');
hide_div('idIndividualFormDiv');
hide_div('idPersonGroupFormDiv');
hideTandem('id_name');
hideTandem('id_agreementDetail');
hideTandem('id_type_another');
hideTandem('id_membership_another');
hideTandem('id_intruderAnother');
hideTandem('id_country_from');
hideTandem('id_is_tnk_member');
hideTandem('id_tnk_name');
hideTandem('id_control_agency_name');
hideTandem('id_intruderAnother');
hideTandem('id_government_agency_name');
hideTandem('id_local_agency_name');
hideTandem('id_police_agency_name');
hide_div('idTradeUnionDiv');
hide_div('idEmployerCompanyDiv');
hideTandem('id_rights_state_another');
hideTandem('id_victim_situation_another');
hideTandem('id_tradeUnionSituation_another');