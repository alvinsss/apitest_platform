//获取Locust信息
var LocustInit = function () {

    var url = document.location;
    var locustfid =  url.pathname.split("/")[3];
    // alert(locustfid)
    $.post("/locustmanager/get_locustlist_info",
    {
        locustfid: locustfid,
    },
    function (resp, status) {

        console.log("返回的结果", resp.data);
        var result = resp.data;
        //下拉选择处理是否加密
         var optionsLength = document.getElementById('encryption').options.length;
         var pt = document.getElementById('encryption');
         for(var i = 0; i < optionsLength; i++){
             var option = parseInt(document.getElementById('encryption').options[i].value);
             if(option == result.encryption) {
                 pt.options[i].setAttribute("selected", "true");
             }
         }
        //请求host
        document.querySelector("#host").value = resp.data.host;
        document.querySelector("#lscript_name").value = result.lscript_name;
        document.querySelector("#slave_num").value = result.slave_num;
        document.querySelector("#uploadfile_text").value = result.uploadfile;
        // alert( result.uploadfile)
        // 初始化菜单
        SelectInit(result.project_id, result.module_id);
    });

}
