@echo off
"C:\Users\home\AppData\Local\Programs\Python\Python37-32\python.exe" "C:\Users\home\OneDrive\projetosUninta\gamefication\5 - BotReports.py"

start /wait "C:\Users\home\AppData\Local\Programs\Python\Python37-32\python.exe" "C:\Users\home\OneDrive\projetosUninta\gamefication\5 - BotReports.py" /ALL /Quite
 "C:\Users\home\AppData\Local\Programs\Python\Python37-32\python.exe" "C:\Users\home\OneDrive\projetosUninta\gamefication\tratarPlanilha.py"
 
 timeout 5
 start /wait "C:\Users\home\AppData\Local\Programs\Python\Python37-32\python.exe" "C:\Users\home\OneDrive\projetosUninta\gamefication\tratarPlanilha.py" /ALL /Quite
 "C:\Users\home\AppData\Local\Programs\Python\Python37-32\python.exe" "C:\Users\home\OneDrive\projetosUninta\gamefication\contadorpy.py"
 
 timeout 5
 start /wait "C:\Users\home\AppData\Local\Programs\Python\Python37-32\python.exe" "C:\Users\home\OneDrive\projetosUninta\gamefication\contadorpy.py" /ALL /Quite
 "C:\Users\home\AppData\Local\Programs\Python\Python37-32\python.exe" "C:\Users\home\OneDrive\projetosUninta\gamefication\importServer.py"



