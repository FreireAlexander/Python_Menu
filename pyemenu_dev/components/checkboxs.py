from .texts import Text

not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

class Checkbox(Text):
    """
    Generate a Check Box with its label, this class extend from Text()
    some formats and effects are not available
    in some terminal emulators as Kitty, Alacritty, etc...
    properties:
        text: str         
    ***** Text Style *****
        fg: str # in html format, much color colud be found in Color() Class
        bg: str # in html format, much color colud be found in Color() Class
        bold: bool 
        italic: bool 
        underline: bool 
        blink: bool 
        reverse: bool 
        crossed: bool 
    """
    def __init__(self, label: str, id=None, box: str=' ', 
                name: str='',_class: str='', fg: str = not_fg, bg: str = not_bg,
                bold: bool = False, italic: bool = False, underline: bool = False,
                blink: bool = False, reverse: bool = False, crossed: bool = False):
        super().__init__(label, id, name,_class, fg, bg,
                bold, italic, underline, blink, reverse, crossed)
        self._text = ' '+label+' '
        self._lenght = len(self._text)
        self.styled = Text.setStyle(self, self._text, self.fg, self.bg, bold, italic, underline, blink, reverse, crossed)
        self.box = box
        self.print = f"{self.bg_rgb}{self.fg_rgb} [{self.box}{self.bg_rgb}]"\
                    +f"{self.bg_rgb}{self.styled}{self.bg_rgb} "\
                    +"\x1b[0m"
        
    
    def onSelect(self):
        if self.box == ' ':
            self.box = '*'
            self.print = f"{self.bg_rgb}{self.fg_rgb} [{self.box}{self.bg_rgb}]"\
                    +f"{self.bg_rgb}{self.styled}{self.bg_rgb} "\
                    +"\x1b[0m"
        else:
            self.box = ' '
            self.print = f"{self.bg_rgb}{self.fg_rgb} [{self.box}{self.bg_rgb}]"\
                    +f"{self.bg_rgb}{self.styled}{self.bg_rgb} "\
                    +"\x1b[0m"
    
    def clear(self):
        self.box = ' '
        self.print = f"{self.bg_rgb}{self.fg_rgb} [{self.box}{self.bg_rgb}]"\
                +f"{self.bg_rgb}{self.styled}{self.bg_rgb} "\
                +"\x1b[0m"