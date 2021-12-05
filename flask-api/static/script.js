$('#checkin_submit').click(function(event) {
    event.preventDefault();
    var form = $('#add_cust')[0];
    var data = new FormData(form);
    $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/reception/customer_checkin",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 800000,
            success: function (data) {
                if(data.hasOwnProperty('msg')) {
                  $('#msg').innerHTML = data['msg'];
                }
            },
            error: function (e) {
                console.log("ERROR : ", e);
            }
        });
});

$('#bill_sub').click(function(event) {
    event.preventDefault();
    var form = $('#bill_form')[0];
    var data = new FormData(form);
    $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/reception/pay_bill",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 800000,
            success: function (data) {
              if(data.hasOwnProperty('msg')) {
                $('#msg').innerHTML = data['msg'];
              }
            },
            error: function (e) {
                console.log("ERROR : ", e);
            }
        });
});

$('#checkout_form_sub').click(function(event) {
    event.preventDefault();
    var form = $('#checkout_form')[0];
    var data = new FormData(form);
    $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/reception/customer_checkout",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 800000,
            success: function (data) {
              if(data.hasOwnProperty('msg')) {
                document.getElementById('msg').innerHTML = data.msg;
              }
              table_text = `<tr><th>INFO</th><th>AMOUNT</th>
                            <th>PAYMENT MODE</th></tr>`;
              for(var i = 0; i < data.data.length; i++){
                table_text += `<tr>`;
                for(var j=0; j < data.data[i].length; j++){
                  table_text += `<td>`+data.data[i][j]+`</td>`;
                }
                table_text += `</tr>`;
                //console.log(data.data[i]);
              }
              document.getElementById('reception_table').innerHTML = table_text;
            },
            error: function (e) {
                console.log("ERROR : ", e);
            }
        });
});

$('#get_bill_sub').click(function(event) {
    event.preventDefault();
    var form = $('#get_bill_form')[0];
    var data = new FormData(form);
    $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/reception/get_bill",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 800000,
            success: function (data) {
                table_text = `<tr><th>INFO</th><th>AMOUNT</th>
                              <th>PAYMENT MODE</th><th>DATE</th></tr>`;
                for(var i = 0; i < data.data.length; i++){
                  table_text += `<tr>`;
                  for(var j=0; j < data.data[i].length; j++){
                    table_text += `<td>`+data.data[i][j]+`</td>`;
                  }
                  table_text += `</tr>`;
                  //console.log(data.data[i]);
                }
                document.getElementById('reception_table').innerHTML = table_text;
            },
            error: function (e) {
                console.log("ERROR : ", e);
            }
        });
});

$('#form_selector').change(function(event) {
  var form = '#'+document.getElementById('form_selector').value;
  $('.reception-form').css({'display':'none'});
  $(form).css({'display':'block'});
  document.getElementById('reception_table').innerHTML = '';
  document.getElementById('msg').innerHTML = '';
});
