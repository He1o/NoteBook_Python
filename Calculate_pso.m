function [pathPoint,trace]= Calculate_pso(point_start,point_end,line_Mid,Sign)
%%   基于粒子群算法的路径优化

%   pathPoint              规划出的路径节点
%   trace                  迭代过程值
%   point_start,point_end  起止点坐标
%   line_Mid               绘制的链接图节点的端点
%   Sign                   能否达到0-1矩阵

%% 
% 初始化PSO算法参数
c1=1.49445;
c2=1.49445;
maxgen=100; %迭代次数
sizepop=20; %种群规模
popmax=1;popmin=0;  %个体取值范围
Vmax=0.2;Vmin=-0.2; %速度取值范围
lenchrom=size(line_Mid,1);       %个体长度
pop=zeros(sizepop,lenchrom);
V=zeros(sizepop,lenchrom);
fitness=zeros(1,sizepop);
trace=zeros(1,maxgen);


%% 初始化种群计算适应度值
for i=1:sizepop
    pop(i,:)=rand(1,lenchrom);
    V(i,:)=Vmin*ones(1,lenchrom)+(Vmax-Vmin)*rand(1,lenchrom);
    
    x=pop(i,:);
    New_Mid=zeros(lenchrom,2);
    for k=1:length(New_Mid)
        New_Mid(k,:)=line_Mid(k,1:2)+(line_Mid(k,3:4)-line_Mid(k,1:2))*x(k);
    end
    Point_path=[point_start;New_Mid;point_end];%路径点
    fitness(i)=pso_fitness(Point_path,Sign);   %染色体的适应度
end
[bestfitness,bestindex]=min(fitness); %找最好的个体
zbest=pop(bestindex,:);         %群体极值位置
gbest=pop;  %个体极值位置
fitnesszbest=bestfitness;                 %群体极值适应度值
fitnessgbest=fitness;      %个体极值适应度值
%% 迭代寻优
for i=1:maxgen
    for j=1:sizepop
        
        %速度更新
        V(j,:)=V(j,:)+c1*rand*(gbest(j,:)-pop(j,:))+c2*rand*(zbest-pop(j,:));
        V(j,find(V(j,:)>Vmax))=Vmax;
        V(j,find(V(j,:)<Vmin))=Vmin;
        
        %粒子更新
        pop(j,:)=pop(j,:)+V(j,:);
        pop(j,find(pop(j,:)>popmax))=popmax;
        pop(j,find(pop(j,:)<popmin))=popmin;
        
        %
        x=pop(j,:);
        New_Mid=zeros(lenchrom,2);
        for k=1:length(New_Mid)
            New_Mid(k,:)=line_Mid(k,1:2)+(line_Mid(k,3:4)-line_Mid(k,1:2))*x(k);
        end
        Point_path=[point_start;New_Mid;point_end];%路径点
        fitness(j)=pso_fitness(Point_path,Sign);
    end
%     f(i)=sum((fitness-239.0996*ones(1,20)).^2)/20;
    for j=1:sizepop %更新极值
        %个体极值更新
        if fitness(j)<fitnessgbest(j)
            gbest(j,:)=pop(j,:);
            fitnessgbest(j)=fitness(j);
        end
        %群体极值更新
        if fitness(j)<fitnesszbest
            zbest=pop(j,:);
            fitnesszbest=fitness(j);
        end
    end
    
    trace(i)=fitnesszbest;
end

% x=sum(f)/100;


x=zbest;
New_Mid(:,1)=line_Mid(:,1)+(line_Mid(:,3)-line_Mid(:,1)).*x';
for j=1:length(New_Mid)
    if (line_Mid(j,3)-line_Mid(j,1))==0
        New_Mid(j,2)=line_Mid(j,2)+(line_Mid(j,4)-line_Mid(j,2))*x(j);
    else
        New_Mid(j,2)=line_Mid(j,2)+((line_Mid(j,4)-line_Mid(j,2))/(line_Mid(j,3)-line_Mid(j,1)))*(New_Mid(j,1)-line_Mid(j,1));
    end
end
Point_path=[point_start;New_Mid;point_end];%路径点
z=DijkstraPlan(Point_path,Sign);%dijkstra最短路
z_2=length(z);
for i=1:length(z) %找到终点到起点的最短路
    z_2(i+1)=z(z_2(i));
    if z(z_2(i))==1
        break
    end
end
z_2=fliplr(z_2);
Lu_2=Point_path(z_2,:);%初始起止路径坐标
pathPoint=Lu_2;

end

