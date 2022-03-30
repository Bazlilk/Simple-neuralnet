import win32api
import win32con
import win32gui
print(f"Имя компьютера: {win32api.GetComputerName()}\n"
      f"Имя пользователя: {win32api.GetUserName()}\n"
      f"Версия операционной системы: \n"
      f"    Версия Windows: {win32api.GetVersionEx()[0]}.{win32api.GetVersionEx()[1]}\n"
      f"    Номер сборки: {win32api.GetVersionEx()[2]}\n"
      f"    Платформа операционной системы: {win32api.GetVersionEx()[3]}\n"
      f"Параметры: \n"
      f"    Анимации сварачивания и восстановления окон: "
      f"    {win32gui.SystemParametersInfo(win32con.SPI_GETANIMATION)}\n"
      f"    Режимы сглаживания шрифтов: {win32gui.SystemParametersInfo(win32con.SPI_GETFONTSMOOTHING)}")
# 15790320 было
print(win32api.SetSysColors(("58ab4921"),win32con.COLOR_MENU))
print(win32api.GetSysColor(win32con.COLOR_MENU))



