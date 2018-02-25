$( document ).ready(function() {

	const url = "http://127.0.0.1:5000";

    $('.task').click(function() {
		let id = $(this).parent().attr('id');
		$(this).toggleClass('line-through');
		let isLineThrough = $(this).hasClass('line-through');
		$.ajax({
			method: "POST",
			url: `${url}/auth`,
			contentType: "application/json",
			dataType: "json",
			data: JSON.stringify({
				username: 'jason', 
				password: 'jason'
			})
		})
		.then(function(token_data) {
			let access_token = token_data.access_token;
			$.ajax({
				beforeSend: function(xhr) {
					xhr.setRequestHeader ("Authorization", `JWT ${access_token}`);
				},
				method: "GET",
				url: `${url}/task/${id}`,
				contentType: "application/json",
				dataType: "json"
			})
			.then(function(task_data) {
				isLineThrough ? task_data.complete = true : task_data.complete = false;				
				$.ajax({
					beforeSend: function(xhr) {
						xhr.setRequestHeader ("Authorization", `JWT ${access_token}`);
					},
					method: "PUT",
					url: `${url}/task/${id}`,
					contentType: "application/json",
					dataType: "json",
					data: JSON.stringify({
						title: task_data.title, 
						category_name: task_data.category_name, 
						complete: task_data.complete
					})
				})
				.then(function(data) {
					console.log(data)
				});
			})
		})
	});

	$('.delete-task').click(function() {
		let id = $(this).parent().attr('id');
		$(this).parent().remove();
		$.ajax({
			method: "POST",
			url: `${url}/auth`,
			contentType: "application/json",
			dataType: "json",
			data: JSON.stringify({
				username: 'jason',
				password: 'jason'
			})
		})
		.then(function(token_data) {
			let access_token = token_data.access_token;			
			$.ajax({
				beforeSend: function(xhr) {
					xhr.setRequestHeader ("Authorization", `JWT ${access_token}`);
				},
				method: "DELETE",
				url: `${url}/task/${id}`,
				contentType: "application/json",
				dataType: "json"
			})
			.then(function(data) {
				console.log(data);
			});
		});
	});
});