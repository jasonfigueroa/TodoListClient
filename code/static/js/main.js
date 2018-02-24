$( document ).ready(function() {
    $('.task').click(function() {
		$(this).toggleClass('line-through');
		// TODO async mark as complete in db
	});

	$('.delete-task').click(function() {
		var id = $(this).parent().attr('id');
		$(this).parent().remove();
		$.ajax({
			method: "POST",
			url: "http://127.0.0.1:5000/auth",
			contentType: "application/json",
			dataType: "json",
			data: JSON.stringify({
				username: 'jason',
				password: 'jason'
			}),
		})
		.then(function(token_data) {
			var access_token = token_data.access_token;			
			$.ajax({
				beforeSend: function (xhr) {
					xhr.setRequestHeader ("Authorization", `JWT ${access_token}`);
				},
				method: "DELETE",
				url: `http://127.0.0.1:5000/task/${id}`,
				contentType: "application/json",
				dataType: "json"
			})
			.then(function(data) {
				console.log(data);
			});
		});
	});
});