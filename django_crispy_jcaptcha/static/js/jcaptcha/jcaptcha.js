var jcaptcha = {
    var: { 
         current_selection: '',
    },
    select: function(field,primary_key, match_key) {
            $('#'+field).val(primary_key+":"+match_key);
            console.log(jcaptcha.var.current_selection)
            $('#id_captcha_image_'+jcaptcha.var.current_selection).removeClass("jcaptcha-active" );
            jcaptcha.var.current_selection = match_key;
            $('#id_captcha_image_'+match_key ).addClass( "jcaptcha-active" );
    }
}
