
function onSourceChanged(value) {
    console.log(value);
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