% Parametros %
a = 60*pi/180; 
c = 0;
k = 1; 
b = 2*pi*k;

% Constantes %
M = 6; % numero de juntas %
d = 70; % distancia entre as juntas [mm] %

wtrad = 0;
wtdeg = (180/pi)*wtrad;

jointanglerad = cell([1,M]);
jointangledeg = cell([1,M]);

for i=1:M
    jointanglerad{1,i} = [-2*a*sin(b/(2*M))]*[sin((wtrad)+(i*b/M))] -c/M; %calcula o angulo de cada junta em cada instante
    jointangledeg{1,i} = (180/pi)*jointanglerad{1,i}; 
end




xposition = cell([1,M]);
yposition = cell([1,M]);

xposition{1,1} = d*cos(a);
yposition{1,1} = d*sin(a);
drelativo = a

for l=2:M
  drelativo = drelativo + jointanglerad{1,l-1};
  display(drelativo)
  xposition{1,l} = xposition{1,l-1} + d*cos(drelativo); %calcula posicao de cada junta na primeira posicao da tabela de angulos
  yposition{1,l} = yposition{1,l-1} + d*sin(drelativo);
end

xposition = cell2mat(xposition);
yposition = cell2mat(yposition);

hold all
plot(xposition,yposition, "linewidth", 3, "-*");
set(gca, "linewidth",1, "fontsize", 20)
xlabel("x (mm)")
ylabel("y (mm)")
hold off







% Parametros %
a = 60*pi/180; 
c = 0;
k = 1; 
b = 2*pi*k;

% Constantes %
M = 8; % numero de juntas %
d = 70; % distancia entre as juntas [mm] %

wtrad = 0;
wtdeg = (180/pi)*wtrad;

jointanglerad = cell([1,M]);
jointangledeg = cell([1,M]);

for i=1:M
    jointanglerad{1,i} = [-2*a*sin(b/(2*M))]*[sin((wtrad)+(i*b/M))] -c/M; %calcula o angulo de cada junta em cada instante
    jointangledeg{1,i} = (180/pi)*jointanglerad{1,i}; 
end




xposition = cell([1,M]);
yposition = cell([1,M]);

xposition{1,1} = d*cos(a);
yposition{1,1} = d*sin(a);
drelativo = a

for l=2:M
  drelativo = drelativo + jointanglerad{1,l-1};
  display(drelativo)
  xposition{1,l} = xposition{1,l-1} + d*cos(drelativo); %calcula posicao de cada junta na primeira posicao da tabela de angulos
  yposition{1,l} = yposition{1,l-1} + d*sin(drelativo);
end

xposition = cell2mat(xposition);
yposition = cell2mat(yposition);

hold all
plot(xposition,yposition, "linewidth", 3, "-*");
set(gca, "linewidth",1, "fontsize", 20)
xlabel("x (mm)")
ylabel("y (mm)")
hold off






% Parametros %
a = 60*pi/180; 
c = 0;
k = 1; 
b = 2*pi*k;

% Constantes %
M = 10; % numero de juntas %
d = 70; % distancia entre as juntas [mm] %

wtrad = 0;
wtdeg = (180/pi)*wtrad;

jointanglerad = cell([1,M]);
jointangledeg = cell([1,M]);

for i=1:M
    jointanglerad{1,i} = [-2*a*sin(b/(2*M))]*[sin((wtrad)+(i*b/M))] -c/M; %calcula o angulo de cada junta em cada instante
    jointangledeg{1,i} = (180/pi)*jointanglerad{1,i}; 
end




xposition = cell([1,M]);
yposition = cell([1,M]);

xposition{1,1} = d*cos(a);
yposition{1,1} = d*sin(a);
drelativo = a

for l=2:M
  drelativo = drelativo + jointanglerad{1,l-1};
  display(drelativo)
  xposition{1,l} = xposition{1,l-1} + d*cos(drelativo); %calcula posicao de cada junta na primeira posicao da tabela de angulos
  yposition{1,l} = yposition{1,l-1} + d*sin(drelativo);
end

xposition = cell2mat(xposition);
yposition = cell2mat(yposition);

hold all
plot(xposition,yposition, "linewidth", 3,"-*");
set(gca, "linewidth",1, "fontsize", 20)
xlabel("x (mm)")
ylabel("y (mm)")
h = legend({"M = 6", "M = 8", "M = 10"}, "location", "southwest")
set (h, "fontsize", 35)
hold off
