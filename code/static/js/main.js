$( document ).ready(function() {

	const url = "http://127.0.0.1:5000";

	$('#add-task-button').click(function() {
		$(this).addClass('hidden');
		$('#add-task-form').removeClass('hidden');
	});

	$('#cancel-add-task-button').click(function(event) {
		event.preventDefault();
		$('#add-task-form').addClass('hidden');
		$('#add-task-button').removeClass('hidden');
	});

	$('#add-category-button').click(function() {
		$(this).addClass('hidden');
		$('#add-category-form').removeClass('hidden');
	});

	$('#cancel-add-category-button').click(function(event) {
		event.preventDefault();
		$('#add-category-form').addClass('hidden');
		$('#add-category-button').removeClass('hidden');
	});

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

	$('.delete-category').click(function() {
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
				url: `${url}/category/${id}`,
				contentType: "application/json",
				dataType: "json"
			})
			.then(function(data) {
				console.log(data);
			});
		});
	});
});