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

	function detail_result(id) {
        console.log("查看详情日志！", id);
        $.post("/testtask/get_detail_result/", {
				result_id: id,
			},
			function (resp) {
				if(resp.status == 10200){
					console.log(resp.data);
					// resp.data = resp.data.replace(/AssertionError/ig,"<span style='color: red;'>$&</span>");
					document.querySelector("#log").innerText = resp.data;
				}
			});
    }


