$(document).ready(function(){
	var p = new Pusher('4e1da9ef46b3a8d5088e');
	var channel = p.subscribe('my_channel');
	channel.bind('notification',function(data){
		alert(data.username + ' is online.');
	});

	channel.bind('chat',function(data){
		$('#chat').append(data.username+": "+data.chat+"<br>");
	});

	$('#chat_cont').on('keydown', function(e){
    	if(e.which==13) {
    		e.preventDefault();
			$('#button-send-chat').click();
		}
  	});
	
	$('#button-send-chat').click(function(){
		var chat=$('#chat_cont').val();
		$.ajax({
			url: '/chat',
			type:'POST',
			data:{"chat":chat},
			// 여기까지는 데이터를 리로딩 하지 않고 보내는 것
			success:function(response){
				var result = $.parseJSON(response);
				// if(result['content']=="bad"){
				// 	$('#chat_err').text("Oops, you have to type anything!");
				// }
				console.log(result['content']);
			},
			error: function(){
				console.log('error');
			},
			complete:function(){
				console.log('complete');
			}
		});
		$('#chat_cont').val("");
	});



});