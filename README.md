# GetGenerate
生成OC的view相关代码

# 用途
通过终端打印已声明的view对象（带*)的get方法及约束方法（Masonry）代码

# 使用要求
python3环境
oc代码格式@property (nonatomic, strong) NSObject *name;

# 使用方法
1.终端cd到python文件所在文件夹
2.执行 python3 GetGenerate
3.将已声明的view属性粘贴进去
  如@property (nonatomic, strong) UIView *view1;（可多条同事执行）
4.回车，输入end，回车
@property (nonatomic, strong) UIView *view1;

end

5.输出
- (UIView *)view1 {
	if (!_view1) {
		_view1 = [[UIView alloc] init];
	}
	return _view1;
}

[self.view addSubview:self.view1];

[self.view1 mas_makeConstraints:^(MASConstraintMaker *make) {
	
}];
