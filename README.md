# DRipper-py-Updated from palahsu/DDoS-Ripper
Easy way to run attack. Just start file with python3 start.py or python start.py and than just edit target of attack in IP.txt - attack will start auto

Для старої версії DDoS-Ripper`a апдейтнув файл start.py . Теперь коли змінюється файл IP.txt (тобто змінюється ціль (зараз поки що лише один ІР може бути)) - відкривається нове вікно атаки:  

також обов'язково потрібен Python3:  

Вінда:  
заходите в cmd (Командная строка), прописуєте - python3 , вас перекине у Microsoft Store, там отримуєте Python  

лінукс:  
sudo apt install git -y  
sudo apt upgrade git -y  
sudo apt install python3 -y  
sudo apt upgrade python3 -y  

 УВАГА У ФАЙЛІ ІР.txt  одночасно може знаходитися лише один ІР:PORT  
ЗАЛИШАЙТЕ ВІКДРИТИМИ НЕ БІЛЬШЕ 3-ОХ ПРАЦЮЮЧИХ СКРИПТІВ  
НЕ ЗАБУВАЙТЕ ЗБЕРІГАТИ ЗМІНИ У IP.txt  

*Для Віндовс*   
!!!Файли start.py та IP.txt требе занести у ту ж папку де знаходиться DRipper.py!!!  
відкривається нове вікно програми з атакою, якщо ІР та Порт коректні (тобто до них можна достукатися) то у вікні буде відображатися робота, якщо ж програмі не вдалося достукатися - то вікно просто закривається, тому стежте уважно.  
Вам залишається лише відкрити папку у cmd у якій знаходяться DRipper.py разом зі start.py та IP.txt  
та запустити команду   
python3 start.py  

Далі коли з'являєтьcя нова ціль для атаки, вписуйте її замість старої у файл ІР.txt та ЗБЕРІГАЙТЕ ЗМІНИ, все нове вікно програми запущено.  


*Для Лінукс (тестив лише на Сервері, де доступний лише термінал)*  

З домашної папки прописуєте  
sudo git clone https://github.com/alexnest-ua/DRipper-py-Updated.git  
переходите у папку DRipper-py-Updated  
cd DRipper-py-Updated  


Відкривайте три вікна з терміналом  
переходьте у папку  
cd DRipper-py-Updated  
у ПЕРШОМУ вікні прописуєте   
python3 start.py  
ТА БІЛЬШЕ ЙОГО НЕ ЧІПАЄТЕ  
у ДРУГОМУ  вікні корегуєте нові цілі  
cat > IP.txt  
натискаєте "Ctrl+V", щоб вставити - Enter, щоб перейти на новий рядок - Ctrl+C, щоб завершити вставку  
  
у ТРЕТЬОМУ вікні відстежуєте стан усіх процесів:  
або команда  
sudo apt install top  - лише один раз прописуйте  
top  - дивитесь на python3  
або команда  
sudo apt install htop - лише один раз прописуйте  
htop - дивитесь на python3 DRipper.py  
  
якщо процесс знаходиться довше ~20-ти секунд у стані S - вбиваєте його:  
для top:  
Копіюєте PID процесу(цифри з першого стовпчика) з таблиці:  
натискаєте Ctrl+C якщо ви не натискали коли копіювали (бо на Гугл сервері можна просто виділіти бажане, та воно ВЖЕ скопійоване)  
прописуєте:  
sudo kill PID  
  
для htop:  
рухаєтеся стрілочкам (вгору вниз) до потрібного процесу  
натискаєте F9  
та Enter  

  
  
Якщо є якісь зауваження/пропозиції/питання - пиши в ЛС @brainqdead
