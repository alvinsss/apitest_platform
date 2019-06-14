
接口测试平台介绍
=================

1、目录结构
-----------
  apps:子功能模块<br>
  exta_apps:xadmin资源文件<br>
  static:静态资源css,js文件<br>
  templates:html文件<br>
  test_platform:django配置文件<br>
  utils:工具类<br>
  my.cnf:mysql配置独立文件
  nginx.conf 和 test_platform.xml 部署nginx和uwsgi配置文件
  requiremenets.txt 项目依赖文件
  
2、部署版本要求
-----------

    1、mysql5.6+
    2、python3.6
    3、django2+
    4、django-formtools2+

3、centos6+部署步骤
-----------
    一：uwsgi+python
        http://note.youdao.com/noteshare?id=d3286e55ee0206da47f188555b03c749&sub=49BC716EBF44490CB953962514155B19
    
    二：centos6安装mysql和创建数据库
        http://note.youdao.com/noteshare?id=842d7fc3f9cebd9624a17240c645a471&sub=C2A18E3A3C4B497AA82EBB83AD6006A5
        
    三：git下载源码并安装第三方库
        http://note.youdao.com/noteshare?id=4becfd9e8d325d370af94941b70e9359&sub=0B9FB935420C4C4FA1176B73C686B321
    
    四：初始化数据及运行
        http://note.youdao.com/noteshare?id=3d2c384bf21abd81cb44a5833ae60d3d&sub=8744555B60944BE2A8E6F7DFBAC14C9B
        
    五：uwsgi和nginx配置
        http://note.youdao.com/noteshare?id=89158d9a4c32109ef86672fa8dd76f61&sub=BAF6B4F7337F4F14BFFD5211F8936F68
        
    
     
     


4、作者信息
-----------

  author:alvin<br>
  qq    :6449694<br>
  email :wanghailin@aliyun.com<br>
