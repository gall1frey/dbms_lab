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
								console.log(data);
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
								document.getElementById('msg').innerHTML = data['msg'];
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
							table_text = `<tr><th>BILL ID</th><th>INFO</th><th>AMOUNT</th>
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

$('#list_accounts_sub').click(function(event) {
	event.preventDefault();
	var form = $('#accounts_list_form')[0];
	var data = new FormData(form);
	$.ajax({
					type: "POST",
					enctype: 'multipart/form-data',
					url: "/accounts/list",
					data: data,
					processData: false,
					contentType: false,
					cache: false,
					timeout: 800000,
					success: function (data) {
							console.log(data);
							table_text = `<tr>`;
							for(var i = 0; i < data.cols.length; i++){
								table_text += `<th>`+data.cols[i]+`</th>`;
							}
							table_text += `<tr>`;
							for(var i = 0; i < data.data.length; i++){
								table_text += `<tr>`;
								for(var j=0; j < data.data[i].length; j++){
									table_text += `<td>`+data.data[i][j]+`</td>`;
								}
								table_text += `</tr>`;
								//console.log(data.data[i]);
							}
							document.getElementById('accounts_table').innerHTML = table_text;
					},
					error: function (e) {
							console.log("ERROR : ", e);
					}
			});
});

$('#list_serv_sub').click(function(event) {
	event.preventDefault();
	var form = $('#list_services_form')[0];
	var data = new FormData(form);
	$.ajax({
					type: "POST",
					enctype: 'multipart/form-data',
					url: "/services/list",
					data: data,
					processData: false,
					contentType: false,
					cache: false,
					timeout: 800000,
					success: function (data) {
							//console.log(data);
							table_text = `<tr><th>SERVICE ID</th><th>SERVICE NAME</th>
														<th>SERVICE DESCRIPTION</th><th>SERVICE CHARGES</th></tr>`;
							for(var i = 0; i < data.data.length; i++){
								table_text += `<tr>`;
								for(var j=0; j < data.data[i].length; j++){
									table_text += `<td>`+data.data[i][j]+`</td>`;
								}
								table_text += `</tr>`;
								//console.log(data.data[i]);
							}
							document.getElementById('service_table').innerHTML = table_text;
					},
					error: function (e) {
							console.log("ERROR : ", e);
					}
			});
});

$('#use_serv_sub').click(function(event) {
	event.preventDefault();
	var form = $('#use_services_form')[0];
	var data = new FormData(form);
	$.ajax({
					type: "POST",
					enctype: 'multipart/form-data',
					url: "/services/use",
					data: data,
					processData: false,
					contentType: false,
					cache: false,
					timeout: 800000,
					success: function (data) {
						document.getElementById('msg').innerHTML = data.msg;
					},
					error: function (e) {
							console.log("ERROR : ", e);
					}
			});
});

$('#update_accounts_sub').click(function(event) {
	event.preventDefault();
	var form = $('#accounts_update_form')[0];
	var data = new FormData(form);
	$.ajax({
					type: "POST",
					enctype: 'multipart/form-data',
					url: "/accounts/update",
					data: data,
					processData: false,
					contentType: false,
					cache: false,
					timeout: 800000,
					success: function (data) {
							console.log(data);
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
							document.getElementById('accounts_table').innerHTML = table_text;
					},
					error: function (e) {
							console.log("ERROR : ", e);
					}
			});
});

$('#form_selector_reception').change(function(event) {
	var form = '#'+document.getElementById('form_selector_reception').value;
	$('.reception-form').css({'display':'none'});
	$(form).css({'display':'block'});
	//document.getElementById('reception_table').innerHTML = '';
	document.getElementById('msg').innerHTML = '';
});

$('#form_selector_services').change(function(event) {
	var form = '#'+document.getElementById('form_selector_services').value;
	$('.service-form').css({'display':'none'});
	$(form).css({'display':'block'});
	//document.getElementById('service_table').innerHTML = '';
	//document.getElementById('msg').innerHTML = '';
});

$('#form_selector_accounts').change(function(event) {
	var form = '#'+document.getElementById('form_selector_accounts').value;
	$('.accounts-form').css({'display':'none'});
	$(form).css({'display':'block'});
	document.getElementById('accounts_table').innerHTML = '';
	document.getElementById('msg').innerHTML = '';
});
