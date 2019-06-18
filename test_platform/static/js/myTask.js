
	//发送方法
	function RunTask(tid) {
		console.log("运行任务的id", tid);

		$.post("/testtask/run_task/",
		{
			task_id:tid,
		},
		function (data, status) {
			alert("提示：" + data.message);
		});

	};

