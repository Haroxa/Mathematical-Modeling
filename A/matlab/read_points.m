% 读取图像文件
img = imread('r_02.png');

% 显示图像
imshow(img);

% 调用 ginput 函数获取用户选择的点
pts = ginput();

% 显示选择的点
disp(pts);

% 将点保存到文件中
xlswrite('matlab\test_points_02.xls',pts);