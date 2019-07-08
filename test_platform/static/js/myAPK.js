//获取APKFileInit信息
var APKFileInit = function () {

    var url = document.location;
    var tid =  url.pathname.split("/")[3];
    $.post("/sdk/get_sdk_info/",
    {
        task_id: tid,
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
	//运行test方法
	function RunAPKtest(tid) {
		console.log("运行任务的 run_apk_task id", tid);

		$.post("/apk/run_apk_task/",
		{
			task_id:tid,
		},
		function (data, status) {
			alert("提示：" + data.message);
		});

	};

	//发送email方法
    function RunAPKmail(tid) {
		console.log("运行任务的 send_apk_mail id", tid);
		$.post("/apk/send_apk_mail/",
		{
			task_id:tid,
		},
		function (data, status) {
			alert("提示：" + data.message);
		});
	};

    function checkOrCancelAll(){
        //1.获取checkbo的元素对象
        var chElt=document.getElementById("chElt");
        //2.获取选中状态
        var checkedElt=chElt.checked;
        console.log("checkedElt",checkedElt)
        //3.若checked=true,将所有的复选框选中,checked=false,将所有的复选框取消
        var allCheck=document.getElementsByName("apk_testtype");
        //4.循环遍历取出每一个复选框中的元素
        //var mySpan=document.getElementById("mySpan");
        if(checkedElt){
            //全选
            for(var i=0;i<allCheck.length;i++){
            //设置复选框的选中状态
            allCheck[i].checked=true;
        }
        //mySpan.innerHTML="取消全选";
        }else{
            //取消全选
            for(var i=0;i<allCheck.length;i++){
            allCheck[i].checked=false;
              }
        //mySpan.innerHTML="全选";
            }
    }