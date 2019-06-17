//获取PythonFileInit信息
var PythonFileInit = function () {

    var url = document.location;
    var pyfid =  url.pathname.split("/")[3];
    // alert(locustfid)
    $.post("/unittest/get_unittestlist_info/",
    {
        pyfid: pyfid,
    },
    function (resp, status) {

        console.log("返回的结果", resp.data);
        var result = resp.data;
        document.querySelector("#unittestscript_name").value = result.unittestscript_name;
        document.querySelector("#uploadfile_text").value = result.uploadfile;
        // alert( result.uploadfile)
        // 初始化菜单
        SelectInit(result.project_id, result.module_id);
    });

}
	//发送方法
	function RunUnittest(tid) {
		console.log("运行任务的id", tid);

		$.post("/unittest/run_unittest_task/",
		{
			task_id:tid,
		},
		function (data, status) {
			alert("提示：" + data.message);
		});

	};