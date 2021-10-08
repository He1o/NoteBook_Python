function [pathPoint,trace]= Calculate_pso(point_start,point_end,line_Mid,Sign)
%%   ��������Ⱥ�㷨��·���Ż�

%   pathPoint              �滮����·���ڵ�
%   trace                  ��������ֵ
%   point_start,point_end  ��ֹ������
%   line_Mid               ���Ƶ�����ͼ�ڵ�Ķ˵�
%   Sign                   �ܷ�ﵽ0-1����

%% 
% ��ʼ��PSO�㷨����
c1=1.49445;
c2=1.49445;
maxgen=100; %��������
sizepop=20; %��Ⱥ��ģ
popmax=1;popmin=0;  %����ȡֵ��Χ
Vmax=0.2;Vmin=-0.2; %�ٶ�ȡֵ��Χ
lenchrom=size(line_Mid,1);       %���峤��
pop=zeros(sizepop,lenchrom);
V=zeros(sizepop,lenchrom);
fitness=zeros(1,sizepop);
trace=zeros(1,maxgen);


%% ��ʼ����Ⱥ������Ӧ��ֵ
for i=1:sizepop
    pop(i,:)=rand(1,lenchrom);
    V(i,:)=Vmin*ones(1,lenchrom)+(Vmax-Vmin)*rand(1,lenchrom);
    
    x=pop(i,:);
    New_Mid=zeros(lenchrom,2);
    for k=1:length(New_Mid)
        New_Mid(k,:)=line_Mid(k,1:2)+(line_Mid(k,3:4)-line_Mid(k,1:2))*x(k);
    end
    Point_path=[point_start;New_Mid;point_end];%·����
    fitness(i)=pso_fitness(Point_path,Sign);   %Ⱦɫ�����Ӧ��
end
[bestfitness,bestindex]=min(fitness); %����õĸ���
zbest=pop(bestindex,:);         %Ⱥ�弫ֵλ��
gbest=pop;  %���弫ֵλ��
fitnesszbest=bestfitness;                 %Ⱥ�弫ֵ��Ӧ��ֵ
fitnessgbest=fitness;      %���弫ֵ��Ӧ��ֵ
%% ����Ѱ��
for i=1:maxgen
    for j=1:sizepop
        
        %�ٶȸ���
        V(j,:)=V(j,:)+c1*rand*(gbest(j,:)-pop(j,:))+c2*rand*(zbest-pop(j,:));
        V(j,find(V(j,:)>Vmax))=Vmax;
        V(j,find(V(j,:)<Vmin))=Vmin;
        
        %���Ӹ���
        pop(j,:)=pop(j,:)+V(j,:);
        pop(j,find(pop(j,:)>popmax))=popmax;
        pop(j,find(pop(j,:)<popmin))=popmin;
        
        %
        x=pop(j,:);
        New_Mid=zeros(lenchrom,2);
        for k=1:length(New_Mid)
            New_Mid(k,:)=line_Mid(k,1:2)+(line_Mid(k,3:4)-line_Mid(k,1:2))*x(k);
        end
        Point_path=[point_start;New_Mid;point_end];%·����
        fitness(j)=pso_fitness(Point_path,Sign);
    end
%     f(i)=sum((fitness-239.0996*ones(1,20)).^2)/20;
    for j=1:sizepop %���¼�ֵ
        %���弫ֵ����
        if fitness(j)<fitnessgbest(j)
            gbest(j,:)=pop(j,:);
            fitnessgbest(j)=fitness(j);
        end
        %Ⱥ�弫ֵ����
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
Point_path=[point_start;New_Mid;point_end];%·����
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
pathPoint=Lu_2;

end

