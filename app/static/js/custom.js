
function SendSMSModal (number) {
	$('#myModal').modal();
	$('#recipientNo').val(number);
}

function Edit (firstname,lastname,mobilenumber,country,skypeID,position,organization,email) {
    $('#my').modal();
    $('#firstname').val(string);
    $('#lastname').val(string);
    $('#mobilenumber').val(number);
    $('#country').val(string);
    $('#skypeID').val(string);
    $('#position').val(string);
    $('#organization').val(string);
    $('#email').val(string);
}
$(window).load(function() {    

    var theWindow        = $(window),
        $bg              = $("#bg"),
        aspectRatio      = $bg.width() / $bg.height();
                                
    function resizeBg() {
        
        if ( (theWindow.width() / theWindow.height()) < aspectRatio ) {
            $bg
                .removeClass()
                .addClass('bgheight');
        } else {
            $bg
                .removeClass()
                .addClass('bgwidth');
        }
                    
    }
                                
    theWindow.resize(resizeBg).trigger("resize");

});