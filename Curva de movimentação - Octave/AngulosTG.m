% Parametros %
a = 2*pi/6; 
c = pi/6;
k = 3/2; 
b = 2*pi*k;

% Constantes %
M = 9; % numero de juntas %
d = 70; % distancia entre as juntas [mm] %

wtrad = 0:(pi/360):(2*pi);
wtdeg = (180/pi)*wtrad;

jointanglerad = cell([1,M]);
jointangledeg = cell([1,M]);

for i=1:M
    jointanglerad{1,i} = [-2*a*sin(b/(2*M))]*[sin((wtrad)+(i*b/M))] -c/M;  %calcula o angulo de cada junta em cada instante
    jointangledeg{1,i} = (180/pi)*jointanglerad{1,i};
end

display(jointangledeg);


filename = "TabelaDeAngulos.txt"; %cria um arquivo .txt com a tabela de angulos
fid = fopen (filename, "w");
fputs (fid, "angletable = [\n");
for k = 1:M
  fputs (fid, "[");
  fprintf(fid, ", %f", jointanglerad{1,k}); %apagar , antes de cada primeiro elemento
  fputs (fid, "],\n"); %apagar , depois do ultimo array
end
fputs (fid, "]\n");
fclose (fid);


hold all
for j = 1:M
    plot(wtdeg,jointanglerad{1,j}, "linewidth", 3)
end
set(gca, "linewidth",1, "fontsize", 20)
hold off
title('Joint Angles')
ylabel('joint angle ( degrees )')
xlabel('phase ( degrees )')
