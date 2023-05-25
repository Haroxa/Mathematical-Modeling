 
clc; 
close all; 
clear all; 
I=imread('a02.jpg'); 
[m,n,d]=size(I); 
 
level=15;%设置阈值 
level2=70;%设置阈值 
 
for i=1:m 
    for j=1:n 
        if((I(i,j,1)-I(i,j,2)>level2)&&(I(i,j,1)-I(i,j,3)>level2)) 
            r(i,j,1)=I(i,j,1); 
            r(i,j,2)=I(i,j,2); 
            r(i,j,3)=I(i,j,3); 
       else  
            r(i,j,1)=255; 
            r(i,j,2)=255; 
            r(i,j,3)=255; 
        end 
    end 
end 
 
figure; 
subplot(2,2,1);imshow(I);title('原图像'); 
subplot(2,2,2);imshow(r);title('提取红分量后');%显示提取红分量后的图 
 
 
%提取绿分量，不满足阈值的变为白色 
for i=1:m 
    for j=1:n 
        if((I(i,j,2)-I(i,j,1)>level)&&(I(i,j,2)-I(i,j,3)>level)) 
            g(i,j,1)=I(i,j,1); 
            g(i,j,2)=I(i,j,2); 
            g(i,j,3)=I(i,j,3); 
        else 
            g(i,j,1)=255; 
            g(i,j,2)=255; 
            g(i,j,3)=255; 
        end 
    end 
end 
 
subplot(2,2,3);imshow(g);title('提取绿分量后'); 
 
 
%提取蓝色分量 
for i=1:m 
    for j=1:n 
        if((I(i,j,3)-I(i,j,1)>level)&&(I(i,j,3)-I(i,j,2)>level)) 
                    b(i,j,1)=I(i,j,1); 
                    b(i,j,2)=I(i,j,2); 
                    b(i,j,3)=I(i,j,3); 
        else 
            b(i,j,1)=255; 
            b(i,j,2)=255; 
            b(i,j,3)=255; 
        end 
    end 
end 
 
subplot(2,2,4);imshow(b);title('提取蓝色分量后');
 

