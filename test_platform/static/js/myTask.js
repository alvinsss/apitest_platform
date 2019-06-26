	function RunTask(tid) {
		console.log("运行任务的id", tid);

		$.post("/testtask/run_task/",
		{
			task_id: tid
		},
		function (resp) {
		    if(resp.status == 10200){
		        window.alert(resp.message);
				window.location.reload();  // 刷新页面
			}

		});

	};



