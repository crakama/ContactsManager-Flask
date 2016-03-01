$(document).ready(function(){
	// $("#myModal").on('show.bs.modal', function(event){
 //        var button = $(event.relatedTarget);  // Button that triggered the modal
 //        console.log(event);
 //        var titleData = button.data('title'); // Extract value from data-* attributes
 //        $(this).find('.modal-title').text(titleData + ' Form');
 //    });
});

function Edit(elm) {
    $.ajax({
        url: '/getWishById',
        data: {
            id: $(elm).attr('data-id')
        },
        type: 'POST',
        success: function(res) {
            console.log(res);
        },
        error: function(error) {
            console.log(error);
        }
    });
    // Parse the received JSON string
    var data = JSON.parse(res);

    //Populate the Pop up
    $('#recipientNo').val(data[0]['mobilenumber']);
   

    // Trigger the Pop Up
    $('#SMSModal').modal();
}


function loadForm (number) {
	$('#myModal').modal();
	$('#recipientNo').val(number);
}