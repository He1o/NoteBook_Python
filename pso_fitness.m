function [ LL ] = pso_fitness(Point_path,Sign)
% �������ܣ�����ø����Ӧ��Ӧ��ֵ
% x           input     ����
% fitness     output    ������Ӧ��ֵ

z=DijkstraPlan(Point_path,Sign);%dijkstra���·
z_2=length(z);
for i=1:length(z) %�ҵ��յ㵽�������·
    z_2(i+1)=z(z_2(i));
    if z(z_2(i))==1
        break
    end
end
z_2=fliplr(z_2);
Lu_2=Point_path(z_2,:);%��ʼ��ֹ·������


dijpathlen=0;
for i=1:length(z_2)-1
    dijpathlen=dijpathlen+sqrt((Lu_2(i,1)-Lu_2(i+1,1))^2+(Lu_2(i,2)-Lu_2(i+1,2))^2);
end
LL=dijpathlen;

end

