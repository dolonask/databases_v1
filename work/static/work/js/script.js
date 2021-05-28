function hideTandem(id){
    $('#' + id + ', label[for=' + id + ']').hide();
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
    if (value == 0){
        // Get the checkbox
        var checkBox = document.getElementById("id_card_sources_0");
        // Get the output text
        // If the checkbox is checked, display the output text
        if (checkBox.checked == true){
            // document.getElementById("id_source_url").readOnly=true;
            hideTandem("id_source_url");
            hideTandem("id_source_content");
        } else {
            showTandem("id_source_url")
            showTandem("id_source_content")
        }
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
    hideTandem('id_tradeUnionRightAnother');
    hideTandem('id_tradeUnionCrime');
    hideTandem('id_tradeUnionCrimeAnother');
    hideTandem('id_tradeUnionBuildingsRight');
    hideTandem('id_meetingsRight');

    switch (value){
        case '1':
            showTandem('id_tradeUnionCrime');
            break;
        case '3':
            showTandem('id_meetingsRight')
            break;
        case '7':
            showTandem('id_tradeUnionRightAnother');
            break;
        case '6':
            showTandem('id_tradeUnionBuildingsRight')
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
            showTandem('id_createOrganizationRight');
            break;
    }
}

function hideRights(){
    hideTandem('id_tradeUnionRight');
    hideTandem('id_tradeUnionRightAnother');
    hideTandem('id_tradeUnionCrime');
    hideTandem('id_tradeUnionCrimeAnother');
    hideTandem('id_meetingsRight');
    hideTandem('id_meetingsRightAnother');
    hideTandem('id_tradeUnionBuildingsRight');
    hideTandem('id_tradeUnionBuildingsRightAnother');
    hideTandem('id_createOrganizationRight');
    hideTandem('id_createOrganizationRightAnother');
}


hideRights()


