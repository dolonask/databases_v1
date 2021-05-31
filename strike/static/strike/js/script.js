
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

function disable(id){
    document.getElementById(id).disabled = true;
}
function enable(id){
    document.getElementById(id).disabled = false;
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

function onSourceChanged(value) {
    var checkBox = document.getElementById("id_card_sources_0");
    if (checkBox.checked == true){
        showTandem("id_source_url");
        showTandem("id_source_content");
    } else {
        hideTandem("id_source_url")
        hideTandem("id_source_content")
    }
}
function onCompanyOwnershipChanged(value) {
    // var checkBox = document.getElementById("id_source_1");
    // if (checkBox.checked == true){
    //     show_div("div_media")
    // } else {
    //     hide_div("div_media")
    // }

    if (get_selected('id_company_ownership_type') == 4){
        showTandem('id_company_is_tnk_member');
    }else{
        hideTandem('id_company_is_tnk_member');
    }
}

function onTradeunionChoiceChanged(value) {
    if (get_selected('id_tradeunionChoice') == 4){
        showTandem('id_tradeunionChoiceAnother');
    }else{
        hideTandem('id_tradeunionChoiceAnother');
    }
}



function onTnkChanged(value) {
    if (get_selected('id_company_is_tnk_member') == 'YES'){
        showTandem('id_company_tnk_name')
    }else if (value = 'NO'){
        hideTandem('id_company_tnk_name')
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
function sources(){
    let x = document.getElementById('card_sources');
    if(x.options[0].selected === true){
        document.getElementById("source_url").style.display = "block";
        document.getElementById("source_con").style.display = "block";
        console.log(x.options[0]);
    }
    else{
        document.getElementById("source_url").style.display = "none";
        document.getElementById("source_con").style.display = "none";
        console.log(x.options[0]);
    }
}

function onCardDemandCategoriesChanged(value) {

    if (document.getElementById("card_demands_0").checked == true) {
        showTandem('id_economic_demands');
    }else{
        hideTandem('id_economic_demands');
    }
    if(document.getElementById("card_demands_1").checked== true) {
        showTandem('id_politic_demands');
    }else{
        hideTandem('id_politic_demands');
    }
    if(document.getElementById("card_demands_2").checked== true){
        showTandem('id_combo_demands');
    }else{
        hideTandem('id_combo_demands');
    }
}

function onInitiatorSelected(value){

    switch (get_selected('id_initiator')){
        case '1':
            show_div('idTradeUnionDiv')
            hide_div('idPersonGroupInfoDiv')
            hide_div('idIndividualFormDiv')
            hide_div('idEmployerFormDiv')
            break;
        case '2':
            hide_div('idTradeUnionDiv')
            show_div('idPersonGroupInfoDiv')
            hide_div('idIndividualFormDiv')
            hide_div('idEmployerFormDiv')
            break;
        case '3':
            hide_div('idTradeUnionDiv')
            hide_div('idPersonGroupInfoDiv')
            show_div('idIndividualFormDiv')
            hide_div('idEmployerFormDiv')
            break;
        case '4':
            hide_div('idTradeUnionDiv')
            hide_div('idPersonGroupInfoDiv')
            hide_div('idIndividualFormDiv')
            show_div('idEmployerFormDiv')
            break;
        default:
            hide_div('idTradeUnionDiv')
            hide_div('idPersonGroupInfoDiv')
            hide_div('idIndividualFormDiv')
            hide_div('idEmployerFormDiv')
            break;
    }
}

function onGroupCharacterChanged(value){
    if (get_selected('id_groupCharacter')==3){
        showTandem("id_groupCharacter_another")
    }else {
        hideTandem("id_groupCharacter_another")
    }
}


function onIndividualAnonimChanged(value){
    if (get_selected('id_is_anonim') == 'NO'){
        showTandem("id_individual_name");
    }else {
        hideTandem("id_individual_name");
    }
}

function onEconomicDemandsChanged(value){
    if(document.getElementById("id_economic_demands_4").checked== true){
        showTandem('id_economic_another');
    }else{
        hideTandem('id_economic_another');
    }
}
function onPoliticDemandsChanged(value){
    if(document.getElementById("id_politic_demands_3").checked== true){
        showTandem('id_politic_another');
    }else{
        hideTandem('id_politic_another');
    }
}
function onComboDemandsChanged(value){
    if(document.getElementById("id_combo_demands_1").checked== true){
        showTandem('id_combo_another');
    }else{
        hideTandem('id_combo_another');
    }
}

// hide_div('idTradeUnionDiv')
// hide_div('idPersonGroupInfoDiv')
// hide_div('idIndividualFormDiv')
// hide_div('idEmployerFormDiv')
// hide_div('card_demands')

onIndividualAnonimChanged();
onSourceChanged();
onInitiatorSelected();
onEconomicDemandsChanged();
onPoliticDemandsChanged();
onComboDemandsChanged();
onTradeunionChoiceChanged();
onCompanyOwnershipChanged();
onTnkChanged();
onGroupCharacterChanged();
onCardDemandCategoriesChanged();
//
// hideTandem("id_groupCharacter_another")
// hideTandem("id_company_is_tnk_member")
// hideTandem("id_company_tnk_name")
// hideTandem("id_tradeunionChoiceAnother")
// hideTandem("id_economic_another ")
// hideTandem("id_politic_another")
// hideTandem("id_combo_another")
