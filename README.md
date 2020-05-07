# GetGenerate
生成OC的view相关代码

# 用途
通过终端打印已声明的view对象（带*)的get方法及约束方法（Masonry）代码

# 使用要求
python3环境
oc代码格式@property (nonatomic, strong) NSObject *name;

# 使用方法<br>
1.终端cd到python文件所在文件夹<br>
2.执行 python3 GetGenerate<br>
3.将已声明的view属性粘贴进去<br>
 如@property (nonatomic, strong) UIView *view1;（可多条同事执行）<br>
4.回车，输入end，回车<br>
@property (nonatomic, strong) UIView *view1;<br>
<br>
end<br>

5.输出<br>
\- (UIView *)view1 {<br>
　　if (!_view1) {<br>
　　　　 _view1 = [[UIView alloc] init];<br>
　　}<br>
　　return _view1;<br>
}<br>
<br>
[self.view addSubview:self.view1];<br>
<br>
[self.view1 mas_makeConstraints:^(MASConstraintMaker *make) {<br>
	<br>
}];<br>
