function [ LL ] = pso_fitness(Point_path,Sign)
% 函数功能：计算该个体对应适应度值
% x           input     个体
% fitness     output    个体适应度值

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


dijpathlen=0;
for i=1:length(z_2)-1
    dijpathlen=dijpathlen+sqrt((Lu_2(i,1)-Lu_2(i+1,1))^2+(Lu_2(i,2)-Lu_2(i+1,2))^2);
end
LL=dijpathlen;

end

