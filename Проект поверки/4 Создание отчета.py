import MOKO
from datetime import datetime

#Region Формирование отчета
MOKO.Program('tree', 'set', f'select = Формирование отчета')


MOKO.Program('Control', 'set', 'Save project report')
MOKO.Program('Control', 'set', 'Save word report')


MOKO.Program('tree', 'set', 'chosen=passed')
#EndRegion Формирование отчета:


MOKO.EndScript('passed')