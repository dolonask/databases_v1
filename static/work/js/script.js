function hideTandem(id){
    $('#' + id + ', label[for=' + id + ']').hide();
}

function showTandem(id){
    $('#' + id + ', label[for=' + id + ']').show();
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